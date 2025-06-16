s = input("Введите строку: ")
if s.startswith('abc'):
    s = 'www' + s[3:]
else:
    s += 'zzz'
print("Результат:", s)