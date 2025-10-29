#здесь будут реальные рабочие примеры

⚙️ 1. Работа с путями и логами (log rotation / структура проекта)

import os
from datetime import datetime

log_dir = "/var/log/myapp"
os.makedirs(log_dir, exist_ok=True)

filename = datetime.now().strftime("%Y-%m-%d.log")
path = os.path.join(log_dir, filename)

with open(path, "a") as f:
    f.write("Сервис успешно запущен\n")


🔹 Реальный кейс: при деплое или запуске сервиса логировать в отдельный файл по дате
(аналог mkdir -p /var/log/myapp && echo ... >> /var/log/myapp/2025-10-08.log).

⚙️ 2. Проверка переменных окружения (например, креды или токены)

import os
token = os.environ.get("AWS_ACCESS_KEY_ID")

if not token:
    raise SystemExit("❌ Нет AWS_ACCESS_KEY_ID в окружении!")

print("✅ Токен найден.")


🔹 Реальный кейс: перед запуском Terraform, Ansible, CI-скрипта — проверяешь, что нужные переменные заданы
(аналог if [ -z "$AWS_ACCESS_KEY_ID" ]; then echo "Missing"; exit 1; fi).

⚙️ 3. Запуск системных команд из Python (аналог shell-скрипта)

import os

ret = os.system("systemctl restart nginx")
if ret != 0:
    print("Ошибка при перезапуске Nginx")


🔹 Реальный кейс: Python-скрипт выполняет команды для CI/CD пайплайна
(например, деплой, рестарт сервисов, health-check).

⚠️ В продакшне чаще используют subprocess, но os.system — базовый и понятный.

⚙️ 4. Получение информации о системе

import os

print("Текущий пользователь:", os.getlogin())
print("PID процесса:", os.getpid())
print("Текущая директория:", os.getcwd())


🔹 Реальный кейс: при отладке контейнеров, сервисов или при запуске демонов — полезно логировать PID, пользователя и рабочий путь.

⚙️ 5. Навигация и работа с файлами

import os

for root, dirs, files in os.walk("/etc"):
    for f in files:
        if f.endswith(".conf"):
            print(os.path.join(root, f))


🔹 Реальный кейс: собрать список всех конфигов или файлов, которые нужно бэкапить или мониторить
(аналог find /etc -name "*.conf").

⚙️ 6. Проверка существования путей

import os

path = "/etc/nginx/nginx.conf"

if os.path.exists(path):
    print("Файл найден ✅")
else:
    print("Файл не найден ❌")


🔹 Реальный кейс: DevOps-скрипт проверяет наличие конфигов перед деплоем или рестартом.

⚙️ 7. Смена директории

import os

os.chdir("/var/www")
print("Текущая директория:", os.getcwd())


🔹 Реальный кейс: при сборке проекта, миграциях, копировании артефактов (аналог cd /var/www).
