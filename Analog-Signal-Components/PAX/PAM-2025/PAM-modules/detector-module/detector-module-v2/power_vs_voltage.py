import pandas as pd
###calculate z values needed to search for pulsar candidate

import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord
from argparse import ArgumentParser
import matplotlib.pyplot as plt
from astropy.coordinates import ICRS
from astropy.coordinates import Galactic
from astropy.wcs import WCS
from astropy.time import Time
from pylab import rcParams
from astropy.io import fits
#import aplpy
from astropy.nddata import Cutout2D
from reproject import reproject_interp
from astropy import constants as const
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.cm as cm
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.colors import LinearSegmentedColormap, LogNorm
import matplotlib.colors as colors
from matplotlib.legend_handler import HandlerTuple
import matplotlib as mpl
mpl.rcParams['axes.axisbelow'] = False  # Set globally

rcParams.keys()
rcParams['font.family'] = 'serif'
params = {'axes.labelsize': 20,'axes.linewidth': 1.5, 'legend.fontsize': 16,'legend.frameon': True,'lines.linewidth': 2,'xtick.direction': 'in','xtick.labelsize': 20,'xtick.major.bottom': True,'xtick.major.pad': 20,'xtick.major.size': 20,'xtick.major.width': 1,'xtick.minor.bottom': True,'xtick.minor.pad': 10,'xtick.minor.size': 10,'xtick.minor.top': True,'xtick.minor.visible': True,'xtick.minor.width': 1,'xtick.top': True,'ytick.direction': 'in','ytick.labelsize': 20,'ytick.major.pad': 20,'ytick.major.size': 20,'ytick.major.width': 1,
    'ytick.minor.pad': 10,'ytick.minor.size': 10,'ytick.minor.visible': True,'ytick.minor.width': 1,
    'ytick.right': True, 'figure.figsize' : (15, 12)}
rcParams.update(params)

df1 = pd.read_excel('PV_measurements.xlsx', sheet_name='Sheet1')  # optional sheet_name

det_array1 = df1['Detector output (dB)'].to_numpy()
volt_array1 = df1['Voltage (V)'].to_numpy()

###--------------------------------------------------------------------------------
df2 = pd.read_excel('PV_measurements.xlsx', sheet_name='Sheet2')  # optional sheet_name

det_array2 = df2['Detector output (dB)'].to_numpy()
volt_array2 = df2['Voltage (V)'].to_numpy()

###--------------------------------------------------------------------------------
df3 = pd.read_excel('PV_measurements.xlsx', sheet_name='Sheet3')  # optional sheet_name

det_array3 = df3['Detector output (dB)'].to_numpy()
volt_array3 = df3['Voltage (V)'].to_numpy()

###--------------------------------------------------------------------------------
df4 = pd.read_excel('PV_measurements.xlsx', sheet_name='Sheet4')  # optional sheet_name

det_array4 = df4['Detector output (dB)'].to_numpy()
volt_array4 = df4['Voltage (V)'].to_numpy()

###--------------------------------------------------------------------------------
df5 = pd.read_excel('PV_measurements.xlsx', sheet_name='Sheet5')  # optional sheet_name

det_array5 = df5['Detector output (dB)'].to_numpy()
volt_array5 = df5['Voltage (V)'].to_numpy()

###--------------------------------------------------------------------------------

l1,= plt.plot(det_array1, volt_array1*1, marker='o', c='tab:blue', label='1 GHz')
l2,= plt.plot(det_array2, volt_array2*1, marker='o', c='tab:orange', label='5 GHz')
l3,= plt.plot(det_array3, volt_array3*1, marker='o', c='g', label='10 GHz')
l4,= plt.plot(det_array4, volt_array4*1, marker='o', c='r', label='15 GHz')
l5,= plt.plot(det_array5, volt_array5*1, marker='o', c='tab:purple', label='18 GHz')

l6,= plt.plot(det_array1, volt_array1*5, marker='o', c='tab:blue', alpha=0.5, label='1 GHz')
l7,= plt.plot(det_array2, volt_array2*5, marker='o', c='tab:orange', alpha=0.5, label='5 GHz')
l8,= plt.plot(det_array3, volt_array3*5, marker='o', c='g', alpha=0.5, label='10 GHz')
l9,= plt.plot(det_array4, volt_array4*5, marker='o', c='r', alpha=0.5, label='15 GHz')
l10,= plt.plot(det_array5, volt_array5*5, marker='o', c='tab:purple', alpha=0.5, label='18 GHz')

l11,= plt.plot(det_array1, volt_array1*10, marker='o', c='tab:blue', alpha=0.2, label='1 GHz')
l12,= plt.plot(det_array2, volt_array2*10, marker='o', c='tab:orange', alpha=0.2, label='5 GHz')
l13,= plt.plot(det_array3, volt_array3*10, marker='o', c='g', alpha=0.2, label='10 GHz')
l14,= plt.plot(det_array4, volt_array4*10, marker='o', c='r', alpha=0.2, label='15 GHz')
l15,= plt.plot(det_array5, volt_array5*10, marker='o', c='tab:purple', alpha=0.2, label='18 GHz')

header1 = Line2D([], [], color='none', label='1 G')
header2 = Line2D([], [], color='none', label='5 G')
header3 = Line2D([], [], color='none', label='10 G')

# Combine: header row first, then actual plot handles
handles = [header1, l1, l2, l3, l4, l5, header2, l6, l7, l8, l9, l10, header3, l11, l12, l13, l14, l15]
labels = [h.get_label() for h in handles]

# Function to find and mark intersections with y = 4
def mark_intersections(det_array, volt_array, gain_factor, color, alpha):
    volt_scaled = volt_array * gain_factor
    for i in range(len(volt_scaled) - 1):
        v1, v2 = volt_scaled[i], volt_scaled[i+1]
        if (v1 - 4) * (v2 - 4) < 0:  # Sign change = crossing
            d1, d2 = det_array[i], det_array[i+1]
            # Linear interpolation
            det_cross = np.interp(4, [v1, v2], [d1, d2])
            plt.plot(det_cross, 4, 'x', color=color, alpha=alpha, markersize=10, label=None)

# Call it for each curve (you can automate this too)
mark_intersections(det_array1, volt_array1, 1, 'tab:blue', 1.0)
mark_intersections(det_array2, volt_array2, 1, 'tab:orange', 1.0)
mark_intersections(det_array3, volt_array3, 1, 'g', 1.0)
mark_intersections(det_array4, volt_array4, 1, 'r', 1.0)
mark_intersections(det_array5, volt_array5, 1, 'tab:purple', 1.0)

mark_intersections(det_array1, volt_array1, 5, 'tab:blue', 0.5)
mark_intersections(det_array2, volt_array2, 5, 'tab:orange', 0.5)
mark_intersections(det_array3, volt_array3, 5, 'g', 0.5)
mark_intersections(det_array4, volt_array4, 5, 'r', 0.5)
mark_intersections(det_array5, volt_array5, 5, 'tab:purple', 0.5)

mark_intersections(det_array1, volt_array1, 10, 'tab:blue', 0.2)
mark_intersections(det_array2, volt_array2, 10, 'tab:orange', 0.2)
mark_intersections(det_array3, volt_array3, 10, 'g', 0.2)
mark_intersections(det_array4, volt_array4, 10, 'r', 0.2)
mark_intersections(det_array5, volt_array5, 10, 'tab:purple', 0.2)



def find_crossings(x, y, threshold=4.0):
    crossings = []
    for i in range(len(y) - 1):
        y1, y2 = y[i], y[i+1]
        if (y1 - threshold) * (y2 - threshold) < 0:
            # crossing occurs between i and i+1
            x1, x2 = x[i], x[i+1]
            # linear interpolation
            x_cross = np.interp(threshold, [y1, y2], [x1, x2])
            crossings.append(x_cross)
    return crossings

# Group data: (det_array, volt_array, gain_factor, label)
curve_data = [
    (det_array1, volt_array1, 1, '1 GHz (Gain 1x)'),
    (det_array2, volt_array2, 1, '5 GHz (Gain 1x)'),
    (det_array3, volt_array3, 1, '10 GHz (Gain 1x)'),
    (det_array4, volt_array4, 1, '15 GHz (Gain 1x)'),
    (det_array5, volt_array5, 1, '18 GHz (Gain 1x)'),

    (det_array1, volt_array1, 5, '1 GHz (Gain 5x)'),
    (det_array2, volt_array2, 5, '5 GHz (Gain 5x)'),
    (det_array3, volt_array3, 5, '10 GHz (Gain 5x)'),
    (det_array4, volt_array4, 5, '15 GHz (Gain 5x)'),
    (det_array5, volt_array5, 5, '18 GHz (Gain 5x)'),

    (det_array1, volt_array1, 10, '1 GHz (Gain 10x)'),
    (det_array2, volt_array2, 10, '5 GHz (Gain 10x)'),
    (det_array3, volt_array3, 10, '10 GHz (Gain 10x)'),
    (det_array4, volt_array4, 10, '15 GHz (Gain 10x)'),
    (det_array5, volt_array5, 10, '18 GHz (Gain 10x)')
]

print("\n--- 4V CROSSINGS ---")
for det, volt, gain, label in curve_data:
    volt_scaled = volt * gain
    crossings = find_crossings(det, volt_scaled, threshold=4.0)
    if crossings:
        for cross in crossings:
            print(f"{label}: crosses 4V at ~ {cross:.2f} dBm")
    else:
        print(f"{label}: no 4V crossing")


plt.axhline(y=4, color='k', linewidth=3)
plt.axhline(y=0.1, color='k', alpha=0.5, linestyle='--', linewidth=3)
plt.axvline(x=-10, color='k', linestyle='--', linewidth=3)
plt.axvline(x=-20, color='k', alpha=0.5, linestyle='--', linewidth=3)
plt.axvline(x=0, color='k', alpha=0.5, linestyle='--', linewidth=3)

plt.yscale('log')
plt.xlabel(r'$P_{in}$ (dBm)')
plt.ylabel('Output Volgage (V)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.title('Measured voltage-to-power curve of detector module; OpAmp Gain= 1, 5, 10 G', fontsize=20)

plt.legend(handles, labels, ncol=3, loc='upper left', frameon=True)

plt.tight_layout()
plt.savefig('PV_measured_OpAmp_Gain_all.pdf')
plt.show()

