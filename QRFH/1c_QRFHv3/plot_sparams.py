import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib as mpl

ORDER = {"S11" : 0, "S21" : 1, "S12" : 2, "S22" : 3}
mpl.rcParams['axes.axisbelow'] = False  # Set globally

rcParams.keys()
rcParams['font.family'] = 'serif'
params = {'axes.labelsize': 20,'axes.linewidth': 1.5, 'legend.fontsize': 16,'legend.frameon': True,'lines.linewidth': 2,'xtick.direction': 'in',
    'xtick.labelsize': 20,'xtick.major.bottom': True,'xtick.major.pad': 20,'xtick.major.size': 20,'xtick.major.width': 1,'xtick.minor.bottom': True,
    'xtick.minor.pad': 10,'xtick.minor.size': 10,'xtick.minor.top': True,'xtick.minor.visible': True,'xtick.minor.width': 1,'xtick.top': True,
    'ytick.direction': 'in','ytick.labelsize': 20,'ytick.major.pad': 20,'ytick.major.size': 20,'ytick.major.width': 1,
    'ytick.minor.pad': 10,'ytick.minor.size': 10,'ytick.minor.visible': True,'ytick.minor.width': 1,
    'ytick.right': True, 'figure.figsize' : (15, 12)}
rcParams.update(params)

def read_cti_file(filepath):
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    # === 1. Extract frequency list ===
    freq_start = lines.index('VAR_LIST_BEGIN') + 1
    freq_end = lines.index('VAR_LIST_END')
    freq = np.array([float(line) for line in lines[freq_start:freq_end]])

    # === 2. Extract BEGIN...END blocks (S-parameters) ===
    s_blocks = []
    idx = 0
    while idx < len(lines):
        if lines[idx] == 'BEGIN':
            block = []
            idx += 1
            while idx < len(lines) and lines[idx] != 'END':
                real_imag = list(map(float, lines[idx].split(',')))
                block.append(complex(real_imag[0], real_imag[1]))
                idx += 1
            s_blocks.append(np.array(block))
        idx += 1

    # Makes the output agnostic to order of s-parameters in the original data file. Reorders so S11 always first
    file_order = [s[5:8] for s in lines[6:10]]
    file_order = {i : s for i, s in enumerate(file_order)}
    ordered_sblocks = [None] * len(s_blocks)
    for i in range(len(s_blocks)):
        ordered_sblocks[ORDER[file_order[i]]] = s_blocks[i]
        print("Moving ", file_order[i]," to ", ORDER[file_order[i]])
    s_blocks = ordered_sblocks

    # === 3. Validate block count ===
    if len(s_blocks) != 4:
        raise ValueError(f"Expected 4 S-parameter blocks, found {len(s_blocks)}")

    s11, s21, s12, s22 = s_blocks
    
    return freq, s11, s21, s12, s22




# === Replace with your filenames ===
feed = '005'
file1_path = f'{feed}.cti'

# === Read files ===
freq1, s11_1, s21_1, s12_1, s22_1 = read_cti_file(file1_path)

# === Plot S21 magnitude in dB ===
plt.figure(figsize=(10, 8))
plt.suptitle(f'LNA S-params feed{feed}', fontsize=18, y=0.90)

print ('freq1', freq1)
print ('s21_1', s21_1)

plt.plot(freq1 / 1e9, 20 * np.log10(np.abs(s11_1)), c='tab:orange', alpha=1.0, label='S11')
plt.plot(freq1 / 1e9, 20 * np.log10(np.abs(s21_1)), c='tab:blue', alpha=1.0, label='S21')
plt.plot(freq1 / 1e9, 20 * np.log10(np.abs(s12_1)), c='tab:red', alpha=1.0, label='S12')
plt.plot(freq1 / 1e9, 20 * np.log10(np.abs(s22_1)), c='tab:green', alpha=1.0, label='S22')

plt.ylim(-60, 10)
plt.xlim(0, 20)
plt.ylabel('Magnitude (dB)')
plt.xlabel('Frequency (GHz)')
plt.grid(True)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), borderaxespad=0, frameon=True, ncol=2)

plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.savefig(f"feed{feed}_Sparam_measurements.pdf")
plt.show()
