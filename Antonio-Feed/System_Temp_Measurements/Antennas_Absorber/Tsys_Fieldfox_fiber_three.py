import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#=========================================================================================
#Input:

t_hot = 286
t_cold = 12
ant = '3C'
nm = '3'
date= '23/02/21 18:10'

t_hot2 = 286
t_cold2 = 12
ant2 = '3C'
nm2 = '5'
date2= '24/02/21 13:35'

t_hot3 = 280
t_cold3 = 12
ant3 = '3C'
nm3 = '7'
date3= '25/02/21 09:30'

#=========================================================================================






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

#=========================================================================================
#measurement 2

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

#=========================================================================================
#measurement 3



cold_l_ing3 = np.zeros((801), dtype=float)
cold_r_ing3 = np.zeros((801), dtype=float)
hot_l_ing3 = np.zeros((801), dtype=float)
hot_r_ing3 = np.zeros((801), dtype=float)

file3=pd.read_csv(ant3+'/2021/X-pol/XH'+nm3+'.csv', sep=',',skiprows=20,header=None)
file33=pd.read_csv(ant3+'/2021/X-pol/XC'+nm3+'.csv', sep=',',skiprows=20,header=None)
print (file3.columns) #writes the simulated values in columns
freq_03= file3.values[range(0, file.shape[0] - 1), 0].astype(float) / 1e9
hot_X_db3 = file3.values[range(file.shape[0] - 1), 1].astype(float)
cold_X_db3 = file33.values[range(file.shape[0] - 1), 1].astype(float)
hot_X3= 10 ** (hot_X_db3/10)
cold_X3= 10 ** (cold_X_db3/10)

file3=pd.read_csv(ant3+'/2021/Y-pol/YC'+nm3+'.csv', sep=',',skiprows=20,header=None)
file33=pd.read_csv(ant3+'/2021/Y-pol/YH'+nm3+'.csv', sep=',',skiprows=20,header=None)
print (file2.columns) #writes the simulated values in columns
freq_03= file3.values[range(0, file.shape[0] - 1), 0].astype(float) / 1e9
cold_Y_db3 = file3.values[range(file.shape[0] - 1), 1].astype(float)
hot_Y_db3 = file33.values[range(file.shape[0] - 1), 1].astype(float)
hot_Y3= 10 ** (hot_Y_db3 / 10)
cold_Y3= 10 ** (cold_Y_db3 / 10)
Y_X3 = np.divide(hot_X3, cold_X3)
Y_Y3 = np.divide(hot_Y3, cold_Y3)
t_sys_X3 = np.divide((t_hot3 - t_cold3 * Y_X3), (Y_X3 - 1))
t_sys_Y3 = np.divide((t_hot3 - t_cold3 * Y_Y3), (Y_Y3 - 1))





plt.figure(1)
plt.subplot(211)
plt.title(ant+'\nY for X-pol and Y-pol')
plt.plot(freq_0,Y_X)
plt.plot(freq_02,Y_X2)
plt.plot(freq_03,Y_X3)
plt.xlim(0.1, 12)
plt.ylim(0, 16)
plt.ylabel('unit')
plt.grid(1)
plt.subplot(212)
plt.plot(freq_0,Y_Y)
plt.plot(freq_02,Y_Y2)
plt.plot(freq_03,Y_Y3)
plt.xlim(0.1, 12)
plt.ylim(0, 15)
plt.ylabel('unit')
plt.xlabel('frequency in GHz')
plt.grid(1)
plt.savefig("Y-factor3.png", bbox_inches="tight")


plt.figure(2)
plt.subplot(211)
plt.title(ant+'\n Cold for X-pol and Y-pol')
plt.plot(freq_0,cold_X_db)
plt.plot(freq_02,cold_X_db2)
plt.plot(freq_03,cold_X_db3)
plt.plot(freq_0,hot_X_db)
plt.plot(freq_02,hot_X_db2)
plt.plot(freq_03,hot_X_db3)
plt.xlim(0.1, 12)
plt.ylim(-70, -20)
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.subplot(212)
plt.plot(freq_0,cold_Y_db)
plt.plot(freq_02,cold_Y_db2)
plt.plot(freq_03,cold_Y_db3)
plt.plot(freq_0,hot_Y_db)
plt.plot(freq_02,hot_Y_db2)
plt.plot(freq_03,hot_Y_db3)
plt.xlim(0.1, 12)
plt.ylim(-70, -20)
plt.xlabel('frequency in GHz')
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.savefig("Spec3.png", bbox_inches="tight")


fig=plt.figure(4)
plt.subplot(211)
plt.title(ant+'\n System Temperature for X-pol and Y-pol')
plt.plot(freq_0,t_sys_X)
plt.plot(freq_02,t_sys_X2)
plt.plot(freq_03,t_sys_X3)
plt.ylim(-25,150)
plt.xlim(0.1, 12)
plt.yticks([-25,0,25,50,75,100,125,150],[-25,0,25,50,75,100,125,150])
plt.grid(1)
plt.ylabel('temperature in K')
plt.subplot(212)
plt.plot(freq_0,t_sys_Y,label=date)
plt.plot(freq_02,t_sys_Y2,label=date2)
plt.plot(freq_03,t_sys_Y3,label=date3)
plt.ylim(-25,150)
plt.xlim(0.1, 12)
plt.yticks([-25,0,25,50,75,100,125,150],[-25,0,25,50,75,100,125,150])
plt.grid(1)
plt.xlabel('frequency in GHz')
plt.ylabel('temperature in K')
legend = plt.legend(loc='best', shadow=True)
plt.savefig("Tsys3.png", bbox_inches="tight")
plt.show()

plt.close()

