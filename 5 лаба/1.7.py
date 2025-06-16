import math

x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
r = float(input("Введите радиус круга: "))

distance = math.sqrt(x**2 + y**2)

if distance <= r:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")