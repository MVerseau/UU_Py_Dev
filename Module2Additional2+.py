from random import randint

x = int(input('Введите верхний предел: ', ))
my_list = []
for _ in range(10000):
    my_list.append(randint(0, x))

list_for_cut_off = [i for i in my_list if i % 5 == 0]
cut_off = sum(list_for_cut_off) / len(list_for_cut_off)
new_list = sorted(my_list)[-1:0:-1]
for i in new_list:
    if i > cut_off:
        print(i ** 0.5, end=', ')
    else:
        break
