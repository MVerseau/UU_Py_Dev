class Buiding:

    def __init__(self, floor=1, buildingType=None):
        self.numberOfFloors = int()
        self.buildingType = str()
        if floor:
            self.numberOfFloors = floor
            self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType==other.buildingType

                                                    

my_build = Buiding(floor=6)
one_build = Buiding(floor=6)

if my_build == one_build:
    print('ok')
