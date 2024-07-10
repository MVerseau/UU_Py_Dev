import multiprocessing


class ContentError(Exception):
    def __init__(self, product):
        self.message = f"No {product} can be shipped."

    def __str__(self):
        return self.message


class WarehouseManager(multiprocessing.Process):
    def __init__(self):
        # super().__init__()
        self.data = dict()

    def run(self, requests):
        with multiprocessing.Pool(processes=len(requests)) as pool:
            pool.map(self.process_request, requests)

    def process_request(self, request):

        if request[1] in self.data or self.data[request[1]]==0:
            print(f"No {request[1]} can be shipped.")
        elif request[1] == 'receipt':
            self.data.setdefault([request[0]], request[2])
            print(self.data)
        elif request[1] == 'shipment':
            print(self.data)
            if self.data[request[0]] >= request[2]:
                self.data[request[0]] -= request[2]
            elif 0 < self.data[request[0]] < request[2]:
                print(f"Only {self.data[request[0]]} can be shipped.")


# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
if __name__ == '__main__':
    manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)
