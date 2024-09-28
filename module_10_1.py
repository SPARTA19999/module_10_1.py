# Импорт необходимых модулей и функций
from time import sleep
import threading
from datetime import datetime


# Объявление функции write_words
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунды после записи каждого слова
    print(f"Завершилась запись в файл {file_name}")


def main():
    # Взятие текущего времени перед запуском функций
    start_functions = datetime.now()

    # Запуск функций с аргументами из задачи
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")

    # Взятие текущего времени после выполнения функций
    end_functions = datetime.now()

    # Вывод разницы начала и конца работы функций
    duration_functions = end_functions - start_functions
    print(f"Работа функций {duration_functions}")

    # Взятие текущего времени перед запуском потоков
    start_threads = datetime.now()

    # Создание потоков с аргументами из задачи
    threads = []
    threads.append(threading.Thread(target=write_words, args=(10, "example5.txt")))
    threads.append(threading.Thread(target=write_words, args=(30, "example6.txt")))
    threads.append(threading.Thread(target=write_words, args=(200, "example7.txt")))
    threads.append(threading.Thread(target=write_words, args=(100, "example8.txt")))

    # Запуск всех потоков
    for thread in threads:
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    # Взятие текущего времени после выполнения потоков
    end_threads = datetime.now()

    # Вывод разницы начала и конца работы потоков
    duration_threads = end_threads - start_threads
    print(f"Работа потоков {duration_threads}")


if __name__ == "__main__":
    main()
