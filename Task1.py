# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Добавить логирование ошибок и полезной информации.
# Также реализовать возможность запуска из командной строки с передачей параметров.

import os
import logging
import argparse


def split_file_path(file_path):
    try:
        # Используем os.path для разделения пути, имени файла и расширения
        path, file_name = os.path.split(file_path)
        name, extension = os.path.splitext(file_name)

        return path, name, extension
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(description="Разделите путь к файлу на путь, имя файла и расширение.")
    parser.add_argument("file_path", help="Абсолютный путь к файлу.")
    args = parser.parse_args()

    try:
        result = split_file_path(args.file_path)
        logging.info("Путь файла успешно разделен.")
        logging.info(f"Путь: {result[0]}, Имя: {result[1]}, Расширение: {result[2]}")
    except Exception as e:
        logging.error(f"Не удалось разделить путь к файлу: {e}")


if __name__ == "__main__":
    # Настройка логгера
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    # Запуск программы
    main()

# Пример кода, для командной строки:
# python Task1.py /GeekBrains/Python_Lessons/Lessons15/Test.py
