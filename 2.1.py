class Student:
    def __init__(self, surname, birth_date, group_number, grades):
        self.surname = surname
        self.birth_date = birth_date
        self.group_number = group_number
        self.grades = grades

    def change_surname(self, new_surname):
        self.surname = new_surname

    def change_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date

    def change_group_number(self, new_group_number):
        self.group_number = new_group_number

    def display_info(self):
        print(f"Фамилия: {self.surname}")
        print(f"Дата рождения: {self.birth_date}")
        print(f"Номер группы: {self.group_number}")
        print(f"Успеваемость: {self.grades}")

student1 = Student("Иванов", "2000-01-01", "A101", [5, 4, 3, 5, 4])
student1.display_info()

new_surname = input("Введите новую фамилию: ")
student1.change_surname(new_surname)
student1.display_info()
