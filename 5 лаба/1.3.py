import random

n = int(input("Введите длину массива: "))
arr = sorted(random.randrange(0, 100, 2) for _ in range(n))
print("Массив чётных чисел:", arr)