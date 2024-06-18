from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            self.days += 1
            self.enemies -= self.skill
            print(f'{self.name} сражается {self.days} день (дня)..., осталось {self.enemies} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {self.days} дней!')


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!\n')

for knight in (knight1, knight2):
    print(f'{knight.name} понадобилось {knight.days} дней, чтобы победить 100 воинов.')
