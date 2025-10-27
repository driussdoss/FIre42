# здесь будут более реальные примеры которые используются в работе

#1. mini cli для запуска деплоя
#!/usr/bin/env python3
import sys, os

if len(sys.argv) < 2:
    print("❌ Использование: deploy.py <env>")
    sys.exit(1)

env = sys.argv[1]

if env not in ["dev", "staging", "prod"]:
    print("❌ Неизвестная среда:", env)
    sys.exit(1)

print(f"🚀 Деплой в среду {env}...")
os.system(f"ansible-playbook deploy_{env}.yml")


#2. проверка версии python и OS
import sys

if sys.version_info < (3, 10):
    print("⚠️ Требуется Python 3.10 или новее!")
    sys.exit(1)

if sys.platform.startswith("linux"):
    print("✅ Linux-среда обнаружена")
else:
    print("❌ Нужен Linux для этого скрипта")
    sys.exit(1)
#3. работа с путями моделуй sys.path
import sys
from pathlib import Path

# Добавляем свою директорию с модулями
sys.path.append(str(Path(__file__).parent / "lib"))

from utils import docker_helper

docker_helper.deploy_container("nginx")

#4. вывод с кодом состояни
import sys, os

result = os.system("kubectl get pods")

if result != 0:
    print("❌ Ошибка при получении списка pod'ов")
    sys.exit(2)

print("✅ Команда выполнена успешно")
sys.exit(0)

#5. разделение stdout stderr
import sys
import subprocess

proc = subprocess.Popen(
    ["kubectl", "apply", "-f", "deployment.yml"],
    stdout=sys.stdout,
    stderr=sys.stderr
)
proc.wait()
sys.exit(proc.returncode)

#6. проверка аргументов при выполнении команды
import sys, os

if len(sys.argv) < 3:
    print("Использование: backup.py <source> <destination>")
    sys.exit(1)

src, dst = sys.argv[1], sys.argv[2]
os.system(f"rsync -av {src} {dst}")

#7. разные действия для разных осей
import sys, os

if sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")

#8. безопастный вывод при ошибках
import sys, subprocess

try:
    subprocess.check_call(["docker", "ps"])
except subprocess.CalledProcessError:
    print("Ошибка: Docker не запущен!")
    sys.exit(1)

#9. использование stdin/stdout для пайпов
# uppercase.py
import sys

for line in sys.stdin:
    sys.stdout.write(line.upper())

#10. вывод системной информации для диагностики
import sys
import platform

print(f"Python version: {sys.version.split()[0]}")
print(f"Platform: {sys.platform}")
print(f"Architecture: {platform.machine()}")
print(f"Executable: {sys.executable}")

