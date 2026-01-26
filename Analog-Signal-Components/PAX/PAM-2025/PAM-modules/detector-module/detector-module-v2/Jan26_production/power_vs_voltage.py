import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
from matplotlib.lines import Line2D
import matplotlib as mpl

mpl.rcParams['axes.axisbelow'] = False  # Set globally

rcParams.keys()
rcParams['font.family'] = 'serif'
params = {'axes.labelsize': 20,'axes.linewidth': 1.5, 'legend.fontsize': 16,'legend.frameon': True,'lines.linewidth': 2,'xtick.direction': 'in','xtick.labelsize': 20,'xtick.major.bottom': True,'xtick.major.pad': 20,'xtick.major.size': 20,'xtick.major.width': 1,'xtick.minor.bottom': True,'xtick.minor.pad': 10,'xtick.minor.size': 10,'xtick.minor.top': True,'xtick.minor.visible': True,'xtick.minor.width': 1,'xtick.top': True,'ytick.direction': 'in','ytick.labelsize': 20,'ytick.major.pad': 20,'ytick.major.size': 20,'ytick.major.width': 1,
    'ytick.minor.pad': 10,'ytick.minor.size': 10,'ytick.minor.visible': True,'ytick.minor.width': 1,
    'ytick.right': True, 'figure.figsize' : (15, 12)}
rcParams.update(params)
module = 'module002'

df1 = pd.read_excel(f'pv_{module}.xlsx', sheet_name='Sheet 1')  # optional sheet_name

det_array1 = df1['Output level (dBm)'].to_numpy()
volt_array1 = df1['Voltage (V)'].to_numpy()

###--------------------------------------------------------------------------------
df2 = pd.read_excel(f'pv_{module}.xlsx', sheet_name='Sheet 2')  # optional sheet_name

det_array2 = df2['Output level (dBm)'].to_numpy()
volt_array2 = df2['Voltage (V)'].to_numpy()

###--------------------------------------------------------------------------------
df3 = pd.read_excel(f'pv_{module}.xlsx', sheet_name='Sheet 3')  # optional sheet_name

det_array3 = df3['Output level (dBm)'].to_numpy()
volt_array3 = df3['Voltage (V)'].to_numpy()

###--------------------------------------------------------------------------------
df4 = pd.read_excel(f'pv_{module}.xlsx', sheet_name='Sheet 4')  # optional sheet_name

det_array4 = df4['Output level (dBm)'].to_numpy()
volt_array4 = df4['Voltage (V)'].to_numpy()

###--------------------------------------------------------------------------------
df5 = pd.read_excel(f'pv_{module}.xlsx', sheet_name='Sheet 5')  # optional sheet_name

det_array5 = df5['Output level (dBm)'].to_numpy()
volt_array5 = df5['Voltage (V)'].to_numpy()

###--------------------------------------------------------------------------------

l1,= plt.plot(det_array1, volt_array1*1, marker='o', c='tab:blue', label='1 GHz')
l2,= plt.plot(det_array2, volt_array2*1, marker='o', c='tab:orange', label='5 GHz')
l3,= plt.plot(det_array3, volt_array3*1, marker='o', c='g', label='10 GHz')
l4,= plt.plot(det_array4, volt_array4*1, marker='o', c='r', label='15 GHz')
l5,= plt.plot(det_array5, volt_array5*1, marker='o', c='tab:purple', label='18 GHz')

# Combine: header row first, then actual plot handles
handles = [l1, l2, l3, l4, l5]
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
    (det_array1, volt_array1, 1, '1 GHz'),
    (det_array2, volt_array2, 1, '5 GHz'),
    (det_array3, volt_array3, 1, '10 GHz'),
    (det_array4, volt_array4, 1, '15 GHz'),
    (det_array5, volt_array5, 1, '18 GHz')

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
plt.title(f'Measured voltage-to-power curve of detector {module}', fontsize=20)

plt.legend(handles, labels, ncol=3, loc='upper left', frameon=True)

plt.tight_layout()
plt.savefig(f'{module}_PV_measured.pdf')
plt.show()

