import asyncio  # Импортируем модуль asyncio для асинхронного программирования
import aiohttp  # Импортируем модуль aiohttp для асинхронных HTTP-запросов
import time  # Импортируем модуль time для измерения времени выполнения
import tracemalloc  # Импортируем модуль tracemalloc для профилирования памяти
import psutil  # Импортируем модуль psutil для получения информации о системе


# Асинхронная функция для загрузки данных
async def fetch(url):
    async with aiohttp.ClientSession() as session:  # Создаем асинхронную сессию HTTP
        async with session.get(url) as response:  # Выполняем асинхронный GET-запрос
            return await response.text()  # Возвращаем текст ответа


# Основная асинхронная функция
async def async_main(urls):
    tasks = [fetch(url) for url in urls]  # Создаем список задач для загрузки данных
    return await asyncio.gather(*tasks)  # Запускаем все задачи параллельно и ждем их завершения


# Функция для профилирования выполнения
def profile_asyncio():
    urls = ["https://www.example.com"] * 100  # Повторяем URL для теста

    # Запуск профилирования памяти
    tracemalloc.start()

    start_time = time.time()  # Начало отсчета времени
    asyncio.run(async_main(urls))  # Запуск асинхронной функции
    end_time = time.time()  # Окончание отсчета времени

    process = psutil.Process()  # Получение информации о текущем процессе
    mem_usage = process.memory_info().rss / (1024 * 1024)  # Получение использования памяти в МБ

    print("Asyncio I/O time:", end_time - start_time)  # Вывод времени выполнения
    print(f"Memory usage: {mem_usage:.2f} MB")  # Вывод использования памяти


profile_asyncio()  # Запуск функции профилирования
