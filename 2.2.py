class Train:
    def __init__(self, destination, train_number, departure_time):
        self.destination = destination
        self.train_number = train_number
        self.departure_time = departure_time

    def display_info(self):
        print(f"Пункт назначения: {self.destination}")
        print(f"Номер поезда: {self.train_number}")
        print(f"Время отправления: {self.departure_time}")

train1 = Train("Москва", "123", "12:30")
train1.display_info()

train_number = input("Введите номер поезда: ")
if train_number == train1.train_number:
    train1.display_info()
else:
    print("Поезд не найден")