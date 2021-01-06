import sys
import serial
import msvcrt
import time
import datetime
from random import randint

com_port = None
ports = ['COM5', 'COM4', 'COM3', 'COM2', 'COM1']

done = False

term_io_func_ptr = None

command = ''

pathname = None

status_line_num = 0

AUTO_STATUS_PERIOD = 3  # minutes

next_status_min = 0

header_one    = '        Vac   ----Vac Drv---- ---Temp TC7x--- ------Cryo----- Diode ---Fan--'
header_two    = ' Time  Guage  p316  p398 p346  A0  A1  A2  A3  TC Max Min Cur  (V)  PWM  RPM'
#                HH:MM 0.0e-00  000 00000  000 000 000 000 000 000 000|000|000 0.000 000 0000

def open_com_port():
    for port in ports:
        try:
            print ('open {0:s} ... '.format(port)),
            com_port = serial.Serial(port, 19200, timeout=0.1)
            print ('O.K.')
            return (com_port) 
        except Exception:  
            print ('fail')

    return (None)

def com_port_recv_char():
    return (com_port.read(1))    

def com_port_recv_line():
    line = ""

    timeout_count = 0

    while True:
        recv_char = com_port_recv_char()
        if (len(recv_char) == 0):
            timeout_count = timeout_count + 1
            if (not(timeout_count < 3)):
                break
            continue
        if (ord(recv_char) == 0x0d):
            break
        if ((ord(recv_char) >= 0x20) and (ord(recv_char) <= 0x7e)):
            line = line + recv_char
            timeout_count = 0

    return (line)

def feed_status():
    global status_line_num
    global next_status_min

    if (not(status_line_num < 10)):
        status_line_num = 0

    if (len(command) > 0):
        sys.stdout.write('\r\n')
        sys.stdout.flush()       

    if (status_line_num == 0):
        sys.stdout.write(header_one)
        sys.stdout.write('\r\n')
        sys.stdout.write(header_two)
        sys.stdout.write('\r\n')
        sys.stdout.flush()

    get_and_print_status()

    next_status_min = (get_minute() + AUTO_STATUS_PERIOD) % 60

    status_line_num = status_line_num + 1    

def main():
    global com_port
    global next_status_min 
    global pathname
    global command

    com_port = open_com_port()
    if (not(com_port)):
        sys.exit()

    dt = datetime.datetime.now()
    filename = dt.strftime('%Y-%m-%d-%H-%M-%S-antonio-feed-status.log')
    pathname = 'logs' + '\\' + filename

    print ('Feed status automatically taken every {0:d} minutes.'.format(AUTO_STATUS_PERIOD))
    print ('Press ? to request and display feed status on demand.')
    print ('Status logged to {0:s}'.format(filename))

    f = open(pathname, 'at')
    f.write(header_one + '\n')
    f.write(header_two + '\n')
    f.close()

    term_io_func_ptr = term_io_handle_keycode

    com_port.write(chr(0x0d))
    time.sleep(0.2)
    com_port.write('minex')
    com_port.write(chr(0x0d))

    next_status_min = (get_minute() + AUTO_STATUS_PERIOD) % 60

    while (not(done)): 
        if (msvcrt.kbhit()):
            keycode = ord(msvcrt.getch())
            term_io_func_ptr(keycode)
        recv_data = com_port_recv_char()
        if (len(recv_data) > 0):
            sys.stdout.write(recv_data)        
            sys.stdout.flush()
        if (get_minute() == next_status_min):
            next_status_min = (next_status_min + AUTO_STATUS_PERIOD) % 60 
            feed_status()
            command = ''
            
    com_port.close()

def get_minute():
    dt = datetime.datetime.now()
    return (dt.minute)

def term_io_handle_keycode(keycode):
    global term_io_func_ptr
    global command

    if (keycode == 0x00):
        term_io_func_ptr = term_io_handle_extended_00_keycode
        return

    if (keycode == 0xe0):
        term_io_func_ptr = term_io_handle_extended_0e_keycode
        return

    if (keycode == 0x08):
        term_io_backspace()
        return

    if (keycode == 0x3f):
        term_io_get_status()
        return

    if ((keycode >= 0x20) and (keycode <= 0x7e)):
        command = command + chr(keycode)
        com_port.write(chr(keycode))
        return

    if (keycode == 0x0d):
        term_io_cr()
        return

def term_io_handle_extended_00_keycode(keycode):
    global term_io_func_ptr

    term_io_func_ptr = term_io_handle_keycode

def term_io_handle_extended_0e_keycode(keycode):
    global term_io_func_ptr

    term_io_func_ptr = term_io_handle_keycode

def term_io_backspace():
    global command

    if (len(command) > 0):
        command = command[0:-1]

    com_port.write(chr(0x08))

def term_io_get_status():
    global command

    feed_status()

    command = ''

def term_io_cr():
    global command
    global status_line_num
    global done

    com_port.write(chr(0x0d))

    command = command.strip()
    print (command)
    if ((command.lower() == 'quit') or (command.lower() == 'exit')):
        done = True
        return 

    status_line_num = 0

    command = ''

def get_and_print_status():
    while (len(com_port_recv_char()) == 1):
        continue

    f = open(pathname, 'at')

    dt = datetime.datetime.now()
    date_str = '{0:5.5s}'.format(dt.strftime('%H:%M'))
    sys.stdout.write(date_str)
    f.write(date_str)

    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')

    vacuum_str = '{0:>7.7s}'.format(get_vacuum())
    sys.stdout.write(vacuum_str)
    f.write(vacuum_str)
        
    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')
    time.sleep(0.1)    

    p316_str = '{0:>4.4s}'.format(get_vac_p316())
    sys.stdout.write(p316_str)
    f.write(p316_str)
        
    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')
    time.sleep(0.1)    
        
    p398_str = '{0:>5.5s}'.format(get_vac_p398())
    sys.stdout.write(p398_str)
    f.write(p398_str)        

    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')
    time.sleep(0.1)    
        
    p346_str = '{0:>4.4s}'.format(get_vac_p346())
    sys.stdout.write(p346_str)
    f.write(p346_str)        

    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')
    time.sleep(0.1)    
        
    temp_a0_str = '{0:>3.3s}'.format(get_temp('A0'))
    sys.stdout.write(temp_a0_str)
    f.write(temp_a0_str)
        
    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')
    time.sleep(0.1)    
        
    temp_a1_str = '{0:>3.3s}'.format(get_temp('A1'))
    sys.stdout.write(temp_a1_str)
    f.write(temp_a1_str)
        
    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')
    time.sleep(0.1)    
        
    temp_a2_str = '{0:>3.3s}'.format(get_temp('A2'))
    sys.stdout.write(temp_a2_str)
    f.write(temp_a2_str)
        
    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')
    time.sleep(0.1)    
        
    temp_a3_str = '{0:>3.3s}'.format(get_temp('A3'))
    sys.stdout.write(temp_a3_str)
    f.write(temp_a3_str)
        
    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')
    time.sleep(0.1)    

    tc_str = '{0:>3.3s}'.format(get_tc()) 
    sys.stdout.write(tc_str)
    f.write(tc_str)

    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')
    time.sleep(0.1)    

    e_str = '{0:11.11s}'.format(get_e()) 
    sys.stdout.write(e_str)
    f.write(e_str)
        
    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')
    time.sleep(0.1)    

    diode_str = '{0:>5.5s}'.format(get_diode())
    sys.stdout.write(diode_str)
    f.write(diode_str)

    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')
    time.sleep(0.1)    

    pwm_str = '{0:>3.3s}'.format(get_pwm())
    sys.stdout.write(pwm_str)
    f.write(pwm_str)

    sys.stdout.write(' ')
    sys.stdout.flush()
    f.write(' ')
    time.sleep(0.1)    

    rpm_str = '{0:>4.4s}'.format(get_rpm())
    sys.stdout.write(rpm_str)
    f.write(rpm_str)

    sys.stdout.write('\r\n')
    sys.stdout.flush()
    f.write('\n')

    f.close()

    while (len(com_port_recv_char()) == 1):
        continue

def get_vacuum():
    vac_str = ''

    com_port.write('getvacuum' + '\r')
    com_port_recv_line() # throw away echoed command
    line = com_port_recv_line() 

    try:
        if (not(len(line) > 0)): 
            raise Exception('')
        field = line.split(' ')[0]
        vac_val = float(field)
        vac_str = '{0:.1e}'.format(vac_val)
    except Exception:
        vac_str = '-------'

    return (vac_str)

def get_vac_p316():
    p316_str = ''

    com_port.write('p316' + '\r')
    com_port_recv_line() # throw away echoed command
    line = com_port_recv_line() 

    try:
        if (not(len(line) > 0)): 
            raise Exception('')
        p316_val = int(line, 10)
        p316_str = '{0:3d}'.format(p316_val)
    except Exception:
        p316_str = '----'

    return (p316_str)    

def get_vac_p398():
    p398_str = ''

    com_port.write('p398' + '\r')
    com_port_recv_line() # throw away echoed command
    line = com_port_recv_line() 

    try:
        if (not(len(line) > 0)): 
            raise Exception('')
        p398_val = int(line, 10)
        p398_str = '{0:5d}'.format(p398_val)
    except Exception:
        p398_str = '-----'

    return (p398_str)    

def get_vac_p346():
    p346_str = ''

    com_port.write('p346' + '\r')
    com_port_recv_line() # throw away echoed command
    line = com_port_recv_line() 

    try:
        if (not(len(line) > 0)): 
            raise Exception('')
        p346_val = int(line, 10)
        p346_str = '{0:4d}'.format(p346_val)
    except Exception:
        p346_str = '----'

    return (p346_str)    

def get_temp(address):
    temp_str = ''

    com_port.write('gettemp' + ' ' + address + '\r')
    com_port_recv_line() # throw away echoed command
    line = com_port_recv_line() 

    try:
        if (not(len(line) > 0)): 
            raise Exception('')
        field = line.split(' ')[0]
        temp_val = float(field)
        temp_str = '{0:3.0f}'.format(temp_val)
    except Exception:
        temp_str = '---'

    return (temp_str)    

def get_tc():
    tc_str = ''

    com_port.write('TC' + '\r')
    com_port_recv_line() # throw away echoed command
    line = com_port_recv_line() 

    try:
        if (not(len(line) > 0)): 
            raise Exception('')
        tc_val = float(line)
        tc_str = '{0:3.0f}'.format(tc_val)
    except Exception:
        tc_str = '---'

    return (tc_str)

def get_e():
    max_str = ''
    min_str = ''
    cur_str = ''

    com_port.write('E' + '\r')
    com_port_recv_line() # throw away echoed command
    max_line = com_port_recv_line() 
    min_line = com_port_recv_line() 
    cur_line = com_port_recv_line() 

    try:
        if (not(len(max_line) > 0)): 
            raise Exception('')
        max_val = float(max_line)
        max_str = '{0:3.0f}'.format(max_val)
    except Exception:
        max_str = '---'

    try:
        if (not(len(min_line) > 0)): 
            raise Exception('')
        min_val = float(min_line)
        min_str = '{0:3.0f}'.format(min_val)
    except Exception:
        min_str = '---'

    try:
        if (not(len(cur_line) > 0)): 
            raise Exception('')
        cur_val = float(cur_line)
        cur_str = '{0:3.0f}'.format(cur_val)
    except Exception:
        cur_str = '---'

    e_str = '{0:>3.3s} {1:>3.3s} {2:>3.3s}'.format(max_str, min_str, cur_str)

    return (e_str)

def get_diode():
    diode_str = ''

    com_port.write('getdiode -v' + '\r')
    com_port_recv_line() # throw away echoed command
    line = com_port_recv_line() 

    try:
        if (not(len(line) > 0)): 
            raise Exception('')
        field = line.split(' ')[0]
        diode_val = float(field)
        diode_str = '{0:5.3f}'.format(diode_val)
    except Exception:
        diode_str = '-----'

    return (diode_str)

def get_pwm():
    pwm_str = ''

    com_port.write('getfanpwm' + '\r')
    com_port_recv_line() # throw away echoed command
    line = com_port_recv_line() 

    try:
        if (not(len(line) > 0)): 
            raise Exception('')
        pwm_val = int(line, 10)
        pwm_str = '{0:3d}'.format(pwm_val)
    except Exception:
        pwm_str = '---'

    return (pwm_str)    

def get_rpm():
    rpm_str = ''

    com_port.write('getfanrpm' + '\r')
    com_port_recv_line() # throw away echoed command
    line = com_port_recv_line() 

    try:
        if (not(len(line) > 0)): 
            raise Exception('')
        rpm_val = int(line, 10)
        rpm_str = '{0:4d}'.format(rpm_val)
    except Exception:
        rpm_str = '----'

    return (rpm_str)    

main()