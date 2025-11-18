import measPAM_import_cti, measPAM_plot

def main():
    ''' This function plots the measured S11, S21 and S22 parameter of one amplifier module measurement with the VNA.
    The measured file must be a cti-file!
    The python files "measPAM_import_cti" and "measPAM_plot" must be in the same folder as "meas_amp_main"!
    '''

    filepath = 'data_amplifier/amplifier_v1/amp1.cti' #substitute with filepath of your measurement; folders must be seperated with a forward slash
    f, s11, s21, s12, s22 = measPAM_import_cti.cti_import(filepath)
    labels = ['S11', 'S21', 'S22']
    colors = ['C0', 'C1', 'C3']
    data_meas = [[labels, colors, f, s11, s21, s22]]
    measPAM_plot.plot(data_meas, color=True, ymax=30, ymin=-50) #adjust limits of y axis (ymax, ymin) if needed

if __name__ == '__main__':
    main()