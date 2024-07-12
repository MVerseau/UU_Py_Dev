class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории.')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return True if self.number_of_floors == other.number_of_floors else False

    def __lt__(self, other):
        return True if self.number_of_floors < other.number_of_floors else False

    def __le__(self, other):
        return True if self.number_of_floors <= other.number_of_floors else False

    def __gt__(self, other):
        return True if self.number_of_floors > other.number_of_floors else False

    def __ge__(self, other):
        return True if self.number_of_floors >= other.number_of_floors else False

    def __ne__(self, other):
        return True if self.number_of_floors != other.number_of_floors else False

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def go_to(self, new_floor):
        if 1 > new_floor or new_floor > self.number_of_floors:
            print('"Такого этажа не существует"')
        else:
            for i in range(1, new_floor + 1):
                print(i)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
