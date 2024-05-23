for i in [[5, 7], [21, 111], [63, 49]]:
    a = i[0]
    b = i[-1]
    while a % b != 0:
        c = a % b
        a, b = b, c
    print(c)
