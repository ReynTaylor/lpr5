class Worker:
    def init(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def GetSalary(self):
        salary = self.rate * self.days
        print("Зарплата работника:", salary)

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_rate(self):
        return self.rate

    def get_days(self):
        return self.days

worker = Worker("Иван", "Иванов", 120, 25)
worker.GetSalary()
print("Имя работника:", worker.get_name())
print("Фамилия работника:", worker.get_surname())