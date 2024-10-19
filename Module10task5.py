import multiprocessing


class WarehouseManager(multiprocessing.Process):
    def __init__(self):
        self.data = dict()

    def run(self, requests):
        with multiprocessing.Pool(processes=len(requests)) as pool:
            for item in pool.map(self.process_request, requests):
                self.data[item[0]] = self.data.setdefault(item[0], 0) + item[1]

    def process_request(self, request):
        if request[1] == 'receipt':
            return request[0], request[2]
        elif request[1] == 'shipment':
            return request[0], -request[2]

    # Плохочитаемый вариант метода
    # def process_request(self, request):
    # return request[0], request[2] * [1, -1][['receipt', 'shipment'].index(request[1])]


# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
if __name__ == '__main__':
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)
