numbers = [3, -5, 25, 7, -1, 42, -2, 0, 81, -4, 13]

two_digit = []
for num in numbers:
    if 10 <= num <= 99:
        two_digit.append(num)

two_digit.sort()
print("Двузначные числа по возрастанию:", two_digit)