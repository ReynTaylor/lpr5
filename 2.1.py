import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("Минимальный элемент коллекции:", min(numbers))