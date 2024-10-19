import queue
import threading
import time


class Table:
    def __init__(self, number: int, is_busy: bool = False):
        self.number = number
        self.is_busy = is_busy


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.queue_lock = threading.Lock()

    def mock_thread(self):
        time.sleep(len(self.tables)+0.1)
        while True:
            if not all([table.is_busy for table in self.tables]):
                # with self.queue_lock:
                customer = self.queue.get()
                if customer is None:
                    break
                customer.start()
                customer.join(1)

    def customer_arrival(self):  # функция-producer
        threading.Thread(target=self.mock_thread).start()
        for i in range(1, 21):
            c = Customer(func=self.serve_customer)
            c.name = f'{i}'
            print(f'Посетитель номер {c.name} прибыл.')
            if not all([table.is_busy for table in self.tables]) and self.queue.empty():  # False
                c.start()
                time.sleep(1)
            else:
                print(f'Посетитель номер {c.name} ожидает свободный стол.')
                with self.queue_lock:
                    self.queue.put(c)
                time.sleep(1)

        self.queue.put(None)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель номер {customer.name} сел за стол {table.number}.')
                time.sleep(5)
                print(f'Посетитель номер {customer.name} покушал и ушёл.')
                table.is_busy = False
                break


class Customer(threading.Thread):
    def __init__(self, func):
        super().__init__()
        self.func = func

    def run(self):
        self.func(self)


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
