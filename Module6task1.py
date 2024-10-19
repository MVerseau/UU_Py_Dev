class Car:
    price = 1000000
    horse_power_attr = None

    def horse_power(self):
        return self.horse_power_attr


class Nissan(Car):
    price = 1000001

    def horse_power(self):
        return self.price


class Kia(Car):
    price = 1000002

    def horse_power(self):
        return 'Some horse power'


car = Car()
print(car.__class__.__name__, car.price, car.horse_power())

nissan = Nissan()
print(nissan.__class__.__name__,nissan.price, nissan.horse_power_attr, nissan.horse_power())

kia = Kia()
print(kia.__class__.__name__,kia.price, kia.horse_power_attr, kia.horse_power())
