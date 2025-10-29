💼 Примеры из практики DevOps
🔹 Пример 1 — безопасный деплой
import subprocess, logging

try:
    subprocess.run(["systemctl", "restart", "nginx"], check=True)
except subprocess.CalledProcessError as e:
    logging.error("Не удалось перезапустить nginx: %s", e)
else:
    logging.info("nginx успешно перезапущен")

🔹 Пример 2 — загрузка в S3 с повтором
import boto3, time
from botocore.exceptions import ClientError

s3 = boto3.client("s3")

for attempt in range(3):
    try:
        s3.upload_file("backup.tar.gz", "my-bucket", "backup.tar.gz")
        print("Загрузка успешна")
        break
    except ClientError as e:
        print(f"Попытка {attempt+1} не удалась:", e)
        time.sleep(3)
else:
    print("Все попытки не удались — выходим")

🔹 Пример 3 — SSH через Paramiko
import paramiko, logging

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.1.10", username="root", password="1234")
except paramiko.AuthenticationException:
    logging.error("Неверный пароль SSH!")
except paramiko.SSHException as e:
    logging.error("Ошибка SSH: %s", e)
else:
    stdin, stdout, stderr = ssh.exec_command("uptime")
    print(stdout.read().decode())
finally:
    ssh.close()
