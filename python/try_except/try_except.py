Отличный вопрос — `try` / `except` — **один из важнейших инструментов DevOps-инженера**,
потому что любая автоматизация (будь то AWS через `boto3`, SSH через `paramiko` или деплой через `subprocess`) должна быть **устойчива к ошибкам**.

---

# ⚙️ БАЗА: Что такое `try` / `except`

Конструкция `try` / `except` используется для **обработки исключений** — ситуаций, когда программа падает с ошибкой.
Вместо “красного трейсбэка” можно отреагировать: записать лог, повторить действие, уведомить Slack и т.д.

---

## 🧩 Синтаксис:

```python
try:
    # Код, где возможна ошибка
    risky_operation()
except SomeError:
    # Что делать, если ошибка
    print("Произошла ошибка!")
```

---

## 🔹 Пример:

```python
try:
    num = int(input("Введите число: "))
    print(10 / num)
except ValueError:
    print("Ошибка: нужно ввести число!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
```

---

# 🧠 Что должен знать DevOps

---

## 1. 🎯 Ловля конкретных ошибок

Никогда не используй голый `except:` — это “поймает всё” (включая системные ошибки).
Лучше указывать конкретные классы ошибок.

```python
import boto3
from botocore.exceptions import ClientError

try:
    s3 = boto3.client("s3")
    s3.create_bucket(Bucket="test-bucket")
except ClientError as e:
    print("Ошибка AWS:", e.response["Error"]["Message"])
```

> ✅ Так ты получаешь точное сообщение от AWS, а не “упавший” скрипт.

---

## 2. 🪶 Блок `else`

Исполняется, **если не было ошибок**.

```python
try:
    print("Подключаемся к базе...")
except ConnectionError:
    print("Не удалось подключиться")
else:
    print("Подключение успешно!")
```

---

## 3. 🧹 Блок `finally`

Исполняется **всегда**, даже если произошла ошибка.
Обычно используется для **очистки ресурсов**: закрытия файлов, соединений и т.д.

```python
file = open("log.txt", "w")
try:
    file.write("Start logging\n")
    raise ValueError("что-то пошло не так")
except ValueError:
    print("Ошибка записи")
finally:
    file.close()  # гарантированное закрытие файла
```

---

## 4. 🪣 Ловля нескольких ошибок

```python
try:
    risky_code()
except (OSError, ValueError) as e:
    print("Ошибка:", e)
```

---

## 5. ⚡ Поднятие исключений вручную

Если ты хочешь **прервать выполнение** и показать, что что-то пошло не так:

```python
if not os.path.exists("/etc/config.yaml"):
    raise FileNotFoundError("Конфиг не найден!")
```

---

## 6. 🪪 Вложенные try-except

```python
try:
    connect_to_server()
    try:
        send_data()
    except TimeoutError:
        print("Сервер не ответил.")
except ConnectionError:
    print("Не удалось подключиться.")
```

---

## 7. 📜 Использование с логированием (`logging`)

В DevOps-скриптах **ошибки должны логироваться**, а не просто печататься:

```python
import logging
from botocore.exceptions import ClientError

logging.basicConfig(filename='error.log', level=logging.ERROR)

try:
    ec2.start_instances(InstanceIds=['i-123456'])
except ClientError as e:
    logging.error("Ошибка при запуске EC2: %s", e)
```
