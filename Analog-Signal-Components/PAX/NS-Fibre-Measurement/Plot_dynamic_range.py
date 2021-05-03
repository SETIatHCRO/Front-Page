'''Program to show Licght Curves of gamma-tay novae by showing stacked

graphs each with the same realtive scales'''



import numpy as np

import matplotlib.pylab as plt

import matplotlib as mat

import pandas as pd
import sys


import seaborn as sns

import math


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






Data = pd.read_csv('2h_X_dynamic_range.csv', sep=',')

IN_X = Data['IN'].values
Att_X = Data['Att'].values
FF_X = Data['FF'].values
PS_X = Data['PS'].values



Data = pd.read_csv('2h_Y_dynamic_range.csv', sep=',')

IN_Y = Data['IN'].values
Att_Y = Data['Att'].values
FF_Y = Data['FF'].values
PS_Y = Data['PS'].values






plt.figure()

plt.plot(IN_X,(FF_X+6),linewidth=1.5,label='X-pol FieldFox')
plt.plot(IN_X,PS_X,linewidth=1.5,label='X-pol PowerSensor')

plt.plot(IN_Y,(FF_Y+6),linewidth=1.5,label='Y-pol FieldFox')
plt.plot(IN_Y,PS_Y,linewidth=1.5,label='Y-pol PowerSensor')

#plt.plot(10.5, -21.73, 'o')


#plt.annotate('',
#            xy=(10.5, -21.7),  # theta, radius
#            xytext=(0.55, 0.05),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='black', shrink=0.04),
#            horizontalalignment='left',
#            verticalalignment='bottom',
#            fontsize=15,)

plt.title('Antenna 2H')


plt.text(-7.7, 0, 'Operational range', fontsize=15,
        bbox={'facecolor':'green', 'alpha':0.2, 'pad':10})

plt.xlim(-26, 3)

plt.ylim(-19, 3)

plt.ylabel('Output Power detected in SPR (dBm)')

plt.xlabel('Input Power to RF-Fibre converter (dBm)')

plt.grid(True)

#plt.xticks([9,9.5,10,10.5,11,11.5,12])
plt.rcParams.update({'font.size': 12})

plt.plot((-8.2, -8.2), (-19, 3), 'k--',linewidth=2.0)
plt.plot((0.0, 0.0), (-19, 3), 'k--',linewidth=2.0)
#plt.plot((0, -10), (0, -10), 'k',linewidth=2.0,label='linear relationship')
#plt.plot((3, 9), (-15, -15), 'k:',linewidth=2.0)

legend = plt.legend(loc='best', shadow=True)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()  # all the text.Text instance in the legend
llines = leg.get_lines()  # all the lines.Line2D instance in the legend
plt.setp(ltext, fontsize='small')
plt.setp(llines, linewidth=1.5)      # the legend linewidth

plt.tight_layout()

plt.savefig('2h_dynamic_range.pdf', bbox_inches="tight")
plt.show()
