"""Заполняем список"""

from random import randint

x = int(input('Введите верхний предел: ', ))
my_list = []
for _ in range(50):
    my_list.append(randint(0, x))

"""Собственно программа ))"""

print(len([i for i in my_list if i % 41 == 0 and i > (sorted(my_list)[0] + sorted(my_list)[-1]) / 2]))
