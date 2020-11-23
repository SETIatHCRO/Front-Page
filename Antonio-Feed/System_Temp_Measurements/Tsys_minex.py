import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

t_hot = 292
t_cold = 77.6
cold_l_ing = np.zeros((801), dtype=float)
cold_r_ing = np.zeros((801), dtype=float)
hot_l_ing = np.zeros((801), dtype=float)
hot_r_ing = np.zeros((801), dtype=float)





file=pd.read_csv('018/ATA_Feed/Feed_018_X_pole_ypam1010_Noise.csv', sep=',')
print file.columns #writes the simulated values in columns
freq_0= file['Freq'].values/1e9
hot_X_db = file['Trace1'].values
cold_X_db = file['Trace2'].values

hot_X= 10 ** (hot_X_db/10)
cold_X= 10 ** (cold_X_db/10)




file=pd.read_csv('018/ATA_Feed/Feed_018_Y_pole_ypam1010_Noise.csv', sep=',')
print file.columns #writes the simulated values in columns
freq_0= file['Freq'].values/1e9
hot_Y_db = file['Trace1'].values
cold_Y_db = file['Trace2'].values

hot_Y= 10 ** (hot_Y_db / 10)
cold_Y= 10 ** (cold_Y_db / 10)




Y_X = np.divide(hot_X, cold_X)
Y_Y = np.divide(hot_Y, cold_Y)


plt.figure(1)
plt.subplot(211)
plt.title('Feed 018 \nY for X-pol')
plt.plot(Y_X)
plt.xlim(0, 801)
plt.xticks([0,100,200,300,400,500,600,700,801],[0,1.5,3,4.5,6,7.5,9,10.5,12])
plt.grid(1)
plt.subplot(212)
plt.title('Y for Y-pol')
plt.plot(Y_Y)
plt.xlim(0, 801)
plt.xticks([0,100,200,300,400,500,600,700,801],[0,1.5,3,4.5,6,7.5,9,10.5,12])
plt.xlabel('frequency in GHz')
plt.grid(1)
plt.savefig("Y-factor.png")

plt.figure(2)
plt.subplot(211)
plt.title('Feed 018 \nCold for X-pol')
plt.plot(cold_X_db)
plt.xlim(0, 801)
plt.xticks([0,100,200,300,400,500,600,700,801],[0,1.5,3,4.5,6,7.5,9,10.5,12])
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.subplot(212)
plt.title('Hot for X-pol')
plt.plot(hot_X_db)
plt.xlim(0, 801)
plt.xticks([0,100,200,300,400,500,600,700,801],[0,1.5,3,4.5,6,7.5,9,10.5,12])
plt.xlabel('frequency in GHz')
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.savefig("SpecX.png")

plt.figure(3)
plt.subplot(211)
plt.title('Feed 018 \nCold for Y-pol')
plt.plot(cold_Y_db)
plt.xlim(0, 801)
plt.xticks([0,100,200,300,400,500,600,700,801],[0,1.5,3,4.5,6,7.5,9,10.5,12])
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.subplot(212)
plt.title('Hot for Y-pol')
plt.plot(hot_Y_db)
plt.xlim(0, 801)
plt.xticks([0,100,200,300,400,500,600,700,801],[0,1.5,3,4.5,6,7.5,9,10.5,12])
plt.xlabel('frequency in GHz')
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.savefig("SpecY.png")

t_sys_X = np.divide((t_hot - t_cold * Y_X), (Y_X - 1))
t_sys_Y = np.divide((t_hot - t_cold * Y_Y), (Y_Y - 1))

fig=plt.figure(4)
plt.subplot(211)
plt.title('Feed 018 \nSystem Temperature for X-pol')
plt.plot(t_sys_X)
plt.ylim(-100,200)
plt.xlim(0, 801)
plt.xticks([0,100,200,300,400,500,600,700,801],[0,1.5,3,4.5,6,7.5,9,10.5,12])
plt.grid(1)
#plt.xlabel('frequency in GHz')
plt.ylabel('temperature in K')

plt.subplot(212)
plt.title('System Temperature for Y-pol')
plt.plot(t_sys_Y)
plt.ylim(-100,200)
plt.xlim(0, 801)
plt.xticks([0,100,200,300,400,500,600,700,801],[0,1.5,3,4.5,6,7.5,9,10.5,12])
plt.grid(1)
plt.xlabel('frequency in GHz')
plt.ylabel('temperature in K')
plt.savefig("Tsys.png")
plt.show()

plt.close()

