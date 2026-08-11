import os
import plot_sparams

files = os.listdir('./cti')

for f in files:
    plot_sparams.plot_sparam(f,'./cti/')
