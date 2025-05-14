elements = []

while True:
    user_input = input("Введите элемент (или нажмите Enter для завершения): ")
    if user_input == "":
        break
    elements.append(user_input)

if elements:
    print("Самый короткий элемент:", min(elements, key=len))
    print("Самый длинный элемент:", max(elements, key=len))
else:
    print("Список пуст.")