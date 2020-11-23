'''Program to show Licght Curves of gamma-tay novae by showing stacked

graphs each with the same realtive scales'''



import numpy as np

import matplotlib.pylab as plt

import matplotlib as mat

import pandas as pd



import seaborn as sns

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


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

HFSS=pd.read_csv('BeamPattern12GHz.csv', sep=',')
#HFSS=pd.read_csv('opt_res_011_hr_all_modes.csv', sep=',')


#VNA=pd.read_csv('OMT_003/OMT_transition_1.txt', sep='\t')
#VNA2=pd.read_csv('OMT_003/OMT_transition_CrossPolar.txt', sep='\t')





#defines the columns by the file header

print (HFSS.columns) #writes the simulated values in columns
angle_0_x1 = HFSS['Theta [deg]'].values

value_0_x1 = HFSS['dB(rETotal) [] - Phi=0deg'].values
value_45_x1 = HFSS['dB(rETotal) [] - Phi=45deg'].values
value_90_x1 = HFSS['dB(rETotal) [] - Phi=90deg'].values

value_0_x2 = HFSS['dB(rEZ) [] - Phi=45deg'].values




#Normalasation of the beam pattern



norm_dB = np.amax(value_0_x1)

value_0_x1 = value_0_x1 - norm_dB
value_45_x1 = value_45_x1 - norm_dB
value_90_x1 = value_90_x1 - norm_dB

value_0_x2 = value_0_x2 - norm_dB




plt.figure(figsize=(10,7.5))




#plt.plot(VNA_freq, VNA_S11,label="Measured RL")
#plt.plot(VNA_freq, VNA_S12,label='Measured IL')
#plt.plot(VNA2_freq, VNA2_S12,label='Measured CP')

plt.plot(angle_0_x1, smooth(value_0_x1,5), linewidth=1.5,label='H-field',color='r')
plt.plot(angle_0_x1, smooth(value_90_x1,5), linewidth=1.5,label='E-field',color='b')
plt.plot(angle_0_x1, smooth(value_45_x1,5), linewidth=1.5,label='D-field',color='g')
plt.plot(angle_0_x1, smooth(value_0_x2,5), linewidth=1.5,label='cross-polar',color='k')




#plt.plot(angle_90_x2, value_90_x2, linewidth=1.5,label='6')

#plt.plot(HFSS_freq, HFSS_S14,label='Simulated CP')
#plt.plot(HFSS_freq, HFSS_S14,label='simulated Cross-Polarisation')

#plt.plot(freq_sim2, sim_S12_CP, '-.', linewidth=1.5,label='simulated CP')
#plt.plot(freq_sim, sim_S11H, '-.', linewidth=1.5)

#'-.'

#plt.errorbar(time_TSok1, Flux_TSok1, yerr=Error_TSok1, fmt='kx', color='0.55', label='9 > TS > 4')
#upperlims = Flux_TSpoor1
#plt.errorbar(time_TSpoor1, Flux_TSpoor1, xerr=None, yerr=0.2E-7, fmt=None, ecolor='0.50', \
#   lolims=True,capsize=3,elinewidth=1,mew=0)


plt.title('Beam Pattern @12GHz',fontsize=18)
plt.xlim(-180, 180)
plt.ylim(-30,5)
plt.ylabel('Magnitude (dB)',fontsize=16)
plt.xlabel('Angle (deg)',fontsize=16)
plt.grid(True)

plt.xticks([-180,-135,-90,-45,0,45,90,135,180],fontsize=12)
plt.yticks([0,-5,-10,-15,-20,-25,-30],fontsize=12)



#plt.rcParams.update({'font.size': 12})



#plt.plot((-12.8, -12.8), (30, -80), 'k:',linewidth=2.0)
#plt.plot((12.8, 12.8), (30, -80), 'k:',linewidth=2.0)
#plt.plot((3, 9), (-15, -15), 'k:',linewidth=2.0)

legend = plt.legend(loc='best', shadow=True)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()  # all the text.Text instance in the legend
llines = leg.get_lines()  # all the lines.Line2D instance in the legend
plt.setp(ltext, fontsize=10)
plt.setp(llines, linewidth=1.5)      # the legend linewidth

plt.tight_layout()

plt.savefig('BeamPattern12GHz.pdf', bbox_inches="tight")
#plt.savefig('returnloss.pdf')
plt.show()

