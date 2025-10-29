Отличный и **очень зрелый** вопрос 👏
То, что ты спрашиваешь про классы ошибок — это **именно то, что отличает хорошего DevOps-инженера** от просто “пишущего скрипты”.

---

# 💡 Кратко: что такое классы ошибок

В Python **все ошибки — это объекты**, унаследованные от базового класса `Exception`.

👉 Это значит, что у каждой библиотеки (`boto3`, `paramiko`, `requests`, `subprocess`)
могут быть **свои типы ошибок**, и их можно ловить выборочно:

```python
try:
    risky_operation()
except ValueError:
    ...
except FileNotFoundError:
    ...
except CustomError:
    ...
```

---

# 🧱 1. Иерархия ошибок в Python (база)

| Класс               | Когда возникает                                |
| ------------------- | ---------------------------------------------- |
| `Exception`         | Родитель всех ошибок                           |
| `ValueError`        | Неверный тип/значение (например, `int("abc")`) |
| `TypeError`         | Неверный тип данных (`"a" + 1`)                |
| `KeyError`          | Нет ключа в словаре                            |
| `IndexError`        | Индекс вне диапазона                           |
| `FileNotFoundError` | Нет такого файла/пути                          |
| `OSError`           | Ошибка работы с ОС (права, файлы, директории)  |
| `ZeroDivisionError` | Деление на ноль                                |
| `ImportError`       | Ошибка импорта модуля                          |
| `RuntimeError`      | Общая ошибка выполнения                        |
| `KeyboardInterrupt` | Прерывание Ctrl+C                              |

💬 Все они в `builtins`, то есть стандартные.

---

# ⚙️ 2. Ошибки по модулям DevOps

Теперь перейдём к **реальным библиотекам**, с которыми ты как DevOps будешь работать каждый день.

---

## 🧩 `subprocess`

**Ошибки:**

| Ошибка                          | Когда бывает                  |
| ------------------------------- | ----------------------------- |
| `subprocess.CalledProcessError` | Команда вернула ненулевой код |
| `FileNotFoundError`             | Команда не найдена            |
| `TimeoutExpired`                | Процесс завис по времени      |

**Пример:**

```python
import subprocess

try:
    subprocess.run(["systemctl", "restart", "nginx"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Ошибка выполнения: {e.returncode}")
except FileNotFoundError:
    print("Команда не найдена")
except subprocess.TimeoutExpired:
    print("Команда зависла по таймауту")
```

---

## ☁️ `boto3` / `botocore` (AWS SDK)

`boto3` использует собственный тип ошибки:

| Ошибка                            | Когда возникает                      |
| --------------------------------- | ------------------------------------ |
| `botocore.exceptions.ClientError` | Ошибка от AWS API (403, 404, и т.д.) |
| `NoCredentialsError`              | Нет AWS-ключей                       |
| `EndpointConnectionError`         | Нет соединения с AWS                 |
| `ParamValidationError`            | Неверные аргументы в запросе         |
| `WaiterError`                     | Ошибка при ожидании статуса ресурса  |

**Пример:**

```python
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

s3 = boto3.client("s3")

try:
    s3.create_bucket(Bucket="test-bucket-1234")
except NoCredentialsError:
    print("Нет AWS ключей!")
except ClientError as e:
    print("Ошибка AWS:", e.response["Error"]["Message"])
```

> 🔎 Документация по ошибкам boto3:
> [https://botocore.amazonaws.com/v1/documentation/api/latest/reference/exceptions.html](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/exceptions.html)

---

## 🔐 `paramiko`

| Ошибка                             | Когда возникает           |
| ---------------------------------- | ------------------------- |
| `paramiko.AuthenticationException` | Неправильный логин/пароль |
| `paramiko.SSHException`            | Ошибка в SSH-протоколе    |
| `paramiko.BadHostKeyException`     | Не совпал ключ хоста      |
| `socket.timeout`                   | Таймаут подключения       |

**Пример:**

```python
import paramiko, socket

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.1.10", username="root", password="badpass")
except paramiko.AuthenticationException:
    print("Ошибка авторизации SSH")
except paramiko.SSHException as e:
    print("Ошибка SSH:", e)
except socket.timeout:
    print("Подключение по SSH не удалось (таймаут)")
```

---

## 🌐 `requests`

| Ошибка                                 | Когда возникает          |
| -------------------------------------- | ------------------------ |
| `requests.exceptions.RequestException` | Базовый класс для всех   |
| `ConnectionError`                      | Нет соединения           |
| `Timeout`                              | Истекло время ожидания   |
| `HTTPError`                            | Сервер вернул 4xx/5xx    |
| `TooManyRedirects`                     | Слишком много редиректов |

**Пример:**

```python
import requests

try:
    r = requests.get("https://example.com", timeout=3)
    r.raise_for_status()
except requests.exceptions.Timeout:
    print("Сервер долго отвечает!")
except requests.exceptions.ConnectionError:
    print("Ошибка соединения")
except requests.exceptions.HTTPError as e:
    print("HTTP ошибка:", e)
```

---

# 🧰 Где искать список ошибок

| Модуль          | Где смотреть                                                                                                |
| --------------- | ----------------------------------------------------------------------------------------------------------- |
| Python builtins | [docs.python.org → Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)                  |
| `subprocess`    | [docs.python.org → subprocess](https://docs.python.org/3/library/subprocess.html#exceptions)                |
| `requests`      | [Requests Exceptions](https://requests.readthedocs.io/en/latest/api/#exceptions)                            |
| `boto3`         | [Botocore Exceptions](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/exceptions.html) |
| `paramiko`      | [Paramiko Exceptions](https://docs.paramiko.org/en/stable/api/errors.html)                                  |

---

# ⚙️  Как DevOps должен работать с ошибками

1. **Всегда знать “какие бывают” ошибки в библиотеке.**
   → смотри документацию и импортируй их из `exceptions`.

2. **Никогда не глуши ошибки просто `except:`**
   → это убивает диагностику.

3. **Логируй и пробрасывай.**

```python
try:
    do_something()
except SomeError as e:
    logging.error("Ошибка: %s", e)
    raise  # пробрасывает ошибку дальше
```

4. **Используй retry-логику**
   (особенно при работе с сетью, AWS, API).

---

