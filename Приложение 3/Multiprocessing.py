import multiprocessing  # Импортируем модуль multiprocessing для многопроцессорного выполнения
import time  # Импортируем модуль time для измерения времени выполнения
import tracemalloc  # Импортируем модуль tracemalloc для профилирования использования памяти
import psutil  # Импортируем модуль psutil для получения информации о системе и процессе


# Функция для обработки задачи
def process_task(i):
    time.sleep(0.1)  # Блокирующая задержка на 0.1 секунды


# Основная функция для выполнения задач с использованием multiprocessing
def multiprocessing_main():
    processes = []  # Список для хранения процессов

    for i in range(1000):  # Создаем и запускаем 1000 процессов
        process = multiprocessing.Process(target=process_task, args=(i,))  # Создаем процесс для выполнения задачи
        processes.append(process)  # Добавляем процесс в список
        process.start()  # Запускаем процесс

    for process in processes:  # Ждем завершения всех процессов
        process.join()  # Блокируем выполнение до завершения текущего процесса


# Функция для профилирования многопроцессорного выполнения
def profile_multiprocessing_parallelism():
    tracemalloc.start()  # Начинаем профилирование использования памяти

    start_time = time.time()  # Фиксируем время начала выполнения
    multiprocessing_main()  # Запускаем основную функцию с multiprocessing
    end_time = time.time()  # Фиксируем время завершения выполнения

    process = psutil.Process()  # Получаем информацию о текущем процессе
    mem_usage = process.memory_info().rss / (1024 * 1024)  # Получаем использование памяти в МБ

    print("Multiprocessing parallelism time:", end_time - start_time)  # Выводим время выполнения
    print(f"Memory usage: {mem_usage:.2f} MB")  # Выводим использование памяти


if __name__ == '__main__':
    profile_multiprocessing_parallelism()  # Запускаем функцию профилирования для multiprocessing
