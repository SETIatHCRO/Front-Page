import measPAM_import_csv, measPAM_plot

def main():
    '''This function plots the measured output voltage vs input power of one detector module measurement.
     The measured file must be a csv-file with the following format:
        1. Column headers separated by colDeli
        2. Then any number of rows with the actual measured values, also separated by colDeli
     The python files "measPAM_import_csv" and "measPAM_plot" must be in the same folder as "meas_det_power_main"!
    '''
    
    filepath_det_2GHz = "data_detetector/det_power_meas_1GHz.CSV" #substitute with filepath of your measurement; folders must be seperated with a forward slash
    titles_2GHz, amp_2GHz, V_2GHz = measPAM_import_csv.importSingleSeriesFromCsvFile(filepath_det_2GHz,",")
    label_2GHz = ['2GHz']
    xlabel = 'P_in [dBm]'
    ylabel = 'output voltage [V]'
    data_det_power = [[label_2GHz, amp_2GHz, V_2GHz]]
    measPAM_plot.plot(data_det_power, log=True, ymin=0.01, ymax=10, xmin=-40, xmax=20, xstep=5, xlabel=xlabel, ylabel=ylabel)

if __name__ == '__main__':
    main()