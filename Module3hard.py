def depack(item):
    global a
    for i in item:
        if isinstance(i, str):
            a += len(i)
        elif isinstance(i, int):
            a += i
        else:
            if isinstance(i, dict):
                i = tuple(i.items())
            depack(i)
    return a


data_structure = [
    [1, 2, 3],  # list
    {'a': 4, 'b': 5},  # dict
    (6, {'cube': 7, 'drum': 8}),  # set
    "Hello",  # string
    ((), [{(2, 'Urban', ('Urban2', 35))}])  # set
]

a = 0
print(depack(data_structure))
