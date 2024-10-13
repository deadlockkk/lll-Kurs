import threading as thr
import time

EVENT = thr.Event()    # Создаем объект события


def producer():    # Функция потока-поставщика
    while True:
        print("Thread(producer): Initializing the event")
        EVENT.set()    # Устанавливаем событие
        time.sleep(1)


def consumer():    # ункция потока-потребителя
    while True:
        print("Thread(consumer): Waiting for the event")
        EVENT.wait()    # Ожидаем событие
        EVENT.clear()    # Сбрасываем наше событие
        print("Thread(consumer): Got the event")

# Создаем и запускаем потоки
PRODUCER_THREAD = thr.Thread(target=producer)
CONSUMER_THREAD = thr.Thread(target=consumer)

PRODUCER_THREAD.start()
CONSUMER_THREAD.start()

# Чтобы завершить программу, можно использовать KeyboardInterrupt (Ctrl+C)
try:
    PRODUCER_THREAD.join()
    CONSUMER_THREAD.join()
except KeyboardInterrupt:
    print("End of program")
