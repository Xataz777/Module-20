import threading  # Импортируем модуль threading для многопоточности
import time  # Импортируем модуль time для измерения времени выполнения
import tracemalloc  # Импортируем модуль tracemalloc для профилирования памяти
import psutil  # Импортируем модуль psutil для получения информации о системе


# Функция для вычисления числа Фибоначчи
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Функция для выполнения вычислений в потоке
def threaded_fibonacci(n, results, index):
    results[index] = fibonacci(n)  # Выполняем вычисление и сохраняем результат


# Основная функция
def threaded_main():
    numbers = [30, 32, 34]  # Список чисел для вычисления
    results = [None] * len(numbers)  # Создаем список для хранения результатов
    threads = []  # Список для хранения потоков

    for i, number in enumerate(numbers):  # Проходим по каждому числу
        thread = threading.Thread(target=threaded_fibonacci,
                                  args=(number, results, i))  # Создаем поток для выполнения функции
        threads.append(thread)  # Добавляем поток в список
        thread.start()  # Запускаем поток

    for thread in threads:  # Ожидаем завершения всех потоков
        thread.join()


def profile_threading_computation():
    # Запуск профилирования памяти
    tracemalloc.start()

    start_time = time.time()  # Начало отсчета времени
    threaded_main()  # Запуск многопоточной функции
    end_time = time.time()  # Окончание отсчета времени

    process = psutil.Process()  # Получение информации о текущем процессе
    mem_usage = process.memory_info().rss / (1024 * 1024)  # Получение использования памяти в МБ

    print("Threading computation time:", end_time - start_time)  # Вывод времени выполнения
    print(f"Memory usage: {mem_usage:.2f} MB")  # Вывод использования памяти


profile_threading_computation()  # Запуск функции профилирования

