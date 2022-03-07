f = open('notes.txt', 'r')  # чтение данных с файла
first_string = f.readline()  # чтение первой строки
second_string = f.readline()  # чтение второй строки
split1 = first_string.split(':')  # разделение через двоеточие первой строки
split2 = second_string.split(':')  # разделение через двоеточие второй строки
longitude = float(split1[1])  # долгота
latitude = float(split2[1])  # широта
# print(longitude)
# print(latitude)
