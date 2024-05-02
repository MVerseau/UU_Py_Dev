import random

end_ = 20
parol = ''
n = random.randint(3, end_)

for i in range(1, n):
    for j in range(i, n):
        if i!=j and n % (i + j) == 0:
            parol = parol + str(i) + str(j)

print(f'{n} - {parol}')
