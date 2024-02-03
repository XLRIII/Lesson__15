# Создайте функцию генератор чисел Фибоначчи
# Добавить логирование ошибок и полезной информации.
# Также реализовать возможность запуска из командной строки с передачей параметров.

import logging
import argparse

def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def main():
    parser = argparse.ArgumentParser(description="Сгенерируйте последовательность Фибоначчи.")
    parser.add_argument("n", type=int, help="Количество чисел Фибоначчи для генерации.")
    args = parser.parse_args()

    try:
        fibonacci = fibonacci_generator(args.n)
        result = list(fibonacci)
        logging.info(f"Последовательность Фибоначчи для n={args.n}: {result}")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        raise


if __name__ == "__main__":
    # Настройка логгера
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    # Запуск программы
    main()

# Команда для ввода в консоль (пример)
# python Task2.py 8