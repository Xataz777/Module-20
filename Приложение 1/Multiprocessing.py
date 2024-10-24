import multiprocessing  # Импортируем модуль multiprocessing для многопроцессорности
import requests  # Импортируем модуль requests для HTTP-запросов
import time  # Импортируем модуль time для измерения времени выполнения
import tracemalloc  # Импортируем модуль tracemalloc для профилирования памяти
import psutil  # Импортируем модуль psutil для получения информации о системе
import logging  # Импортируем модуль logging для логирования

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Функция для загрузки данных
def fetch(url):
    logging.info(f"Fetching {url}")
    response = requests.get(url)  # Выполняем синхронный GET-запрос
    return response.text  # Возвращаем текст ответа


# Основная функция с использованием пула процессов
def multiprocessing_main(urls):
    num_processes = min(50, len(urls))  # Ограничиваем количество процессов
    logging.info(f"Starting multiprocessing with {num_processes} processes")

    with multiprocessing.Pool(processes=num_processes) as pool:  # Используем пул процессов
        results = pool.map(fetch, urls)  # pool.map автоматически распределяет задачи между процессами

    return results


# Функция профилирования
def profile_multiprocessing():
    urls = ["https://www.example.com"] * 100  # Повторяем URL для теста

    # Запуск профилирования памяти
    tracemalloc.start()

    start_time = time.time()  # Начало отсчета времени
    results = multiprocessing_main(urls)  # Запуск многопроцессорной функции
    end_time = time.time()  # Окончание отсчета времени

    process = psutil.Process()  # Получение информации о текущем процессе
    mem_usage = process.memory_info().rss / (1024 * 1024)  # Получение использования памяти в МБ

    # Логирование времени выполнения и использования памяти
    logging.info(f"Multiprocessing I/O time: {end_time - start_time:.2f} seconds")
    logging.info(f"Memory usage: {mem_usage:.2f} MB")


if __name__ == '__main__':
    profile_multiprocessing()  # Запуск функции профилирования
