# ATA UVW Beam
Code to compute UVWs and simulate synthesized beam patterns

Dependencies
------------
- numpy
- scipy
- pandas
- pytoml
- astropy

To modify, comment/uncomment antennas in the `telinfo_ata.toml` file. Coordinates of source, time and length of observation can be modified inside the `compute_uvw.py` script

Usage
-----
`python compute_uvw.py`

Example plots:
--------------
The script, if run as-is, should generate the plots below. UV coverage and simulated beam pattern (amongst others) for a **2h track** of the calibrator **3c48** at **3GHz**:

### UV-coverage
<img width="1119" alt="Screenshot 2024-12-10 at 5 33 47 PM" src="https://github.com/user-attachments/assets/91e07d11-0b27-4474-b12c-f58e2719be33">

### UV-coverage (in wavelength)
<img width="1070" alt="Screenshot 2024-12-10 at 5 33 36 PM" src="https://github.com/user-attachments/assets/989da829-2809-421d-bcba-545310f4cd69">


### Synthesized beam pattern with primary beam attenuation
<img width="1207" alt="Screenshot 2024-12-10 at 5 32 49 PM" src="https://github.com/user-attachments/assets/6ae0ae33-d390-4c8f-bdf6-39bb7efa0d4e">

Zoomed in to +-0.2 deg

<img width="1160" alt="Screenshot 2024-12-10 at 5 39 32 PM" src="https://github.com/user-attachments/assets/3a9b95f6-ac23-4e14-be79-a17505507ff9">

### UV-coverage with antenna `6c` uncommented in the `telinfo_ata.toml`:
This is the potential position of the 43rd ATA antenna
<img width="1113" alt="Screenshot 2024-12-06 at 10 41 26 AM" src="https://github.com/user-attachments/assets/58c390d0-d02c-456c-88fa-977655899050">

### UV-coverage (in wavelength) with `6c`
<img width="1102" alt="Screenshot 2024-12-10 at 5 35 48 PM" src="https://github.com/user-attachments/assets/70774310-e8e8-4461-9ca4-010d5df5d8d3">


### Synthesized beam pattern with primary beam attenuation (with `6c`)
<img width="1198" alt="Screenshot 2024-12-10 at 5 35 19 PM" src="https://github.com/user-attachments/assets/11d06a61-ce44-4d75-9a9e-2d2fe2282763">

Zoomed in to +-0.2 deg

<img width="1144" alt="Screenshot 2024-12-10 at 5 37 55 PM" src="https://github.com/user-attachments/assets/d04625a2-2ef0-474d-b03a-d547561f24e4">
