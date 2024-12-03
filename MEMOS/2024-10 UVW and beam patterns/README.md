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
The script, if run as-is, should generate the plots below. UV coverage and simulated beam pattern (amongst others) for a **6h track** of the calibrator **3c286** at **3GHz**:

### UV-coverage
<img width="1096" alt="Screenshot 2024-12-02 at 2 57 07 PM" src="https://github.com/user-attachments/assets/d658dbac-f7d4-4000-954f-f25b7feb2add">

### Synthesized beam pattern with primary beam attenuation
<img width="1327" alt="Screenshot 2024-12-02 at 3 55 41 PM" src="https://github.com/user-attachments/assets/98e0534a-eeb4-4dc1-ba6f-459783a7aa22">

### UV-coverage with antenna `6c` uncommented in the `telinfo_ata.toml`:
This is the potential position of the 43rd ATA antenna
<img width="1110" alt="Screenshot 2024-12-02 at 3 07 42 PM" src="https://github.com/user-attachments/assets/57a73cd5-25b8-4886-a9e9-dc7b1233a2cc">

