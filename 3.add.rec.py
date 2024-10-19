# def depack(item):
#     global a
#     # print(item)
#     for i in item:
#         # print(i)
#         if isinstance(i,str):
#             a+=len(i)
#             # print (f'a+i={a+len(i)}')
#         elif isinstance(i,int):
#             a+=i
#             # print(f'a+i={a + i}')
#         else:
#             # print('to be depacked')
#             if isinstance(i,dict):
#                 # print(f'{i} is dict')
#                 i=tuple(i.items())
#             depack(i)
#     return a
#
# data_structure = [
#     [1, 2, 3], #list
#     {'a': 4, 'b': 5}, #dict
#     (6, {'cube': 7, 'drum': 8}), #set
#     "Hello", #string
#     ((), [{(2, 'Urban', ('Urban2', 35))}]) #set
# ]
#
# a=0
# print(depack(data_structure))

def depack(item, a):
    # global a
    # print(item)
    for i in item:
        # print(i)
        if isinstance(i, str):
            a += len(i)
            # print (f'a+i={a+len(i)}')
        elif isinstance(i, int):
            a += i
            # print(f'a+i={a + i}')
        else:
            # print('to be depacked')
            if isinstance(i, dict):
                # print(f'{i} is dict')
                i = tuple(i.items())
            print(a)
            depack(i, a)

    return a


data_structure = [
    [1, 2, 3],  # list
    {'a': 4, 'b': 5},  # dict
    (6, {'cube': 7, 'drum': 8}),  # set
    "Hello",  # string
    ((), [{(2, 'Urban', ('Urban2', 35))}])  # set
]

a = 0
print(depack(data_structure, a))
