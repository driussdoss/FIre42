🌍 Модуль requests — база

requests — это самый популярный модуль Python для работы с HTTP-запросами.
Он используется для общения с веб-серверами, API, микросервисами, DevOps-интеграций (Slack, GitHub, Docker, мониторинг и т.д.).

🔹 Установка
pip install requests

🔹 Импорт
import requests

⚙️ Основные методы
Метод	Назначение
requests.get()	Получить данные с сервера
requests.post()	Отправить данные на сервер
requests.put()	Обновить данные
requests.delete()	Удалить данные
requests.head()	Только заголовки (без тела)
requests.patch()	Частичное обновление данных
📘 Простые примеры
1️⃣ GET-запрос (получение данных)
import requests

response = requests.get("https://api.github.com")

print(response.status_code)   # Код ответа (200, 404, 500)
print(response.headers)       # Заголовки
print(response.text)          # Тело ответа (строка)

2️⃣ GET с параметрами
import requests

params = {"q": "python", "sort": "stars"}
response = requests.get("https://api.github.com/search/repositories", params=params)

print(response.url)      # Полный URL с параметрами
print(response.json())   # Ответ в формате JSON (автоматически преобразован)

3️⃣ POST (отправка данных)
import requests

data = {"username": "walter", "password": "1234"}
response = requests.post("https://httpbin.org/post", data=data)

print(response.json())

4️⃣ Отправка JSON
import requests

payload = {"name": "John", "age": 30}
response = requests.post("https://httpbin.org/post", json=payload)

print(response.json())

5️⃣ Заголовки (headers)
headers = {"Authorization": "Bearer my-token"}
r = requests.get("https://api.example.com/data", headers=headers)

6️⃣ Работа с файлами
files = {"file": open("report.txt", "rb")}
r = requests.post("https://httpbin.org/post", files=files)
print(r.status_code)

7️⃣ Таймаут
r = requests.get("https://example.com", timeout=5)


⚠️ Если сайт не ответит за 5 секунд — requests.exceptions.Timeout

8️⃣ Проверка ошибок
r = requests.get("https://example.com/notfound")

if r.status_code == 404:
    print("Страница не найдена")


или так:

r.raise_for_status()  # выбросит исключение, если код != 200

9️⃣ Сессии (сохранение cookie / headers)
s = requests.Session()
s.headers.update({"User-Agent": "DevOps-Script"})
s.get("https://httpbin.org/cookies/set/sessionid/123")
r = s.get("https://httpbin.org/cookies")
print(r.text)

🔟 Скачивание файла
url = "https://example.com/file.zip"
r = requests.get(url)

with open("file.zip", "wb") as f:
    f.write(r.content)

🧭 Что такое DELETE

DELETE — HTTP-метод для удаления ресурса на сервере (например запись, файл, контейнер).
Важно помнить: поведение сервера зависит от API — обычно DELETE идемпотентен (повторный вызов даёт тот же результат).

Типичные коды ответа:

200 OK — возвращён ответ/тело,

202 Accepted — удаление в очереди/асинхронно,

204 No Content — успешно, тело отсутствует,

401/403 — нет авторизации/доступа,

404 — ресурс не найден.

🔐 Безопасность и нюансы

Многие API НЕ принимают тело (body) в DELETE — проверь спецификацию.

Всегда проверяй права (auth) и CSRF для браузерных вызовов.

На проде обычно делают soft-delete или требуют confirm=true / dry-run флаг.

Используй таймауты и обработку ошибок.

⚙️ Примеры (коротко, рабочие)
1) Простой DELETE по id
import requests

url = "https://api.example.com/items/123"
resp = requests.delete(url, timeout=5)

print(resp.status_code)        # например 204
print(resp.ok)                 # True если код < 400
if resp.status_code == 204:
    print("Удалено успешно (No Content)")
else:
    print(resp.text)           # тело ответа (если есть)

2) DELETE с Bearer-токеном (Authorization header)
import requests

url = "https://api.example.com/items/123"
headers = {"Authorization": "Bearer YOUR_TOKEN"}
resp = requests.delete(url, headers=headers, timeout=5)
resp.raise_for_status()   # выбросит исключение при ошибке

3) DELETE с Basic Auth
from requests.auth import HTTPBasicAuth
import requests

url = "https://api.example.com/resource/45"
resp = requests.delete(url, auth=HTTPBasicAuth("user", "pass"), timeout=5)
print(resp.status_code)

4) DELETE с параметрами (query params), например подтверждение или dry-run
import requests

url = "https://api.example.com/items/123"
params = {"confirm": "true"}   # или dry_run=true
resp = requests.delete(url, params=params, timeout=5)
print(resp.url)    # покажет полный URL с ?confirm=true
print(resp.status_code)

5) DELETE с JSON body (только если API это поддерживает)
import requests

url = "https://api.example.com/bulk-delete"
payload = {"ids": [1, 2, 3]}
# Некоторые API поддерживают тело в DELETE, многие — нет
resp = requests.delete(url, json=payload, timeout=10)
print(resp.status_code, resp.text)

6) Использование Session (повторные запросы, общие заголовки)
import requests

s = requests.Session()
s.headers.update({"Authorization": "Bearer TOKEN", "User-Agent": "monitor/1.0"})

resp = s.delete("https://api.example.com/items/123", timeout=5)
print(resp.status_code)

7) Обработка ошибок и таймаутов
import requests

try:
    resp = requests.delete("https://api.example.com/items/123", timeout=3)
    resp.raise_for_status()
except requests.exceptions.Timeout:
    print("Таймаут при соединении")
except requests.exceptions.HTTPError as e:
    print("HTTP ошибка:", e, resp.status_code)
except requests.exceptions.RequestException as e:
    print("Ошибка запроса:", e)

8) Логгирование результатов (DevOps-паттерн)
import requests, logging

logging.basicConfig(level=logging.INFO)
url = "https://api.example.com/items/123"

resp = requests.delete(url, timeout=5)
if resp.ok:
    logging.info("DELETE %s -> %s", url, resp.status_code)
else:
    logging.error("DELETE %s failed -> %s %s", url, resp.status_code, resp.text)

✅ Краткие рекомендации (чеклист перед DELETE)

Проверь спецификацию API — принимает ли DELETE тело.

Используй авторизацию (headers / auth).

Делай timeout.

Логируй ответ и код возврата.

На продакшне добавь confirm/dry-run или soft-delete.

Обрабатывай исключения (requests.exceptions.RequestException).
