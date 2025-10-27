import os
from datetime import datetime

# 1. Определяем текущую дату
today = datetime.now()
folder_path = os.path.join(
    "logs",
    str(today.year),
    str(today.month).zfill(2),
    str(today.day).zfill(2)
)

# 2. Создаём вложенные папки (если их нет)
os.makedirs(folder_path, exist_ok=True)

# 3. Путь к файлу
log_file = os.path.join(folder_path, "app.log")

# 4. Записываем сообщение
with open(log_file, "a") as f:
    f.write("Программа запущена\n")

print(f"Лог сохранён в: {log_file}")

