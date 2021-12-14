import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
filename1 = '0013A'
filename2 = '0030A'

## Code for file1
file1=pd.read_table("SN"+filename1+"/"+filename1+".cti", sep='/n',skiprows=5,header=None)

samples1 = int (re.findall(r'-?\d+\.?\d*', file1.values[0][0])[0])

freq1 = np.zeros((samples1), dtype=float)
file1_S11 = np.zeros((samples1), dtype=complex)
file1_S21 = np.zeros((samples1), dtype=complex)
file1_S12 = np.zeros((samples1), dtype=complex)
file1_S22 = np.zeros((samples1), dtype=complex)

freq1 = file1.values[6:(samples1 + 6), 0].astype(np.float)
x=0
for s in range ((8 + samples1), (8 + samples1 * 2)):
    file1_S11[x]= np.complex( float( (re.findall(r'-?\d+\.?\d*', file1.values[s][0])[0])) , float( (re.findall(r'-?\d+\.?\d*', file1.values[s][0])[1])) )
    x=x+1
x=0
for s in range ((10 + samples1 * 2), (10 + samples1 * 3)):
    file1_S21[x]= np.complex( float( (re.findall(r'-?\d+\.?\d*', file1.values[s][0])[0])) , float( (re.findall(r'-?\d+\.?\d*', file1.values[s][0])[1])) )
    x=x+1
x=0
for s in range ((12 + samples1 * 3), (12 + samples1 * 4)):
    file1_S12[x]= np.complex( float( (re.findall(r'-?\d+\.?\d*', file1.values[s][0])[0])) , float( (re.findall(r'-?\d+\.?\d*', file1.values[s][0])[1])) )
    x=x+1
x=0
for s in range ((14 + samples1 * 4), (14 + samples1 * 5)):
    file1_S22[x]= np.complex( float( (re.findall(r'-?\d+\.?\d*', file1.values[s][0])[0])) , float( (re.findall(r'-?\d+\.?\d*', file1.values[s][0])[1])) )
    x=x+1

## Code for file2
file2=pd.read_table("SN"+filename2+"/"+filename2+".cti", sep='/n',skiprows=5,header=None)

samples2 = int (re.findall(r'-?\d+\.?\d*', file2.values[0][0])[0])

freq2 = np.zeros((samples2), dtype=float)
file2_S11 = np.zeros((samples2), dtype=complex)
file2_S21 = np.zeros((samples2), dtype=complex)
file2_S12 = np.zeros((samples2), dtype=complex)
file2_S22 = np.zeros((samples2), dtype=complex)

freq2 = file2.values[6:(samples2 + 6), 0].astype(np.float)
x=0
for s in range ((8 + samples2), (8 + samples2 * 2)):
    file2_S11[x]= np.complex( float( (re.findall(r'-?\d+\.?\d*', file2.values[s][0])[0])) , float( (re.findall(r'-?\d+\.?\d*', file2.values[s][0])[1])) )
    x=x+1
x=0
for s in range ((10 + samples2 * 2), (10 + samples2 * 3)):
    file2_S21[x]= np.complex( float( (re.findall(r'-?\d+\.?\d*', file2.values[s][0])[0])) , float( (re.findall(r'-?\d+\.?\d*', file2.values[s][0])[1])) )
    x=x+1
x=0
for s in range ((12 + samples2 * 3), (12 + samples2 * 4)):
    file2_S12[x]= np.complex( float( (re.findall(r'-?\d+\.?\d*', file2.values[s][0])[0])) , float( (re.findall(r'-?\d+\.?\d*', file2.values[s][0])[1])) )
    x=x+1
x=0
for s in range ((14 + samples2 * 4), (14 + samples2 * 5)):
    file2_S22[x]= np.complex( float( (re.findall(r'-?\d+\.?\d*', file2.values[s][0])[0])) , float( (re.findall(r'-?\d+\.?\d*', file2.values[s][0])[1])) )
    x=x+1







plt.figure(1)
plt.title('LNA S21')
plt.plot(freq1/10**9,20*np.log10(np.absolute(file1_S21)), label=filename1)
plt.plot(freq2/10**9,20*np.log10(np.absolute(file2_S21)), label=filename2)
plt.ylim(-40, 10)
plt.xlim(0, 20)
plt.ylabel('dB')
plt.xlabel('frequency in GHz')
plt.grid(1)
plt.legend(loc="upper right")
plt.savefig("Spare-S21.png", bbox_inches="tight")
plt.show()



plt.close()

