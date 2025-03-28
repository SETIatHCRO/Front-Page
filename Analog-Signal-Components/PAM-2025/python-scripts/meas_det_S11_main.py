import measPAM_import_cti, measPAM_plot

def main():
    '''This function plots the measured S11 parameter of one detector module measurement with the VNA.
     The measured file must be a cti-file!
     The python files "measPAM_import_cti" and "measPAM_plot" must be in the same folder as "meas_det_S11_main"!
    '''

    filepath = 'data_detetector/S11.cti' #substitute with filepath of your measurement; folders must be seperated with a forward slash
    f, s11, s21, s12, s22 = measPAM_import_cti.cti_import(filepath)
    labels = ['S11']
    data_meas = [[labels, f, s11]]
    measPAM_plot.plot(data_meas, ymax=30, ymin=-50) #adjust limits of y axis (ymax, ymin) if needed

if __name__ == '__main__':
    main()