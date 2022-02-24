import serial
ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 115200

msg = '12001200'
msg = msg.encode('utf-8')
ser.write(msg)
print("String sended")
