import multiprocessing


class ContentError(Exception):
    def __init__(self):
        self.message = f"No {self.data[request[1]]} can be shipped."

    def __str__(self):
        return self.message


class WarehouseManager(multiprocessing.Process):
    def __init__(self):
        super().__init__()
        self.data = dict()

    def run(self, requests):
        for request in requests:
            multiprocessing.Process(target=self.process_request, args=(request,)).start()

    def process_request(self, request):
        try:
            if request[0] == 'receipt':
                self.data[request[1]] = request[2]
            elif request[0] == 'shipment':
                if self.data[request[1]] >= request[2]:
                    self.data[request[1]] -= request[2]
                elif 0 < self.data[request[1]] < request[2]:
                    print(f"Only {self.data[request[1]]} can be shipped.")
                else:
                    raise ContentError
        except:
            raise ContentError


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
if __name__=='__main__':
    manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)
