class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

sessions = [
    FitnessCenter("A001", 2023, 1, 60),
    FitnessCenter("A002", 2023, 2, 45),
    FitnessCenter("A003", 2023, 3, 90),
    FitnessCenter("A004", 2023, 4, 30),
    FitnessCenter("A005", 2023, 5, 120)
]

shortest = longest = sessions[0]
for session in sessions[1:]:
    if session.duration < shortest.duration:
        shortest = session
    if session.duration > longest.duration:
        longest = session

print("Самое короткое занятие:")
print(f"Код: {shortest.client_code}, Длительность: {shortest.duration} мин")
print("\nСамое долгое занятие:")
print(f"Код: {longest.client_code}, Длительность: {longest.duration} мин")