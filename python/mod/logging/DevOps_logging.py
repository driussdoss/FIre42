🧠 БАЗА ПО МОДУЛЮ logging

Модуль logging — стандартный способ писать сообщения о работе программы:

вместо print()

с уровнями важности

с сохранением в файл или выводом в консоль

можно настраивать формат и уровни логов.

🔹 Основные уровни логирования
Уровень	Назначение	Метод
DEBUG	Отладочная информация (для разработчиков)	logging.debug()
INFO	Обычные события (программа работает штатно)	logging.info()
WARNING	Что-то может пойти не так	logging.warning()
ERROR	Произошла ошибка	logging.error()
CRITICAL	Критическая ошибка (крах приложения)	logging.critical()
🔹 Базовая настройка логирования
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Скрипт запущен")
logging.warning("Что-то может быть не так")
logging.error("Ошибка при выполнении запроса")


📤 Вывод:

INFO:root:Скрипт запущен
WARNING:root:Что-то может быть не так
ERROR:root:Ошибка при выполнении запроса

🔹 Настройка формата
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.debug("Отладка")
logging.info("Запуск программы")
logging.warning("Возможная проблема")


📤 Вывод:

2025-10-08 16:34:21,123 [DEBUG] Отладка
2025-10-08 16:34:21,123 [INFO] Запуск программы
2025-10-08 16:34:21,124 [WARNING] Возможная проблема

🔹 Запись логов в файл
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.info("Программа запущена")
logging.error("Ошибка соединения с БД")


📁 В app.log будет:

2025-10-08 16:36:00 [INFO] Программа запущена
2025-10-08 16:36:05 [ERROR] Ошибка соединения с БД

🔹 Логирование в консоль и файл одновременно
import logging

logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

# Консольный хэндлер
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# Файловый хэндлер
file = logging.FileHandler("myapp.log")
file.setLevel(logging.DEBUG)

# Формат
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console.setFormatter(formatter)
file.setFormatter(formatter)

# Добавляем
logger.addHandler(console)
logger.addHandler(file)

logger.info("Программа стартовала")
logger.debug("Подробная информация для отладки")

🔹 Исключения и логирование ошибок
import logging

logging.basicConfig(level=logging.ERROR)

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Ошибка: деление на ноль")


📤 Выведет стек ошибки:

ERROR:root:Ошибка: деление на ноль
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
