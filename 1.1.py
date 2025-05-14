J = "ab"
S = "aabbccd"

count = 0

for stone in S:
    if stone in J:
        count += 1

print(count)
