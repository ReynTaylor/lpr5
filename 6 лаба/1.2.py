class User:
    def __init__(self, login, password):
        self.Login = login
        self.Password = password

users = [
    User("ivanov", "qwerty123"),
    User("petrov", "asdfgh456"),
    User("sidorov", "zxcvbn789"),
    User("smirnov", "password1"),
    User("popov", "hello123")
]

search_login = "sidorov"
search_password = "zxcvbn789"

found_user = None
for user in users:
    if user.Login == search_login and user.Password == search_password:
        found_user = user
        break

if found_user:
    print(f"Найден пользователь: Логин - {found_user.Login}, Пароль - {found_user.Password}")
else:
    print("Пользователь не найден")