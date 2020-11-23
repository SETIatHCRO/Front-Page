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


#read the files into the script

Champ=pd.read_csv('beam_4_0_GHz.dat', sep=',')


#HFSS=pd.read_csv('opt_res_011_hr_all_modes.csv', sep=',')


#VNA=pd.read_csv('OMT_003/OMT_transition_1.txt', sep='\t')
#VNA2=pd.read_csv('OMT_003/OMT_transition_CrossPolar.txt', sep='\t')


angle_0_x1 = np.zeros(shape=(361),dtype=float)
value_0_x1 = np.zeros(shape=(361),dtype=float)

angle_0_x2 = np.zeros(shape=(361),dtype=float)
value_0_x2 = np.zeros(shape=(361),dtype=float)

angle_45_x1 = np.zeros(shape=(361),dtype=float)
value_45_x1 = np.zeros(shape=(361),dtype=float)

angle_45_x2 = np.zeros(shape=(361),dtype=float)
value_45_x2 = np.zeros(shape=(361),dtype=float)

angle_90_x1 = np.zeros(shape=(361),dtype=float)
value_90_x1 = np.zeros(shape=(361),dtype=float)

angle_90_x2 = np.zeros(shape=(361),dtype=float)
value_90_x2 = np.zeros(shape=(361),dtype=float)

N =361
#defines the columns by the file header

print (Champ.columns) #writes the simulated values in columns
for i in range (N):
 angle_0_x1[i] = Champ['SolidAngle []'].values[i]
 value_0_x1[i] = Champ['dB []'].values[i]

 angle_0_x2[i] = Champ['SolidAngle []'].values[i+N]
 value_0_x2[i] = Champ['dB []'].values[i+N]

 angle_45_x1[i] = Champ['SolidAngle []'].values[i + N*2]
 value_45_x1[i] = Champ['dB []'].values[i + N*2]

 angle_45_x2[i] = Champ['SolidAngle []'].values[i + N * 3]
 value_45_x2[i] = Champ['dB []'].values[i + N * 3]

 angle_90_x1[i] = Champ['SolidAngle []'].values[i + N * 4]
 value_90_x1[i] = Champ['dB []'].values[i + N * 4]

 angle_90_x2[i] = Champ['SolidAngle []'].values[i + N * 5]
 value_90_x2[i] = Champ['dB []'].values[i + N * 5]



norm_dB =np.amax(value_0_x1)


value_0_x1 = value_0_x1 -norm_dB
value_45_x1 = value_45_x1 -norm_dB
value_90_x1 = value_90_x1 -norm_dB

value_0_x2 = value_0_x2 -norm_dB
value_45_x2= value_45_x2 -norm_dB
value_90_x2 = value_90_x2 -norm_dB





plt.figure()

#plt.plot(VNA_freq, VNA_S11,label="Measured RL")
#plt.plot(VNA_freq, VNA_S12,label='Measured IL')
#plt.plot(VNA2_freq, VNA2_S12,label='Measured CP')

plt.plot(angle_0_x1, value_0_x1,-angle_0_x1, value_0_x1, linewidth=1.5,label='H-field',color='r')
plt.plot(angle_90_x1, value_90_x1,-angle_90_x1, value_90_x1, linewidth=1.5,label='E-field',color='b')
plt.plot(angle_45_x1, value_45_x1,-angle_45_x1, value_45_x1, linewidth=1.5,label='45.0deg-field',color='g')
plt.plot(angle_45_x2, value_45_x2,-angle_45_x2, value_45_x2, linewidth=1.5,label='cross-polar',color='k')

#plt.plot(angle_90_x2, value_90_x2, linewidth=1.5,label='6')

plt.plot(HFSS_freq, HFSS_S14,label='Simulated CP')
plt.plot(HFSS_freq, HFSS_S14,label='simulated Cross-Polarisation')

#plt.plot(freq_sim2, sim_S12_CP, '-.', linewidth=1.5,label='simulated CP')
#plt.plot(freq_sim, sim_S11H, '-.', linewidth=1.5)

#'-.'

#plt.errorbar(time_TSok1, Flux_TSok1, yerr=Error_TSok1, fmt='kx', color='0.55', label='9 > TS > 4')
#upperlims = Flux_TSpoor1
#plt.errorbar(time_TSpoor1, Flux_TSpoor1, xerr=None, yerr=0.2E-7, fmt=None, ecolor='0.50', \
#   lolims=True,capsize=3,elinewidth=1,mew=0)

plt.xlim(-90, 90)
plt.ylim(-70,5)
plt.ylabel('Magnitude (dB)')
plt.xlabel('Angle (deg)')

plt.grid(True)

plt.xticks([-90,-60,-30,0,30,60,90])
#plt.yticks([-20,-25,-30,-35,-40,-45,-50,-55])



plt.rcParams.update({'font.size': 12})



plt.plot((-12.8, -12.8), (30, -80), 'k:',linewidth=2.0)
plt.plot((12.8, 12.8), (30, -80), 'k:',linewidth=2.0)
#plt.plot((3, 9), (-15, -15), 'k:',linewidth=2.0)

#legend = plt.legend(loc='best', shadow=True)
#leg = plt.gca().get_legend()
#ltext  = leg.get_texts()  # all the text.Text instance in the legend
#llines = leg.get_lines()  # all the lines.Line2D instance in the legend
#plt.setp(ltext, fontsize='small')
#plt.setp(llines, linewidth=1.5)      # the legend linewidth

plt.tight_layout()

plt.savefig('BeamPattern1GHz.pdf', bbox_inches="tight")
#plt.savefig('returnloss.pdf')
plt.show()

