import serial
ser = serial.Serial('/dev/serial0')
ser.baudrate = 115200

msg = '11001100'
msg = msg.encode('utf-8')
ser.write(msg)
print("Строка успешно отправлена")
