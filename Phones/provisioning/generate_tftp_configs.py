#!/usr/bin/env python3

import argparse
import logging
import os
import shutil
from pathlib import Path

import yaml

LOGGER = logging.Logger(name=__name__, level=logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
LOGGER.addHandler(handler)

SECRETS_INPUT_FILE = "secrets.yaml"
SECRETS_CONFIG_FILE = "secret.cfg"
TFTP_OUT_SUBDIRECTORY = "tftp-out"
TFTP_COMMON_SRC_SUBDIRECTORY = "tftp-common-src"
DEVICE_CONFIG_PATH = "devices"
CONTACTS_CONFIG_PATH = "contacts"
COMMON_CONFIG_PATH = "common"
FIRMWARE_CONFIG_PATH = "firmware"
DIRECTORY_FILE_NAME = "000000000000-directory.xml"
PHONE_CONFIG_FILE = "phone_config.yaml"
FIRMWARE_FILE_NAME = "3111-48820-001.sip.ld"

BASE_XML_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!--
{comment}
-->
<APPLICATION
    CONFIG_FILES="common/common.cfg, common/secret.cfg, {device_config_file_path}"
    APP_FILE_PATH="/{firmware_config_path}/{firmware_file_name}"
    DECT_FILE_PATH=""
    SERVICE_FILES=""
    MISC_FILES=""
    LOG_FILE_DIRECTORY="/log"
    OVERRIDES_DIRECTORY=""
    CONTACTS_DIRECTORY="/{contacts_config_path}"
    LICENSE_DIRECTORY=""
    USER_PROFILES_DIRECTORY=""
    CALL_LISTS_DIRECTORY=""
    COREFILE_DIRECTORY=""
    CERTIFICATE_DIRECTORY=""
    FLK_DIRECTORY=""
/>
'''

DEVICE_XML_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!--
{comment}
-->
<PHONE_CONFIG>
    <ALL
            device.net.ipAddress="{phone_ipv4}"

            reg.1.address="{extension}"
            reg.1.auth.userId="{extension}"
            reg.1.label="{line_title}"
    />
</PHONE_CONFIG>
'''

SECRET_XML_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<PHONE_CONFIG>
    <ALL
            device.auth.localUserPassword="{local_user_password}"
            device.auth.localAdminPassword="{local_admin_password}"
            reg.1.auth.password="{sip_auth_password}"
/>
</PHONE_CONFIG>
'''

DIRECTORY_XML_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<directory>
    <item_list>{directory_item_list}
    </item_list>
</directory>
'''

DIRECTORY_ITEM_TEMPLATE = '''
        <item>
            <ln>{description}</ln>
            <ct>{extension}</ct>
        </item>'''


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    if os.path.exists(TFTP_OUT_SUBDIRECTORY):
        shutil.rmtree(TFTP_OUT_SUBDIRECTORY)
        LOGGER.info("Removed existing {tftp_out_subdirectory}.".format(
            tftp_out_subdirectory=TFTP_OUT_SUBDIRECTORY))

    os.mkdir(TFTP_OUT_SUBDIRECTORY)
    os.mkdir(os.path.join(TFTP_OUT_SUBDIRECTORY, DEVICE_CONFIG_PATH))
    os.mkdir(os.path.join(TFTP_OUT_SUBDIRECTORY, COMMON_CONFIG_PATH))
    os.mkdir(os.path.join(TFTP_OUT_SUBDIRECTORY, CONTACTS_CONFIG_PATH))
    LOGGER.info("Created empty {tftp_out_subdirectory}.".format(
        tftp_out_subdirectory=TFTP_OUT_SUBDIRECTORY))

    with open(SECRETS_INPUT_FILE, 'r') as f:
        secrets_data = yaml.load(f, Loader=yaml.SafeLoader)

    secrets_xml = SECRET_XML_TEMPLATE.format(
        local_user_password=secrets_data['secrets']['local_user_password'],
        local_admin_password=secrets_data['secrets']['local_admin_password'],
        sip_auth_password=secrets_data['secrets']['sip_auth_password'])

    secrets_file_path = os.path.join(TFTP_OUT_SUBDIRECTORY, COMMON_CONFIG_PATH, SECRETS_CONFIG_FILE)
    with open(secrets_file_path, 'w') as f:
        f.write(secrets_xml)
    LOGGER.info("Wrote secrets to {path}.".format(
        path=secrets_file_path))

    with open(PHONE_CONFIG_FILE, 'r') as f:
        phone_config_data = yaml.load(f, Loader=yaml.SafeLoader)

    LOGGER.info("Loaded {num_lines} lines and {num_groups} groups from {phone_config_file_name}".format(
        num_lines=len(phone_config_data['lines']),
        num_groups=len(phone_config_data['groups']),
        phone_config_file_name=PHONE_CONFIG_FILE))

    directory_item_list = ""

    for line in phone_config_data['lines']:
        description = line['description']
        extension = line['extension']
        line_title = line['line_title']
        phone_mac = line['phone_mac']
        phone_ipv4 = line['phone_ipv4']

        LOGGER.info(f"Processing line {extension} ({description}).".format(
            extension=extension,
            description=description))

        line_title_with_extension = "{extension} - {line_title}".format(
            extension=extension,
            line_title=line_title)

        description_with_extension = "{extension} - {description}".format(
            extension=extension,
            description=description)

        comment = ("Description: {description}\n"
                   "Extension: {extension}\n"
                   "Line Title: {line_title}\n"
                   "Phone MAC: {phone_mac}\n"
                   "Phone IPv4: {phone_ipv4}".format(description=description,
                                                     extension=extension,
                                                     line_title=line_title_with_extension,
                                                     phone_mac=phone_mac,
                                                     phone_ipv4=phone_ipv4))

        device_xml = DEVICE_XML_TEMPLATE.format(
            comment=comment,
            phone_ipv4=phone_ipv4,
            extension=extension,
            line_title=line_title_with_extension)

        device_config_file_name = "{extension}-{line_title_filename}.cfg".format(
            extension=extension,
            line_title_filename=line_title.lower().strip().replace(" / ", '-').replace(' ', '-'))

        device_config_relative_path = os.path.join(DEVICE_CONFIG_PATH, device_config_file_name)
        device_config_file_path = os.path.join(TFTP_OUT_SUBDIRECTORY, device_config_relative_path)

        with open(device_config_file_path, 'w') as f:
            f.write(device_xml)
        LOGGER.info("Wrote {path} for line {extension}.".format(
            extension=extension,
            path=device_config_file_path))

        base_xml = BASE_XML_TEMPLATE.format(
            comment=comment,
            device_config_file_path=device_config_relative_path,
            firmware_config_path=FIRMWARE_CONFIG_PATH,
            contacts_config_path=CONTACTS_CONFIG_PATH,
            firmware_file_name=FIRMWARE_FILE_NAME)

        mac_formatted = phone_mac.lower().strip().replace(':', '').replace('-', '')

        base_xml_filename = "{mac_formatted}.cfg".format(
            mac_formatted=mac_formatted)

        base_config_file_path = os.path.join(TFTP_OUT_SUBDIRECTORY, base_xml_filename)

        with open(base_config_file_path, 'w') as f:
            f.write(base_xml)
        LOGGER.info("Wrote {path} for line {extension}.".format(
            extension=extension,
            path=base_config_file_path))

        directory_item = DIRECTORY_ITEM_TEMPLATE.format(
            description=description_with_extension,
            extension=extension
        )

        directory_item_list += directory_item

    for group in phone_config_data['groups']:
        description = group['description']
        extension = group['extension']

        LOGGER.info(f"Processing group {extension} ({description}).".format(
            extension=extension,
            description=description))

        group_description_with_extension = "{extension} - {description}".format(
            extension=extension,
            description=description)

        directory_item = DIRECTORY_ITEM_TEMPLATE.format(
            description=group_description_with_extension,
            extension=extension
        )

        directory_item_list += directory_item

    directory_xml = DIRECTORY_XML_TEMPLATE.format(
        directory_item_list=directory_item_list)

    directory_file_path = os.path.join(TFTP_OUT_SUBDIRECTORY, CONTACTS_CONFIG_PATH, DIRECTORY_FILE_NAME)

    with open(directory_file_path, 'w') as f:
        f.write(directory_xml)

    LOGGER.info("Wrote directory to {path}.".format(
        path=directory_file_path))

    for filename in Path(TFTP_COMMON_SRC_SUBDIRECTORY).glob('**/*'):
        relative_file_src_path = os.path.relpath(str(filename), TFTP_COMMON_SRC_SUBDIRECTORY)
        if os.path.isdir(filename):
            if not os.path.exists(os.path.join(TFTP_OUT_SUBDIRECTORY, relative_file_src_path)):
                os.mkdir(os.path.join(TFTP_OUT_SUBDIRECTORY, relative_file_src_path))
        else:
            full_file_src_path = os.path.join(TFTP_COMMON_SRC_SUBDIRECTORY, relative_file_src_path)
            file_output_path = os.path.join(TFTP_OUT_SUBDIRECTORY, relative_file_src_path)
            shutil.copy(full_file_src_path, file_output_path)
            LOGGER.info("Copied common file {file_src_path} to {file_output_path}".format(
                file_src_path=full_file_src_path,
                file_output_path=file_output_path))


if __name__ == "__main__":
    main()
