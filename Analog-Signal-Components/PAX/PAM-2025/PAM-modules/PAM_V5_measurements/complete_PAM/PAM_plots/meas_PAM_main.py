import measPAM_import_cti, measPAM_plot

def main():
    '''This function plots the measured S11, S21 and S22 parameter of one PAM module measurement with the VNA.
     The measured file must be a cti-file!
     The python files "measPAM_import_cti" and "measPAM_plot" must be in the same folder as "meas_att_main"!
    '''
    
    #plot S11, S21, S22 for same attenuation level
    filepath_011111 = 'data_PAM\PAM_011111.cti' #substitute with filepath of your measurement; folders must be seperated with a forward slash
    f_011111, s11_011111, s21_011111, s12_011111, s22_011111 = measPAM_import_cti.cti_import(filepath_011111)
    labels = ['S11', 'S21', 'S22']
    colors = ['C0', 'C1', 'C3']
    data_meas1 = [[labels, colors, f_011111, s11_011111, s21_011111, s22_011111]]
    measPAM_plot.plot(data_meas1, color=True, ymax=40, ymin=-50) #adjust limits of y axis (ymax, ymin) if needed

    #plot S21 for different attenuation levels
    filepath_001111 = 'data_PAM/PAM_001111.cti' #substitute with filepath of your measurement; folders must be seperated with a forward slash
    filepath_000111 = 'data_PAM\PAM_000111.cti'
    filepath_000011 = 'data_PAM\PAM_000011.cti'
    filepath_000001 = 'data_PAM\PAM_000001.cti'
    filepath_000000 = 'data_PAM\PAM_000000.cti'
    f_001111, s11_001111, s21_001111, s12_001111, s22_001111 = measPAM_import_cti.cti_import(filepath_001111)
    f_000111, s11_000111, s21_000111, s12_000111, s22_000111 = measPAM_import_cti.cti_import(filepath_000111)
    f_000011, s11_000011, s21_000011, s12_000011, s22_000011 = measPAM_import_cti.cti_import(filepath_000011)
    f_000001, s11_000001, s21_000001, s12_000001, s22_000001 = measPAM_import_cti.cti_import(filepath_000001)
    f_000000, s11_000000, s21_000000, s12_000000, s22_000000 = measPAM_import_cti.cti_import(filepath_000000)
    label_011111 = ['S21_011111']
    label_001111 = ['S21_001111']
    label_000111 = ['S21_000111']
    label_000011 = ['S21_000011']
    label_000001 = ['S21_000001']
    label_000000 = ['S21_000000']
    data_meas2 = [[label_011111, f_011111, s21_011111],
                 [label_001111, f_001111, s21_001111],
                 [label_000111, f_000111, s21_000111],
                 [label_000011, f_000011, s21_000011],
                 [label_000001, f_000001, s21_000001],
                 [label_000000, f_000000, s21_000000]]
    measPAM_plot.plot(data_meas2, ymax=70, ymin=-20) #adjust limits of y axis (ymax, ymin) if needed

if __name__ == '__main__':
    main()