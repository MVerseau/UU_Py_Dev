class House:

    def __init__(self):
        self.numberOfFloors = 0

    def __setNewNumberOfFloors__(self, floors):
        self.numberOfFloors = floors
        return self.numberOfFloors

        # print(self.numberOfFloors) (см. строку 17 кода)


house = House()

print(house.__setNewNumberOfFloors__(22))

# house.__setNewNumberOfFloors__(22)
