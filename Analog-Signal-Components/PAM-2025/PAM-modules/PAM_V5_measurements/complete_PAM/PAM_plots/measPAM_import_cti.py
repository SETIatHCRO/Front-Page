import math

def cti_import(filepath):
    '''imports a cti-file with four S-parameters, measured with the VNA'''

    # Initialize containers
    frequencies = []
    s11 = []
    s21 = []
    s12 = []
    s22 = []

    # Reading the .cti file
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # Flags for parsing
    data_section = False
    n = -1
    s = [frequencies,s11, s21, s12, s22]

    # Parsing the CitiFile
    for line in lines:
        line = line.strip()

        # Check for the beginning of the data section
        if line.startswith("BEGIN") or line.startswith("VAR_LIST_BEGIN"):
            data_section = True
            n += 1
            continue
        elif line.startswith("END") or line.startswith("VAR_LIST_END"):
            data_section = False
            continue

        # Process data section
        if data_section: # Extract real Part of S-parameters
            values = line.split(',')
            r = float(values[0]) #real part
            if n == 0: #frequencies
                f = r/1e9
                s[n].append(f)
            else: #S-Parameters
                i = float(values[1]) #imaginary part
                mag = math.sqrt(r**2+i**2) #magnitude
                mag_db = 20*math.log10(mag) #magnitude in dB
                s[n].append(mag_db)
    return frequencies, s11, s21, s12, s22