import threading  # Импортируем модуль threading для многопоточного выполнения
import time  # Импортируем модуль time для измерения времени выполнения
import tracemalloc  # Импортируем модуль tracemalloc для профилирования использования памяти
import psutil  # Импортируем модуль psutil для получения информации о системе и процессе


# Функция для обработки задачи
def process_task(i):
    time.sleep(0.1)  # Блокирующая задержка на 0.1 секунды


# Основная функция для выполнения задач с использованием threading
def threaded_main():
    threads = []  # Список для хранения потоков

    for i in range(1000):  # Создаем и запускаем 1000 потоков
        thread = threading.Thread(target=process_task, args=(i,))  # Создаем поток для выполнения задачи
        threads.append(thread)  # Добавляем поток в список
        thread.start()  # Запускаем поток

    for thread in threads:  # Ждем завершения всех потоков
        thread.join()  # Блокируем выполнение до завершения текущего потока


# Функция для профилирования многопоточного выполнения
def profile_threading_parallelism():
    tracemalloc.start()  # Начинаем профилирование использования памяти

    start_time = time.time()  # Фиксируем время начала выполнения
    threaded_main()  # Запускаем основную функцию с threading
    end_time = time.time()  # Фиксируем время завершения выполнения

    process = psutil.Process()  # Получаем информацию о текущем процессе
    mem_usage = process.memory_info().rss / (1024 * 1024)  # Получаем использование памяти в МБ

    print("Threading parallelism time:", end_time - start_time)  # Выводим время выполнения
    print(f"Memory usage: {mem_usage:.2f} MB")  # Выводим использование памяти


profile_threading_parallelism()  # Запускаем функцию профилирования для threading
