'''Program to show Licght Curves of gamma-tay novae by showing stacked

graphs each with the same realtive scales'''



import numpy as np

import matplotlib.pylab as plt

import matplotlib as mat

import pandas as pd



import seaborn as sns

sns.set_style("whitegrid",
              {'axes.edgecolor': '.2',
               'axes.facecolor': 'white',
               'axes.grid': True,
               'axes.linewidth': 0.5,
               'figure.facecolor': 'white',
               'grid.color': '.8',
               'grid.linestyle': u'-',
               'legend.frameon': True,
               'xtick.color': '.15',
               'xtick.direction': u'in',
               'xtick.major.size': 3.0,
               'xtick.minor.size': 1.0,
               'ytick.color': '.15',
               'ytick.direction': u'in',
               'ytick.major.size': 3.0,
               'ytick.minor.size': 1.0,
               })

sns.set_context("poster")


#HFSS=pd.read_csv('OMT_006_2.csv', sep=',')
#file=pd.read_csv('HPF_750MHz_sim.csv', sep=';')
file2=pd.read_csv('HPF_750MHz_sim.csv', sep=',')


#print file.columns #writes the simulated values in columns
#freq = file['freq[Hz]'].values/1e9
#S11 = file['db:Trc1_S11'].values
#S22 = file['db:Trc4_S22'].values
#S21 = file['db:Trc3_S21'].values
#S12 = file['db:Trc2_S12'].values

freq_2 = file2['F[GHz]'].values
S11_2 = file2['dB(S(Port1Port1))'].values
S12_2 = file2['dB(S(Port1Port2))'].values





plt.figure()

#plt.plot(VNA_freq, VNA_S11,label="Measured RL")
#plt.plot(VNA_freq, VNA_S12,label='Measured IL')
#plt.plot(VNA2_freq, VNA2_S12,label='Measured CP')


#plt.plot(freq, S11, linewidth=1.5,label='S11')
#plt.plot(freq, S12, linewidth=1.5,label='S21', color='orange')

plt.plot(freq_2, S11_2, linewidth=1.5,label='S11')
plt.plot(freq_2, S12_2, linewidth=1.5,label='S21')
#plt.plot(freq, S21_Isol, linewidth=1.5,label='RF Isolation', color='purple')
#plt.plot(freq, S13_I, linewidth=1.5,label='LO Leak')


#plt.annotate('',
#            xy=(12.8, 3.135),  # theta, radius
#            xytext=(0.4, 0.67),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='black', shrink=0.06),
#            horizontalalignment='left',
#            verticalalignment='bottom',
#            fontsize=15
#            )


#plt.text(5.38, -4, 'LO @ 4.0 GHz and 14 dBm', fontsize=15,
#        bbox={'facecolor':'grey', 'alpha':0.2, 'pad':10})



plt.xlim(0,3)
plt.ylim(-50,0)
plt.ylabel('Magnitude (dB)')
plt.xlabel('Frequency (GHz)')

plt.grid(True)

plt.xticks([0,0.5,0.75,1,1.5,2,2.5,3])
plt.yticks([0,-5,-10,-15,-20,-25,-30,-35,-40,-45,-50])



plt.rcParams.update({'font.size': 12})



#plt.plot((4, 4), (0, -80), 'k:',linewidth=2.0)
#plt.plot((8.5, 8.5), (0, -80), 'k:',linewidth=2.0)
#plt.plot((3, 9), (-15, -15), 'k:',linewidth=2.0)

legend = plt.legend(loc='best', shadow=True)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()  # all the text.Text instance in the legend
llines = leg.get_lines()  # all the lines.Line2D instance in the legend
plt.setp(ltext, fontsize='small')
plt.setp(llines, linewidth=1.5)      # the legend linewidth

plt.tight_layout()

plt.savefig('HPF_750MHz_sim.pdf', bbox_inches="tight")
#plt.savefig('returnloss.pdf')
plt.show()

