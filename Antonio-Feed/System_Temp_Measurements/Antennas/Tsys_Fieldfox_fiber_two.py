import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

t_hot = 287
t_cold = 12
ant = '3c'
nm = '1'
date1= '23/02/21 09:40'

t_hot2 = 289
t_cold2 = 12
ant2 = '3c'
nm2 = '8'
date2='25/02/21 13:30'


cold_l_ing = np.zeros((801), dtype=float)
cold_r_ing = np.zeros((801), dtype=float)
hot_l_ing = np.zeros((801), dtype=float)
hot_r_ing = np.zeros((801), dtype=float)

file=pd.read_csv(ant+'/2021/X-pol/XH'+nm+'.csv', sep=',',skiprows=20,header=None)
file2=pd.read_csv( ant+'/2021/X-pol/XC'+nm+'.csv', sep=',',skiprows=20,header=None)
print (file.columns) #writes the simulated values in columns
freq_0= file.values[range(0, file.shape[0] - 1), 0].astype(float) / 1e9
hot_X_db = file.values[range(file.shape[0] - 1), 1].astype(float)
cold_X_db = file2.values[range(file.shape[0] - 1), 1].astype(float)
hot_X= 10 ** (hot_X_db/10)
cold_X= 10 ** (cold_X_db/10)

file=pd.read_csv(ant+'/2021/Y-pol/YC'+nm+'.csv', sep=',',skiprows=20,header=None)
file2=pd.read_csv(ant+'/2021/Y-pol/YH'+nm+'.csv', sep=',',skiprows=20,header=None)
print (file.columns) #writes the simulated values in columns
freq_0= file.values[range(0, file.shape[0] - 1), 0].astype(float) / 1e9
cold_Y_db = file.values[range(file.shape[0] - 1), 1].astype(float)
hot_Y_db = file2.values[range(file.shape[0] - 1), 1].astype(float)
hot_Y= 10 ** (hot_Y_db / 10)
cold_Y= 10 ** (cold_Y_db / 10)

Y_X = np.divide(hot_X, cold_X)
Y_Y = np.divide(hot_Y, cold_Y)
t_sys_X = np.divide((t_hot - t_cold * Y_X), (Y_X - 1))
t_sys_Y = np.divide((t_hot - t_cold * Y_Y), (Y_Y - 1))


cold_l_ing2 = np.zeros((801), dtype=float)
cold_r_ing2 = np.zeros((801), dtype=float)
hot_l_ing2 = np.zeros((801), dtype=float)
hot_r_ing2 = np.zeros((801), dtype=float)

file2=pd.read_csv(ant2+'/2021/X-pol/XH'+nm2+'.csv', sep=',',skiprows=20,header=None)
file22=pd.read_csv(ant2+'/2021/X-pol/XC'+nm2+'.csv', sep=',',skiprows=20,header=None)
print (file2.columns) #writes the simulated values in columns
freq_02= file2.values[range(0, file.shape[0] - 1), 0].astype(float) / 1e9
hot_X_db2 = file2.values[range(file.shape[0] - 1), 1].astype(float)
cold_X_db2 = file22.values[range(file.shape[0] - 1), 1].astype(float)
hot_X2= 10 ** (hot_X_db2/10)
cold_X2= 10 ** (cold_X_db2/10)

file2=pd.read_csv(ant2+'/2021/Y-pol/YC'+nm2+'.csv', sep=',',skiprows=20,header=None)
file22=pd.read_csv(ant2+'/2021/Y-pol/YH'+nm2+'.csv', sep=',',skiprows=20,header=None)
print (file2.columns) #writes the simulated values in columns
freq_02= file2.values[range(0, file.shape[0] - 1), 0].astype(float) / 1e9
cold_Y_db2 = file2.values[range(file.shape[0] - 1), 1].astype(float)
hot_Y_db2 = file22.values[range(file.shape[0] - 1), 1].astype(float)
hot_Y2= 10 ** (hot_Y_db2 / 10)
cold_Y2= 10 ** (cold_Y_db2 / 10)
Y_X2 = np.divide(hot_X2, cold_X2)
Y_Y2 = np.divide(hot_Y2, cold_Y2)
t_sys_X2 = np.divide((t_hot2 - t_cold2 * Y_X2), (Y_X2 - 1))
t_sys_Y2 = np.divide((t_hot2 - t_cold2 * Y_Y2), (Y_Y2 - 1))





plt.figure(1)
plt.subplot(211)
plt.title(ant+'\nY for X-pol and Y-pol')
plt.plot(freq_0,Y_X)
plt.plot(freq_02,Y_X2)
plt.xlim(0.1, 12)
plt.ylim(0, 16)
plt.ylabel('unit')
plt.grid(1)
plt.subplot(212)
plt.plot(freq_0,Y_Y)
plt.plot(freq_02,Y_Y2)
plt.xlim(0.1, 12)
plt.ylim(0, 16)
plt.ylabel('unit')
plt.xlabel('frequency in GHz')
plt.grid(1)
plt.savefig("Y-factor.png", bbox_inches="tight")


plt.figure(2)
plt.subplot(211)
plt.title(ant+'\n Hot/Cold for X-pol and Y-pol')
plt.plot(freq_0,cold_X_db)
plt.plot(freq_02,cold_X_db2)
plt.plot(freq_0,hot_X_db)
plt.plot(freq_02,hot_X_db2)
plt.xlim(0.1, 12)
plt.ylim(-70, -20)
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.subplot(212)
plt.plot(freq_0,cold_Y_db)
plt.plot(freq_02,cold_Y_db2)
plt.plot(freq_0,hot_Y_db)
plt.plot(freq_02,hot_Y_db2)
plt.xlim(0.1, 12)
plt.ylim(-70, -20)
plt.xlabel('frequency in GHz')
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.savefig("Spectra.png", bbox_inches="tight")


fig=plt.figure(4)
plt.subplot(211)
plt.title(ant+'\n System Temperature for X-pol and Y-pol')
plt.plot(freq_0,t_sys_X,label='1')
plt.plot(freq_02,t_sys_X2,label='2')
plt.ylim(-25,150)
plt.xlim(0.1, 12)
plt.yticks([-25,0,25,50,75,100,125,150],[-25,0,25,50,75,100,125,150])
plt.grid(1)
plt.ylabel('temperature in K')
plt.subplot(212)
plt.plot(freq_0,t_sys_Y,label=date1)
plt.plot(freq_02,t_sys_Y2,label=date2)
plt.ylim(-25,150)
plt.xlim(0.1, 12)
plt.yticks([-25,0,25,50,75,100,125,150],[-25,0,25,50,75,100,125,150])
plt.grid(1)
plt.xlabel('frequency in GHz')
plt.ylabel('temperature in K')
legend = plt.legend(loc='best', shadow=True)
plt.savefig("Tsys.png", bbox_inches="tight")
plt.show()

plt.close()

