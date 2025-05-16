class TwoProperties:
    def __init__(self, prop1=0, prop2=0):
        self.prop1 = prop1
        self.prop2 = prop2

    def __del__(self):
        print("Объект удален")

obj = TwoProperties(5, 10)
print(f"Первое свойство: {obj.prop1}, Второе свойство: {obj.prop2}")
del obj