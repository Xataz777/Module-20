import threading  # Импортируем модуль threading для многопоточности
import requests  # Импортируем модуль requests для HTTP-запросов
import time  # Импортируем модуль time для измерения времени выполнения
import tracemalloc  # Импортируем модуль tracemalloc для профилирования памяти
import psutil  # Импортируем модуль psutil для получения информации о системе


# Функция для загрузки данных
def fetch(url, results, index):
    response = requests.get(url)  # Выполняем синхронный GET-запрос
    results[index] = response.text  # Сохраняем текст ответа в список


# Основная функция
def threaded_main(urls):
    results = [None] * len(urls)  # Создаем список для хранения результатов
    threads = []  # Список для хранения потоков

    for i, url in enumerate(urls):  # Проходим по каждому URL
        thread = threading.Thread(target=fetch, args=(url, results, i))  # Создаем поток для выполнения функции
        threads.append(thread)  # Добавляем поток в список
        thread.start()  # Запускаем поток

    for thread in threads:  # Ожидаем завершения всех потоков
        thread.join()


def profile_threading():
    urls = ["https://www.example.com"] * 100  # Повторяем URL для теста

    # Запуск профилирования памяти
    tracemalloc.start()

    start_time = time.time()  # Начало отсчета времени
    threaded_main(urls)  # Запуск многопоточной функции
    end_time = time.time()  # Окончание отсчета времени

    process = psutil.Process()  # Получение информации о текущем процессе
    mem_usage = process.memory_info().rss / (1024 * 1024)  # Получение использования памяти в МБ

    print("Threading I/O time:", end_time - start_time)  # Вывод времени выполнения
    print(f"Memory usage: {mem_usage:.2f} MB")  # Вывод использования памяти


profile_threading()  # Запуск функции профилирования
