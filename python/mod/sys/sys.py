###!!!---SYS---!!!###
import sys

print(sys.args) #список аргументов переданных при запуске скрипта

#exit programm

if len(sys.args) < 2:
    print("Ошибка нет аргументов")
    sys.exit(1) #exit with code 1
print("Программа запущена успешно")
sys.exit(0)

#get platform name
print(sys.platform)

#python version
print(sys.version)
print(sys.version_info) #more info

#find path mod
for p in sys.path:
    print(p)

# stdin stdout stderr
sys.stdout.write("stdout!")
sys.stderr.write("error massage")

###!!!---EXAMPLES---!!!###

#обработка аргументов командной строки

# save as hello.py
import sys

if len(sys.argv) < 2:
    print("Использование: python hello.py <имя>")
    sys.exit(1)

name = sys.argv[1]
print(f"Привет, {name}!")

#завершение программы по ошибке
import sys, os

if not os.path.exists("config.yaml"):
    print("Ошибка: нет файла конфигурации")
    sys.exit(1)

#проверка версии в python
import sys

if sys.version_info < (3, 10):
    print("Требуется Python 3.10 или выше")
    sys.exit(1)

#добавление пользовательско библиотеки
import sys
sys.path.append("/home/user/my_utils")

import my_module  # теперь импортируется из добавленного пути

#Разное поведение разных OS
import sys, os

if sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")

