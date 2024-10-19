def euclides(L):
    NOD_list = []

    def euclides_rec(a, b):
        if a % b == 0:
            NOD_list.append(b)
        else:
            euclides_rec(b, a % b)
        return NOD_list

    for i in L:
        euclides_rec(i[0], i[1])

    print(*NOD_list, sep=', ')


euclides([[5, 7], [21, 111], [63, 49]])
