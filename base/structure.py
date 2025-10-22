#!/usr/bin/env python3 
# 1. Shebang: Указывает интерпретатор

# 2. Импорты
import boto3
import sys

def main(num_a, num_b):
    """
    3. Функция main: Вся логика здесь.
    """
    # ... логика сравнения, работа с AWS, анализ логов ...
    print(f"Обработка чисел: {num_a} и {num_b}")
    return num_a + num_b

# 4. Точка входа
if __name__ == "__main__":
    # Код, который выполнится ТОЛЬКО при прямом запуске скрипта
    try:
        main(a=15, b=20)
    except Exception as e:
        # Обработка ошибок верхнего уровня
        print(f"Скрипт завершился с ошибкой: {e}")
        sys.exit(1)
