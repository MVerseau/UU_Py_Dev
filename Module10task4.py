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

        self.cstrs_lock = threading.Lock()
        self.tables_lock = threading.Lock()

    def customer_arrival(self):  # функция-producer
        for i in range(1, 21):
            time.sleep(1)
            c = Customer(func=self.serve_customer)
            c.name = f'{i}'
            print(f'Посетитель номер {c.name} прибыл.')
            c.start()
            # self.queue.put(c)



    def serve_customer(self, customer):  # функция-customer #FIXME: Зациклился - приходит и есть только посетитель 1

        if all([table.is_busy for table in tables]):  # False
            print(f'Посетитель номер {customer.name} ожидает свободный стол.')
            event.clear()
            event.wait()
        for table in self.tables:

            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель номер {customer.name} сел за стол {table.number}.')
                time.sleep(5)
                table.is_busy = False
                # self.queue.task_done()
                event.set()
                print(f'Посетитель номер {customer.name} покушал и ушёл.')

                break
        # print(f'Количество потоков {threading.active_count()}')
        # self.queue.join()


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
