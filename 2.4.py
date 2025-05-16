class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value

counter = Counter()
print(f"Текущее значение: {counter.get_value()}")
counter.increment()
print(f"Значение после увеличения: {counter.get_value()}")
counter.decrement()
print(f"Значение после уменьшения: {counter.get_value()}")