'''
Parse CSV files to plot for the G_ReX EMI spectrum analysis at HCRO
Marc jacquart 2024-04-05
'''

import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


# Create main dataframe
df_list = []
csv_filenames = ["baseline",
                 "closed",
                 "open",
                 "absorber"]

for csv_filename in csv_filenames:
    df_tmp = pd.read_csv(
        f"{csv_filename}.csv",
        skiprows = 45,
        names = [f"{csv_filename}_freq", f"{csv_filename}_ampl"])
    df_list.append(df_tmp)

df = pd.concat(df_list, axis = 1) #ignore_index=True


def find_EMI_peaks(filename):
    '''
    Find EMI peaks:
    inputs:
    - filename: name of the file. e.g.: 'baseline'

    outputs: peak_frequencies, peak_amplitudes
    - peak_frequencies: Array containing the peak frequency values
    - peak_amplitudes: Array containing the peak amplitude values
    '''

    peak_indices, _ = find_peaks(df[f"{filename}_ampl"], threshold = 30, distance = 5 )
    peak_frequencies = df[f"{filename}_freq"].iloc[peak_indices]
    peak_amplitudes = df[f"{filename}_ampl"].iloc[peak_indices]
    print("---")
    print(filename)
    print(peak_frequencies)
    print(peak_amplitudes)
    print("---")
    print(" ")
    return peak_frequencies, peak_amplitudes

# individual plots:
for name in  csv_filenames:
    plt.clf()
    fig, ax = plt.subplots(figsize=(8,6),dpi=800)
    plt.plot(df[f"{name}_freq"]/1e9,df[f"{name}_ampl"], color='blue')
    plt.xlabel("Frequency [GHz]")
    plt.ylabel("dBm")
    plt.grid(axis = 'y', color='k', linestyle='-', linewidth=1, alpha = 0.2)
    plt.grid(axis = 'x', color='k', linestyle='-', linewidth=1, alpha = 0.2)
    plt.savefig(f"{name}_spectrum.jpg")


# Comparison to baseline:
for name in ["closed", "open", "absorber"]:
    plt.clf()
    fig, ax = plt.subplots(figsize=(8,6),dpi=800)
    plt.plot(df[f"{name}_freq"]/1e9,df[f"{name}_ampl"], label=name, color = 'blue')
    plt.plot(df["baseline_freq"]/1e9,df["baseline_ampl"], label='baseline', color = 'grey')
    peak_frequencies_tmp, peak_amplitudes_tmp = find_EMI_peaks(filename = name)
    plt.xlabel("Frequency [GHz]")
    plt.ylabel("dBm")
    plt.legend()
    plt.grid(axis = 'y', color='k', linestyle='-', linewidth=1, alpha = 0.2)
    plt.grid(axis = 'x', color='k', linestyle='-', linewidth=1, alpha = 0.2)
    plt.savefig(f"{name}_comparison_spectrum.jpg")
