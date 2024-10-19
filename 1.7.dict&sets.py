my_list = ['apple', 'orange', 'banana', 'lemon', 'plum', 'pear', 'peach']
print('List: ', my_list)
print('First element: ' + my_list[0], 'Last element: ' + my_list[-1], sep='\n')
print('Sublist: ', my_list[2:4])
my_list[2] = 'grape'
print('Modified list: ', my_list)

my_dict = {'boy': 'мальчик', 'girl': 'девочка', 'man': 'мужчина', 'woman': 'женщина'}
print(my_dict, my_dict['girl'], sep='\n')
my_dict['man'] = 'мужчина, человек'
print(my_dict)
