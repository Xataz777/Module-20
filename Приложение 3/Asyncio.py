import asyncio  # Импортируем модуль asyncio для асинхронного программирования
import time  # Импортируем модуль time для измерения времени выполнения
import tracemalloc  # Импортируем модуль tracemalloc для профилирования использования памяти
import psutil  # Импортируем модуль psutil для получения информации о системе и процессе


# Блокирующая функция для обработки задачи
def blocking_task(i):
    time.sleep(0.1)  # Блокирующая задержка на 0.1 секунды
    return i  # Возвращаем значение i после выполнения задачи


# Асинхронная функция для выполнения блокирующих задач
async def async_main():
    loop = asyncio.get_event_loop()  # Получаем текущий событийный цикл
    # Запуск 1000 задач в блокирующем режиме через executor
    tasks = [loop.run_in_executor(None, blocking_task, i) for i in range(1000)]
    return await asyncio.gather(*tasks)  # Ожидаем завершения всех задач и собираем результаты


# Функция для профилирования асинхронного выполнения с блокирующими задачами
def profile_asyncio_parallelism():
    tracemalloc.start()  # Начинаем профилирование использования памяти

    start_time = time.time()  # Фиксируем время начала выполнения
    asyncio.run(async_main())  # Запускаем асинхронную функцию с блокирующими задачами
    end_time = time.time()  # Фиксируем время завершения выполнения

    process = psutil.Process()  # Получаем информацию о текущем процессе
    mem_usage = process.memory_info().rss / (1024 * 1024)  # Получаем использование памяти в МБ

    print("Asyncio (blocking) parallelism time:", end_time - start_time)  # Выводим время выполнения
    print(f"Memory usage: {mem_usage:.2f} MB")  # Выводим использование памяти


profile_asyncio_parallelism()  # Запускаем функцию профилирования для asyncio
