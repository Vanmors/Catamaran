import serial
ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 115200


protocolUART = "S" + motorSpeed() + angleServo() + "E"
# print(protocolUART)
protocolUART = protocolUART.encode('utf-8')
ser.write(protocolUART)
print("String sended")


def motorSpeed():
    speed = "99"
    if -1 < int(speed) < 10:
        return "0" + speed
    else:
        return speed


def angleServo():
    angle = "180"
    if -1 < int(angle) < 10:
        return "00" + angle
    elif 9 < int(angle) < 100:
        return "0" + angle
    else:
        return angle
