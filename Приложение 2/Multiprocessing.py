import multiprocessing
import time
import tracemalloc
import psutil


# Функция для вычисления числа Фибоначчи
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Функция для выполнения вычислений в процессе
def worker(n, queue):
    result = fibonacci(n)
    queue.put(result)


# Основная функция
def multiprocessing_main():
    numbers = [30, 32, 34]
    queue = multiprocessing.Queue()
    processes = []

    for number in numbers:
        process = multiprocessing.Process(target=worker, args=(number, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = [queue.get() for _ in range(len(numbers))]
    return results


def profile_multiprocessing_computation():
    # Запуск профилирования памяти
    tracemalloc.start()

    start_time = time.time()
    multiprocessing_main()
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print("Multiprocessing computation time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


if __name__ == '__main__':
    profile_multiprocessing_computation()
