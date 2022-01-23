import serial
import micropyGPS
import threading
import time

gps = micropyGPS.MicropyGPS(9, 'dd')  # Создание объекта MicroGPS


# Аргументы - разница во времени часового пояса и формат вывода

def rungps():  # Чтение модуля GPS и обновление объекта GPS
    s = serial.Serial('/dev/serial0', 9600, timeout=10)
    s.readline()  # Отказываемся от первой строки, так как она может считывать незаконченные данные
    while True:
        sentence = s.readline().decode('utf-8')  # Чтение данных GPS и преобразование их в строку символов
        if sentence[0] != '$':  # Если первый символ $ - начать
            continue
        for x in sentence:  # Проанализируйте прочитанную строку символов и добавьте или обновите данные к объекту GPS
            gps.update(x)


gpsthread = threading.Thread(target=rungps, args=())  # Создание потока для выполнения вышеуказанной функции
gpsthread.daemon = True
gpsthread.start()

while True:
    if gps.clean_sentences > 20:  # Вывод, когда правильные данные накапливаются
        h = gps.timestamp[0] if gps.timestamp[0] < 24 else gps.timestamp[0] - 24
        print('%2d:%02d:%04.1f' % (h, gps.timestamp[1], gps.timestamp[2]))
        print('долгота широта: %2.8f, %2.8f' % (gps.latitude[0], gps.longitude[0]))
time.sleep(3.0)
