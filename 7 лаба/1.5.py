class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

sessions = [
    FitnessCenter("A001", 2022, 1, 60),
    FitnessCenter("A002", 2022, 2, 45),
    FitnessCenter("A003", 2023, 3, 90),
    FitnessCenter("A004", 2023, 4, 30),
    FitnessCenter("A005", 2023, 5, 120),
    FitnessCenter("A006", 2023, 6, 60),
    FitnessCenter("A007", 2024, 7, 45),
    FitnessCenter("A008", 2024, 8, 90),
    FitnessCenter("A009", 2024, 9, 180),
    FitnessCenter("A010", 2024, 10, 60)
]

year_durations = {}
for session in sessions:
    if session.year in year_durations:
        year_durations[session.year] += session.duration
    else:
        year_durations[session.year] = session.duration

max_year = min(year_durations.keys())
max_duration = year_durations[max_year]

for year, duration in year_durations.items():
    if duration > max_duration or (duration == max_duration and year < max_year):
        max_year = year
        max_duration = duration

print(f"Год с наибольшей продолжительностью занятий: {max_year}")
print(f"Суммарная продолжительность: {max_duration} минут")