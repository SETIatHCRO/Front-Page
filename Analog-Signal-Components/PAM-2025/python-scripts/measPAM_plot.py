import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def plot(data, color=False, log=False, ymin=-80, ymax=10, ystep=10, xmin=0, xmax=20, xstep=2, xlabel="f [GHz]", ylabel="Mag [dB]"):
    '''
    plots data with matplotlib;
    
    expected input:
    * if color is "False" (default):
        data = list, consisting of any amount of inner lists; each inner list must contain:
                * element[0]: list of labels
                * element[1]: list of x-values
                * element[2:]: any amount of lists with y-values
    * if color is "True":
        data = list, consisting of any amount of inner lists; each inner list must contain:
                * element[0]: list of labels
                * element[1]: list of colors for plot
                * element[2]: list of x-values
                * element[3:]: any amount of lists with y-values
    * if log is "False" (default):
        x- and y-axis are linear
    * if log is "True":
        y-axis is plottet in logarithmic scale, x-axis remains linear
    * ymin (default = -80): minimum value y-axis
    * ymax (default = 10): maximum value y-axis
    * ystep (default = 10): stepsize between y-axis ticks
    * xmin (default = 0): minimum value of x-axis
    * xmax (default = 21): maximum value of y-axis
    * xstep (default = 2): stepsize between x-axis ticks
    * xlabel (default = "f [GHz]"): label of x-axis
    * ylabel (default = "Mag [dB]): label of y-axis
    '''

    #setup figuresize axis and grid

    if log==False:
        plt.figure(figsize=(10, 6))
        plt.yticks(np.arange(ymin,ymax+1,ystep), fontsize = 15)

    elif log==True:
        plt.figure(figsize=(7.5, 4.5)) #7.5, 6
        plt.yticks(np.arange(ymin,ymax+1), fontsize = 15)
        plt.yscale("log")
        plt.grid(which="minor", color="0.9")

    else:
        raise Exception('ERROR: argument "log" must be a boolean')

    plt.grid(True)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    ax = plt.gca()
    #ax.ticklabel_format(style='plain', axis='x') #not needed
    ax.set_xlim([0,20])
    ax.set_ylim([ymin,ymax])
    plt.xticks(np.arange(xmin,xmax+1,xstep), fontsize = 15)
    
    #plot data

    if color == False:
        # data structure = [ [[lables1,...],[x1,...],[y11,...],[y12,...]] , [[lables2,...][x2,...],[y21,...],[y22,...]] ]
        for i in data:
            for s in range (len(i)-2):
                plt.plot(i[1],i[s+2],label=i[0][s])
    elif color == True:
        # data structure with color = [ [[lables1,...], [color11, color12], [x1,...],[y11,...],[y12,...]] , [[lables2,...], [color11, color12], [x2,...],[y21,...],[y22,...]] ]
        for i in data:
            for s in range (len(i)-3):
                plt.plot(i[2],i[s+3],label=i[0][s],color=i[1][s])
    else:
        raise Exception('ERROR: argument "color" must be a boolean')

    #plot ledgend and show plot

    plt.legend(fontsize=14)
    plt.show()