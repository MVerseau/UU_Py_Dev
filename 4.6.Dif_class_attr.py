class Buiding:
    total=0

    def __init__(self):
        Buiding.total+=1

for i in range(40):
    my_build = Buiding()
    print(Buiding.total)

print(f'Всего объектов Buiding {Buiding.total} штук.')