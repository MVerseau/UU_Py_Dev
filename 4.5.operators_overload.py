class Buiding:

    def __init__(self, floor=1):
        self.numberOfFloors = int()
        self.buildingType = str()
        if floor:
            self.numberOfFloors = int(floor)
            self.buildingType = str(floor)

    def __eq__(self, other):
        # return self.numberOfFloors == other.numberOfFloors
        return self.buildingType == other.buildingType


my_build = Buiding(floor=10)
one_build = Buiding(floor=6)

if my_build == one_build:
    print('ok')
