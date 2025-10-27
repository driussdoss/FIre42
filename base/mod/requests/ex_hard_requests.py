🔴 10 СЛОЖНЫХ ЗАДАЧ (реальные DevOps-примеры с DELETE)

Цель — использовать requests в типичных сценариях DevOps: CI/CD, мониторинг, API-интеграции.

Health-check сервисов
Напиши функцию check_services(urls),
возвращающую доступные сервисы (status_code == 200).
Используй logging для логирования.

Создание ресурса и его удаление

Создай запись POST https://httpbin.org/post {"job": "backup"}

После успешного создания вызови DELETE https://httpbin.org/delete.
Выведи "Job removed" если оба успешны.

Slack webhook уведомление
Отправь POST на https://httpbin.org/post
с JSON: {"text": "✅ Deploy complete"}
(имитируем Slack).

DELETE c подтверждением dry-run
Напиши функцию safe_delete(url, dry_run=True) —
если dry_run=True → просто печатай "would delete"
иначе выполняй реальный requests.delete().

Проверка статуса GitHub API
GET https://api.github.com
→ если не 200, отправь POST в Slack/webhook с ошибкой.

Очистка временных данных через API
Удали данные: DELETE https://httpbin.org/delete?type=temp
→ логируй дату и результат в cleanup.log.

CI/CD отчёт о деплое
POST на https://httpbin.org/post с JSON:
{"pipeline": "build_42", "status": "success"}
→ при неудаче DELETE https://httpbin.org/delete?rollback=true.

Мониторинг API
Циклом каждые 10 секунд проверяй GET https://httpbin.org/status/200
→ если статус != 200 → шли POST "service down".

Массовое удаление
Отправь DELETE https://httpbin.org/delete
с JSON: {"ids": [1,2,3,4,5]}
→ выведи результат и логируй в файл.

Prometheus pushgateway интеграция
После успешного DELETE на API
отправь POST на http://localhost:9091/metrics/job/cleanup
с метрикой:

cleanup_success 1
cleanup_duration 3.7


