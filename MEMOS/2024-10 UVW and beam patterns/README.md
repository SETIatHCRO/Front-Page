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
The script, if run as-is, should generate the plots below. UV coverage and simulated beam pattern (amongst others) for a **2h track** of the calibrator **3c48** at **3GHz** (assuming a single frequency observation):

### UV-coverage
<img width="1134" alt="Screenshot 2024-12-06 at 10 36 46 AM" src="https://github.com/user-attachments/assets/271a79e4-708f-438f-9457-3126dc6d32ec">

### Synthesized beam pattern with primary beam attenuation
<img width="1250" alt="Screenshot 2024-12-06 at 10 37 21 AM" src="https://github.com/user-attachments/assets/789056e2-9a60-408a-8bec-8bdd90b5c8bd">


### UV-coverage with antenna `6c` uncommented in the `telinfo_ata.toml`:
This is the potential position of the 43rd ATA antenna
<img width="1113" alt="Screenshot 2024-12-06 at 10 41 26 AM" src="https://github.com/user-attachments/assets/58c390d0-d02c-456c-88fa-977655899050">

