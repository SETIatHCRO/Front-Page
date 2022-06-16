import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

t_hot = 286
t_cold = 12
ant = '3c'
nm = '1'


Enable=False
a0=8.986
a1=0.5229
a2=-0.07776
a3=0.005763
a4=-0.0001203
T408=11.98
Beta=-2.682



cold_l_ing = np.zeros((801), dtype=float)
cold_r_ing = np.zeros((801), dtype=float)
hot_l_ing = np.zeros((801), dtype=float)
hot_r_ing = np.zeros((801), dtype=float)
t_cold_ing = np.full((801),t_cold, dtype=float)
t_sys_X = np.zeros((801), dtype=float)
t_sys_Y = np.zeros((801), dtype=float)


file=pd.read_csv(ant+'/2021/X-pol/XH'+nm+'.csv', sep=',',skiprows=16,header=None)
file2=pd.read_csv( ant+'/2021/X-pol/XC'+nm+'.csv', sep=',',skiprows=16,header=None)
print (file.columns) #writes the simulated values in columns
freq_0= file.values[range(0, file.shape[0] - 1), 0].astype(float) / 1e9
hot_X_db = file.values[range(file.shape[0] - 1), 1].astype(float)
cold_X_db = file2.values[range(file.shape[0] - 1), 1].astype(float)


hot_X= 10 ** (hot_X_db/10)
cold_X= 10 ** (cold_X_db/10)
if Enable:
    for x in range(801):
        t_cold_ing[x]= a0 + a1*freq_0[x] + a2*pow(freq_0[x],2)  + a3*pow(freq_0[x],3) + a4*pow(freq_0[x],4) + T408*pow(freq_0[x]/0.408,Beta)



file=pd.read_csv(ant+'/2021/Y-pol/YC'+nm+'.csv', sep=',',skiprows=16,header=None)
file2=pd.read_csv(ant+'/2021/Y-pol/YH'+nm+'.csv', sep=',',skiprows=16,header=None)
print (file.columns) #writes the simulated values in columns
freq_0= file.values[range(0, file.shape[0] - 1), 0].astype(float) / 1e9
cold_Y_db = file.values[range(file.shape[0] - 1), 1].astype(float)
hot_Y_db = file2.values[range(file.shape[0] - 1), 1].astype(float)


hot_Y= 10 ** (hot_Y_db / 10)
cold_Y= 10 ** (cold_Y_db / 10)



Y_X = np.divide(hot_X, cold_X)
Y_Y = np.divide(hot_Y, cold_Y)


plt.figure(10)
plt.title(ant+'\nSky Temp')
plt.plot(freq_0,t_cold_ing)
plt.xlim(0.1, 12)
plt.ylim(0,25)
plt.ylabel('Kelvin')
plt.xlabel('frequency in GHz')
plt.grid(1)
plt.savefig("Sky-Temp.pdf", bbox_inches="tight")



plt.figure(1)
plt.subplot(211)
plt.title(ant+'\nY for X-pol')
plt.plot(freq_0,Y_X)
plt.xlim(0.1, 12)
plt.ylim(0, 16)
plt.ylabel('unit')
plt.grid(1)
plt.subplot(212)
plt.title('Y for Y-pol')
plt.plot(freq_0,Y_Y)
plt.xlim(0.1, 16)
plt.ylim(0, 12)
plt.ylabel('unit')
plt.xlabel('frequency in GHz')
plt.grid(1)
plt.savefig("Y-factor.pdf", bbox_inches="tight")


plt.figure(2)
plt.subplot(211)
plt.title(ant+'\n Cold for X-pol')
plt.plot(freq_0,cold_X_db)
plt.xlim(0.1, 12)
plt.ylim(-70, -20)
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.subplot(212)
plt.title('Hot for X-pol')
plt.plot(freq_0,hot_X_db)
plt.xlim(0.1, 12)
plt.ylim(-70, -20)
plt.xlabel('frequency in GHz')
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.savefig("SpecX.pdf", bbox_inches="tight")

plt.figure(3)
plt.subplot(211)
plt.title(ant+' \nCold for Y-pol')
plt.plot(freq_0,cold_Y_db)
plt.xlim(0.1, 12)
plt.ylim(-70, -20)
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.subplot(212)
plt.title('Hot for Y-pol')
plt.plot(freq_0,hot_Y_db)
plt.xlim(0.1, 12)
plt.ylim(-70, -20)
plt.xlabel('frequency in GHz')
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.savefig("SpecY.pdf", bbox_inches="tight")



for x in range (801):
    t_sys_X[x] = np.divide((t_hot - t_cold_ing[x] * Y_X[x]), (Y_X[x] - 1))
    t_sys_Y[x] = np.divide((t_hot - t_cold_ing[x] * Y_Y[x]), (Y_Y[x] - 1))






fig=plt.figure(4)
plt.subplot(211)
plt.title(ant+'\n System Temperature for X-pol (UP) and Y-pol (DOWN)')
plt.plot(freq_0,t_sys_X)
plt.ylim(-50,150)
plt.xlim(0.1, 12)
plt.yticks([-50,-25,0,25,50,75,100,125,150],[-50,-25,0,25,50,75,100,125,150])
#plt.xticks([0,100,200,300,400,500,600,700,801],[0,1.5,3,4.5,6,7.5,9,10.5,12])
plt.grid(1)
#plt.xlabel('frequency in GHz')
plt.ylabel('temperature in K')

plt.subplot(212)
#plt.title('System Temperature for Y-pol')
plt.plot(freq_0,t_sys_Y)
plt.ylim(-50,150)
plt.xlim(0.1, 12)
plt.yticks([-50,-25,0,25,50,75,100,125,150],[-50,-25,0,25,50,75,100,125,150])
#plt.xticks([0,100,200,300,400,500,600,700,801],[0,1.5,3,4.5,6,7.5,9,10.5,12])
plt.grid(1)
plt.xlabel('frequency in GHz')
plt.ylabel('temperature in K')
plt.savefig("Tsys.png")#, bbox_inches="tight"
plt.show()

plt.close()

