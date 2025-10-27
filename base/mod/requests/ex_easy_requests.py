🟢 10 ПРОСТЫХ ЗАДАЧ (основы работы с requests + DELETE)

Цель — понять, как делать разные типы HTTP-запросов и работать с ответами.

GET-запрос
Получи https://httpbin.org/get и выведи статус-код и JSON-ответ.

POST-запрос с данными
Отправь POST https://httpbin.org/post с data={"name": "devops"}
и выведи значение поля "form" из ответа.

POST с JSON
Отправь JSON {"service": "nginx", "status": "running"}
и выведи поле "json" из ответа.

GET с параметрами
Сделай запрос https://httpbin.org/get?env=prod&region=eu
и выведи конечный URL (response.url).

DELETE-запрос простой
Удали тестовый ресурс: DELETE https://httpbin.org/delete
→ выведи "deleted" если статус 200.

DELETE с параметрами
Выполни DELETE https://httpbin.org/delete?confirm=true
→ выведи "confirmed delete" если статус 200.

GET с пользовательским заголовком
Добавь заголовок "User-Agent": "DevOpsScript/1.0"
и выведи "headers" из JSON-ответа.

POST и DELETE последовательно
Сначала сделай POST https://httpbin.org/post с JSON {"file": "temp"},
затем DELETE https://httpbin.org/delete — выведи оба статуса.

Проверка 404
GET https://httpbin.org/status/404
→ если не 200, выведи "Not Found".

Обработка таймаута
Попробуй GET https://httpbin.org/delay/5 с timeout=2
→ обработай requests.exceptions.Timeout.
