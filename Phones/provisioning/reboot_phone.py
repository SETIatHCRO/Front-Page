#!/usr/bin/env python3

import argparse
import logging

import requests
import yaml

LOGGER = logging.Logger(name=__name__, level=logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
LOGGER.addHandler(handler)

SECRETS_INPUT_FILE = "secrets.yaml"
PHONE_CONFIG_FILE = "phone_config.yaml"

RESTART_URL = "http://{ip_address}/api/v1/mgmt/safeRestart"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", default=None)
    args = parser.parse_args()

    with open(SECRETS_INPUT_FILE, 'r') as f:
        secrets_data = yaml.load(f, Loader=yaml.SafeLoader)

    local_admin_password = secrets_data['secrets']['local_admin_password']

    admin_password = None

    input = args.ip

    if len(input) == 3:
        # It's an extension or "all".

        with open(PHONE_CONFIG_FILE, 'r') as f:
            phone_config_data = yaml.load(f, Loader=yaml.SafeLoader)

        if input == "all":
            LOGGER.info("Restarting all phones. Found {count} phones to restart.".format(
                count=len(phone_config_data['lines'])))
            for line in phone_config_data['lines']:
                description = line['description']
                extension = line['extension']
                phone_ipv4 = line['phone_ipv4']
                LOGGER.info("About to restart line {extension}, \"{description}\".".format(
                    extension=extension,
                    description=description))
                try:
                    restart_phone(ip_address=phone_ipv4,
                                  local_admin_password=local_admin_password)
                except Exception:
                    LOGGER.info("FAILED to restart line {extension}, \"{description}\" at IP {ip_address}.".format(
                        extension=extension,
                        description=description,
                        ip_address=phone_ipv4))
        else:
            # It's a single extension.
            found = False
            for line in phone_config_data['lines']:
                description = line['description']
                extension = line['extension']
                phone_ipv4 = line['phone_ipv4']
                if str(extension) == str(input):
                    found = True
                    LOGGER.info("Found phone with extension {extension}: \"{description}\" at IP {ip_address}.".format(
                        extension=extension,
                        description=description,
                        ip_address=phone_ipv4))
                    try:
                        restart_phone(ip_address=phone_ipv4,
                                      local_admin_password=local_admin_password)
                    except Exception:
                        LOGGER.info("FAILED to restart line {extension}, \"{description}\" at IP {ip_address}.".format(
                            extension=extension,
                            description=description,
                            ip_address=phone_ipv4))
            if not found:
                LOGGER.error("Did not find phone with extension {extension} to reboot.".format(
                    extension=input))
    else:
        restart_phone(ip_address=input,
                      local_admin_password=local_admin_password)


def restart_phone(ip_address, local_admin_password):
    LOGGER.info("Restarting phone with IP {ip_address}.".format(
        ip_address=ip_address))

    response = requests.post(
        RESTART_URL.format(
            ip_address=ip_address),
        auth=("Polycom", local_admin_password),
        json={},
        timeout=3)

    response_code = response.status_code
    LOGGER.info("Got HTTP {response_code} from safeRestart API.".format(response_code=response_code))

    if response_code != 200:
        LOGGER.error("Error restarting phone {ip_address}. Got HTTP {response_code}.".format(
            ip_address=ip_address,
            response_code=response_code))
        raise Exception("Failed to restart phone {ip_address}.".format(
            ip_address=ip_address))

    response_json = response.json()

    status_code = response_json["Status"]

    LOGGER.info("Got Poly status code {status_code} from safeRestart API.".format(status_code=status_code))

    if status_code != "2000":
        LOGGER.error("Error restarting phone {ip_address}. Got Poly status code {status_code}.".format(
            ip_address=ip_address,
            status_code=status_code))
        raise Exception("Failed to restart phone {ip_address}.".format(
            ip_address=ip_address))

    LOGGER.info("SUCCESS: Successfully restarted phone {ip_address}.".format(
        ip_address=ip_address))


if __name__ == "__main__":
    main()
