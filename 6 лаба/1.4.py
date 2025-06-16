numbers = [3, -5, 2, 7, -1, 4, -2, 0, 8, -4]

first_positive = None
for num in numbers:
    if num > 0:
        first_positive = num
        break

last_negative = None
for num in reversed(numbers):
    if num < 0:
        last_negative = num
        break

print(f"Первый положительный: {first_positive}")
print(f"Последний отрицательный: {last_negative}")