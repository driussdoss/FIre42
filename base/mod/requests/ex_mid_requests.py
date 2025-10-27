🟡 10 СРЕДНИХ ЗАДАЧ (работа с API, авторизация, сессии, DELETE)

Цель — освоить практическую работу с API, cookies и авторизацией.

Работа с сессией
Через requests.Session():

Установи cookie https://httpbin.org/cookies/set/id/123,

Проверь https://httpbin.org/cookies, выведи значение "id".

API GitHub — список репозиториев
Получи GET https://api.github.com/users/torvalds/repos
→ выведи первые 5 имён.

Создание и удаление ресурса (симуляция)
POST https://httpbin.org/post c JSON {"user": "test"},
затем DELETE https://httpbin.org/delete
→ если оба кода 200, выведи "OK".

DELETE с токеном
Выполни DELETE https://httpbin.org/delete
с заголовком "Authorization": "Bearer 12345",
→ проверь статус-код.

PUT (обновление данных)
Отправь PUT https://httpbin.org/put с json={"config": "updated"}
→ выведи "json" из ответа.

Авторизация (Basic Auth)
Проверь GET https://httpbin.org/basic-auth/admin/1234
с auth=("admin", "1234").

POST и DELETE с логированием
Используй модуль logging:
логируй статусы обоих запросов.

DELETE c телом JSON
DELETE https://httpbin.org/delete с json={"id": 77}
→ выведи "json" из ответа.

HEAD-запрос
Сделай HEAD https://httpbin.org/get и выведи только заголовки.

Проверка списка URL
Для списка ["https://google.com", "https://nosite123.com"]:
выведи "OK" или "FAIL" для каждого.
