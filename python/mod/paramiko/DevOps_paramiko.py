🧭 Что такое Paramiko

Paramiko — это чисто-питоновская реализация протоколов SSHv2 и SFTP,
которая позволяет работать с удалёнными Linux/Unix машинами программно (без прямого ssh в терминале).

📦 Установка:

pip install paramiko

⚙️ Основные возможности
Возможность	Описание
🔑 SSH-клиент	Подключение по SSH и выполнение команд
📂 SFTP	Передача файлов (upload/download)
🧰 Key-based auth	Аутентификация по приватному ключу
🧱 Туннелирование	(реже используется) перенаправление портов
🖥️ SSH-сервер	Можно создать свой мини SSH-сервер (редко в DevOps)
🧩 Основные объекты и классы
Класс	Назначение
paramiko.SSHClient()	Основной клиент для SSH
paramiko.AutoAddPolicy()	Автоматическое добавление host key
paramiko.RSAKey, Ed25519Key	Работа с ключами
paramiko.SFTPClient()	Работа с файлами по SFTP
paramiko.Transport()	Низкоуровневое подключение (используется внутри SSHClient)
🔐 Пример 1. Подключение по логину и паролю
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # авто-добавление ключей

ssh.connect(
    hostname="192.168.1.10",
    username="ubuntu",
    password="1234",
    port=22
)

stdin, stdout, stderr = ssh.exec_command("uname -a")
print(stdout.read().decode())

ssh.close()


💡 Так можно получить системную информацию, логи, статус сервисов и т.д.

🔑 Пример 2. Подключение по ключу (без пароля)
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname="192.168.1.10",
    username="ubuntu",
    key_filename="/home/user/.ssh/id_rsa"
)

stdin, stdout, stderr = ssh.exec_command("df -h")
print(stdout.read().decode())

ssh.close()


💡 Обычно DevOps-инженеры используют именно key-based auth (а не пароли).

🧾 Пример 3. Выполнение нескольких команд подряд
commands = [
    "hostname",
    "uptime",
    "free -h"
]

for cmd in commands:
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(f"[{cmd}]")
    print(stdout.read().decode().strip())

📂 Пример 4. Загрузка и скачивание файлов (SFTP)
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.1.10", username="ubuntu", key_filename="~/.ssh/id_rsa")

sftp = ssh.open_sftp()
sftp.get("/remote/path/app.log", "app.log")        # скачать
sftp.put("local_script.sh", "/remote/path/script.sh")  # загрузить
sftp.close()

ssh.close()

⚙️ Пример 5. Выполнение команды с возвратом кода завершения
stdin, stdout, stderr = ssh.exec_command("systemctl restart nginx")
exit_status = stdout.channel.recv_exit_status()

if exit_status == 0:
    print("Nginx перезапущен успешно")
else:
    print("Ошибка:", stderr.read().decode())

🪄 Полезные приёмы для понимания
✅ 1. Контекстный менеджер (авто-закрытие)
from paramiko import SSHClient, AutoAddPolicy

with SSHClient() as ssh:
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect("192.168.1.10", username="ubuntu", key_filename="~/.ssh/id_rsa")
    stdin, stdout, stderr = ssh.exec_command("uptime")
    print(stdout.read().decode())

✅ 2. Подключение к списку серверов
servers = ["192.168.1.10", "192.168.1.11"]

for host in servers:
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username="ubuntu", key_filename="~/.ssh/id_rsa")
        stdin, stdout, _ = ssh.exec_command("uptime")
        print(f"{host}: {stdout.read().decode().strip()}")

✅ 3. Обработка ошибок
import paramiko

try:
    ssh.connect("192.168.1.100", username="root", password="1234")
except paramiko.AuthenticationException:
    print("Ошибка авторизации")
except paramiko.SSHException as e:
    print("Ошибка SSH:", e)
except Exception as e:
    print("Другая ошибка:", e)

