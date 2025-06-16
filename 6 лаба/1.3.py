class Task:
    def __init__(self, date_start, date_finish, description):
        self.DateStart = date_start
        self.DateFinish = date_finish
        self.Description = description

tasks = [
    Task("2023-01-01 10:00", "2023-01-01 12:00", "Лекция по математике"),
    Task("2023-01-02 09:00", "2023-01-02 11:00", "Практика по программированию"),
    Task("2023-01-03 14:00", "2023-01-03 18:00", "Семинар по физике"),
    Task("2023-01-04 13:00", "2023-01-04 15:00", "Консультация"),
    Task("2023-01-05 16:00", "2023-01-05 19:00", "Экзамен")
]

latest_task = tasks[0]
for task in tasks[1:]:
    if task.DateFinish > latest_task.DateFinish:
        latest_task = task

print("Самое позднее занятие:")
print(f"Описание: {latest_task.Description}")
print(f"Начало: {latest_task.DateStart}")
print(f"Окончание: {latest_task.DateFinish}")