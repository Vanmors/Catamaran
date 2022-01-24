import math

gpslat1 = 35  # Долгота начальной точки
gpslong1 = 37  # Широта начальной точки

gpslat2 = 46  # Долгота конечной точки
gpslong2 = 42  # Широта конечной точки

x = math.fabs(gpslat2 - gpslat1)  # Вычисление x для вектора движения
y = math.fabs(gpslong2 - gpslong1)  # Вычисление y для вектора движения
try:
    degree = math.degrees(math.asin((y / (math.sqrt(x * x + y * y)))))  # Вычисление градуса поворота
    print('%2.2f' % (degree))
except:
    print("Division by zero")
