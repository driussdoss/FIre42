💻 Примеры из реальной работы DevOps
🧰 1. Проверить статус сервиса
import subprocess

res = subprocess.run(["systemctl", "is-active", "nginx"], capture_output=True, text=True)
print("Статус nginx:", res.stdout.strip())

🧰 2. Перезапустить контейнер
import subprocess

subprocess.run(["docker", "restart", "web_app"], check=True)
print("Контейнер перезапущен ✅")

🧰 3. Получить текущего пользователя
import subprocess

user = subprocess.check_output(["whoami"], text=True).strip()
print("Скрипт запущен от:", user)

🧰 4. Проверить свободное место на диске
import subprocess

disk = subprocess.check_output(["df", "-h", "/"], text=True)
print(disk)

🧰 5. Автоматический деплой (упрощённо)
import subprocess

for cmd in [["git", "pull"], ["docker-compose", "build"], ["docker-compose", "up", "-d"]]:
    res = subprocess.run(cmd)
    if res.returncode != 0:
        print("Ошибка:", " ".join(cmd))
        break
