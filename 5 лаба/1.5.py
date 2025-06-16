def calculate(a, b):
    return (a + 4*b) * (a - 3*b) + a**2

a = float(input("Введите a: "))
b = float(input("Введите b: "))
print("Результат:", calculate(a, b))