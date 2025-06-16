A = ['apple', 'banana', 'car', 'cucumber', 'cat', 'dog', 'c', 'carpet']
C = 'c'

count = 0
for item in A:
    if len(item) > 1 and item.startswith(C) and item.endswith(C):
        count += 1

print(f"Количество элементов, начинающихся и заканчивающихся на '{C}': {count}")