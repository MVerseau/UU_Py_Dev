class Vehicle:
    vehicle_type = 'none'


class Car:
    price = 1000000

    def horse_powers(self):
        return "1"


class Nissan(Car, Vehicle):
    price = 1000001
    vehicle_type = 'cabriolet'

    def horse_powers(self):
        return '2'


nissan = Nissan()
print(nissan.vehicle_type, nissan.price)
