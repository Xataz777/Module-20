import asyncio  # Импортируем модуль asyncio для асинхронного программирования
import time  # Импортируем модуль time для измерения времени выполнения
import tracemalloc  # Импортируем модуль tracemalloc для профилирования памяти
import psutil  # Импортируем модуль psutil для получения информации о системе


# Функция для вычисления числа Фибоначчи
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Асинхронная функция для выполнения вычислений
async def async_fibonacci(n):
    loop = asyncio.get_event_loop()  # Получаем текущий событийный цикл
    return await loop.run_in_executor(None, fibonacci, n)  # Выполняем вычисление в отдельном потоке


# Основная асинхронная функция
async def async_main():
    numbers = [30, 32, 34]  # Список чисел для вычисления
    tasks = [async_fibonacci(n) for n in numbers]  # Создаем задачи для вычисления
    return await asyncio.gather(*tasks)  # Запускаем все задачи параллельно и ждем их завершения


def profile_asyncio_computation():
    # Запуск профилирования памяти
    tracemalloc.start()

    start_time = time.time()  # Начало отсчета времени
    asyncio.run(async_main())  # Запуск асинхронной функции
    end_time = time.time()  # Окончание отсчета времени

    process = psutil.Process()  # Получение информации о текущем процессе
    mem_usage = process.memory_info().rss / (1024 * 1024)  # Получение использования памяти в МБ

    print("Asyncio computation time:", end_time - start_time)  # Вывод времени выполнения
    print(f"Memory usage: {mem_usage:.2f} MB")  # Вывод использования памяти


profile_asyncio_computation()  # Запуск функции профилирования
