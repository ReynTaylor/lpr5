def task2(arr):
    sum_pos = sum(x for x in arr if x > 0)

    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    product = 1
    for num in arr[start:end]:
        product *= num

    return sum_pos, product


numbers = [3, -5, 2, 7, -1, 4]
result = task2(numbers)
print("Сумма положительных:", result[0], "Произведение между min и max:", result[1])