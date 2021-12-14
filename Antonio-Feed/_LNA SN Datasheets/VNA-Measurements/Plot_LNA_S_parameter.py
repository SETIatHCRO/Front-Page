import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
filename = 'SN0002A/0002A.cti'



file=pd.read_table(filename, sep='/n',skiprows=5,header=None)

samples = int (re.findall(r'-?\d+\.?\d*', file.values[0][0])[0])


freq = np.zeros((samples), dtype=float)
S11 = np.zeros((samples), dtype=complex)
S21 = np.zeros((samples), dtype=complex)
S12 = np.zeros((samples), dtype=complex)
S22 = np.zeros((samples), dtype=complex)

freq = file.values[6:(samples+6),0].astype(np.float)


x=0
for s in range ((8+samples),(8+samples*2)):
    S11[x]= np.complex( float( (re.findall(r'-?\d+\.?\d*', file.values[s][0])[0])) , float( (re.findall(r'-?\d+\.?\d*', file.values[s][0])[1])) )
    x=x+1

x=0
for s in range ((10+samples*2),(10+samples*3)):
    S21[x]= np.complex( float( (re.findall(r'-?\d+\.?\d*', file.values[s][0])[0])) , float( (re.findall(r'-?\d+\.?\d*', file.values[s][0])[1])) )
    x=x+1

x=0
for s in range ((12+samples*3),(12+samples*4)):
    S12[x]= np.complex( float( (re.findall(r'-?\d+\.?\d*', file.values[s][0])[0])) , float( (re.findall(r'-?\d+\.?\d*', file.values[s][0])[1])) )
    x=x+1

x=0
for s in range ((14+samples*4),(14+samples*5)):
    S22[x]= np.complex( float( (re.findall(r'-?\d+\.?\d*', file.values[s][0])[0])) , float( (re.findall(r'-?\d+\.?\d*', file.values[s][0])[1])) )
    x=x+1









plt.figure(1)
plt.title('Y for Y-pol')
plt.plot(freq/10**9,20*np.log10(np.absolute(S21)))
plt.ylim(-40, 0)
plt.xlim(0, 20)
plt.ylabel('dB')
plt.xlabel('frequency in GHz')
plt.grid(1)
#plt.savefig("S21.png", bbox_inches="tight")
plt.show()



plt.close()

