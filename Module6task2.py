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
print(nissan.vehicle_type, nissan.price, nissan.horse_powers(),'- атрибуты и методы экземпляра класса Nissan.')
print(Nissan.vehicle_type, Nissan.price, Nissan.horse_powers(Nissan),'- атрибуты и методы класса Nissan.')
print(Car.price, Car.horse_powers(Car),'- атрибуты и методы класса Nissan, атрибута "vehicle_type" у него нет.')
print(Vehicle.vehicle_type, f'({type(Vehicle.vehicle_type)})','- атрибуты и методы класса Nissan, атрибута "price" и "horse_powers" у него нет.')

