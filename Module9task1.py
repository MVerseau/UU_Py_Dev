# Нечетные квадраты чисел
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]))))

# Квадраты нечетных чисел
print(list(filter(lambda x: x % 2 != 0, map(lambda x: x ** 2, [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]))))


