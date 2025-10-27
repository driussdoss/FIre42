🧩 МОДУЛЬ subprocess в Python — краткая база

Модуль subprocess нужен, чтобы выполнять системные команды (как в bash)
и работать с их результатом (stdout, stderr, код выхода и т.п.).

📘 Основные функции
Функция	Назначение	Пример
subprocess.run()	Запускает команду и ждёт завершения	subprocess.run(["ls", "-l"])
subprocess.check_output()	Выполняет команду и возвращает stdout	out = subprocess.check_output(["whoami"])
subprocess.Popen()	Запускает процесс и позволяет работать с ним во время выполнения	proc = subprocess.Popen(["ping", "8.8.8.8"])
subprocess.DEVNULL	Подавляет вывод	subprocess.run(["ls"], stdout=subprocess.DEVNULL)
subprocess.PIPE	Захватывает stdout/stderr для обработки	subprocess.run(["ls"], stdout=subprocess.PIPE)

⚙️ Ключевые параметры
Аргумент	Что делает
capture_output=True	Захватывает stdout и stderr
text=True	Преобразует байты в строку
check=True	Бросает ошибку, если код возврата ≠ 0
shell=True	Выполняет через оболочку (sh, bash) — нужно осторожно!

🔹 Примеры
1. Простая команда
import subprocess
subprocess.run(["ls", "-l"])

2. Захват вывода
import subprocess
result = subprocess.run(["whoami"], capture_output=True, text=True)
print(result.stdout)

3. Проверка кода возврата
r = subprocess.run(["ping", "-c", "1", "8.8.8.8"])
if r.returncode == 0:
    print("OK")
else:
    print("Ошибка")

4. Получение только вывода (коротко)
out = subprocess.check_output(["pwd"], text=True)
print(out)

5. Подавление вывода
subprocess.run(["ls"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

