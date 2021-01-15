import serial
import time
from ominibot_car_com import Ominibot_Car
if __name__ == '__main__':
    while True:
        a=0
        a=a+1
        if a > 255:
            print("找不到COM")
            break
        try:
            _port = "ttyUSB"+str(a)
            _baud = 115200
            ominibot  = Ominibot_Car(_port,_baud, py_version=3)
            break
        except:
            pass
    ominibot.set_motor_voltage( voltage=12)
    while True:
        ser.flushInput()
        com =ser.read(3)
        if com == b'sto':
            ominibot.individual_wheel(v1=0, v2=0, v3=0, v4=0, mode=0x02)
        elif com ==b'for':
            ominibot.individual_wheel(v1=100, v2=100, v3=100, v4=100, mode=0x02)
        elif com ==b'bac':
            ominibot.individual_wheel(v1=-100, v2=-100, v3=-100, v4=-100, mode=0x02)
        elif com ==b'lef':
            ominibot.individual_wheel(v1=100, v2=-100, v3=-100, v4=100, mode=0x02)
        elif com ==b'rig':
            ominibot.individual_wheel(v1=-100, v2=100, v3=100, v4=-100, mode=0x02)
        elif com ==b'rsp':
            ominibot.individual_wheel(v1=100, v2=100, v3=-100, v4=-100, mode=0x02)
        elif com ==b'lsp':
            ominibot.individual_wheel(v1=20, v2=20, v3=20, v4=20, mode=0x02)
        elif com ==b'rst':
            ominibot.individual_wheel(v1=0, v2=100, v3=100, v4=0, mode=0x02)
        elif com ==b'rsd':
            ominibot.individual_wheel(v1=0, v2=-100, v3=-100, v4=0, mode=0x02)
        elif com ==b'lst':
            ominibot.individual_wheel(v1=100, v2=0, v3=0, v4=100, mode=0x02)
        elif com ==b'lsd':
            ominibot.individual_wheel(v1=-100, v2=0, v3=0, v4=-100, mode=0x02)
        time.sleep(0.01)
            
        
        

