# Generate latex text to include all the figures

channels = ["1A", "1B", "1C", "1D", "1E", "1F", "1G", "1H", "1J", "1K"
           "2A", "2B", "2C", "2D", "2E", "2F", "2G", "2H", "2J", "2K", "2M", "2N"
           "Ia", "IIa"]

polarizations = ["x", "y"]

outputs = ["3dB1", "6dB2", "6dB3"]

file = open("VNA_results_LateX.txt",'w')

for channel in channels:
    for polarization in polarizations:
        for output in outputs:
            name = f"{channel}{polarization}_{output}"
            try:
                file.write(f"% --- {name}--- \n")
                file.write("\\begin{figure}[H]\n")
                file.write("\\centering\n")
                file.write("\\includegraphics[width=0.9\\linewidth]{VNA_results/"+name+".png}\n")
                file.write("\\caption{Scattering matrix for channel "+channel+", polarization "+polarization+" and output "+output+".}\n")
                file.write("\\label{fig:"+name+"}\n")
                file.write("\\end{figure}\n\n\n")
            except:
                print(f"failed to print {name}")