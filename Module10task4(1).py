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
        self.tables_lock = threading.Lock()

    def mock_thread(self):
        time.sleep(3)
        while True:
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

            #for table in self.tables:
             #   print(f'{table}.is_busy {table.is_busy}')
            #print(f'all tables are busy {all([table.is_busy for table in tables])}')
            self.queue.put(c)
            time.sleep(1)
        self.queue.put(None)

    def serve_customer(self, customer):
        if all([table.is_busy for table in self.tables]):  # False

            event.clear()
            print(f'Посетитель номер {customer.name} ожидает свободный стол.')
            # time.sleep(3)
            event.wait()


        for table in self.tables:

            if not table.is_busy:

                table.is_busy = True
                event.clear()
                print(f'Посетитель номер {customer.name} сел за стол {table.number}.')
                time.sleep(5)
                print(f'Посетитель номер {customer.name} покушал и ушёл.')

                table.is_busy = False
                event.set()
                break


class Customer(threading.Thread):
    def __init__(self, func):
        super().__init__()
        self.func = func

    def run(self):
        self.func(self)


event = threading.Event()
event.set()

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
