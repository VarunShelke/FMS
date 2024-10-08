import serial
import RPi.GPIO as GPIO      
import os, time

GPIO.setmode(GPIO.BOARD)    

# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

port.write('AT'+'\r\n')
rcv = port.read(100)
print(rcv)
time.sleep(1)

port.write('AT+CGATT=1'+'\r\n')
rcv = port.read(100)
print(rcv)
time.sleep(1)

port.write('AT+SAPBR =3,1,"CONTYPE","GPRS"'+'\r\n')
rcv = port.read(100)
print(rcv)
time.sleep(1)

port.write('AT+SAPBR =3,1,"APN","RCMNET"'+'\r\n')
rcv = port.read(100)
print(rcv)
time.sleep(1)

port.write('AT+SAPBR=1,1'+'\r\n')
rcv = port.read(100)
print(rcv)
time.sleep(1)

port.write('AT+SAPBR=2,1'+'\r\n')
rcv = port.read(100)
print(rcv)
time.sleep(1)

port.write('AT+CIPGSMLOC=1,1'+'\r\n')
rcv = port.read(100)
print(rcv)
time.sleep(1)

port.write('AT+CIPGSMLOC=2,1'+'\r\n')
rcv = port.read(100)
print(rcv)
time.sleep(1)

port.write('AT+SAPBR =0,1'+'\r\n')
rcv = port.read(100)
print(rcv)
time.sleep(1)

port.write('ATE0'+'\r\n')      # Disable the Echo
rcv = port.read(100)
print(rcv)
time.sleep(1)

port.write('AT+CMGF=1'+'\r\n')  # Select Message format as Text mode 
rcv = port.read(100)
print(rcv)
time.sleep(1)

port.write('AT+CNMI=2,1,0,0,0'+'\r\n')   # New SMS Message Indications
rcv = port.read(100)
print(rcv)
time.sleep(1)

# Sending a message to a particular Number

port.write('AT+CMGS="7588975476"'+'\r\n')
rcv = port.read(100)
print(rcv)
time.sleep(1)

port.write('Sewage Overflow'+'\r\n')  # Message
rcv = port.read(100)
print(rcv)

port.write("\x1A") # Enable to send SMS
'''for i in range(10):
    rcv = port.read(100)
    print(rcv)'''