# Задача 1. Фабрика Функций

def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y

        return add
    elif operation == "substract":
        def substract(x, y):
            return x - y

        return substract
    # Просто дописано к тому, что в комментарию к заданию
    elif operation == 'multiply':
        def mul(x, y):
            return x * y

        return mul
    elif operation == 'division':
        def div(x, y):
            return x / y

        return div


my_func_add = create_operation("add")
print(my_func_add(1, 2))
my_func_sub = create_operation("substract")
print(my_func_sub(1, 2))
my_func_mul = create_operation("multiply")
print(my_func_mul(1, 2))
my_func_div = create_operation("division")
print(my_func_div(1, 2))

# Задача 2. Лямбда-Функции


sq = lambda x, y: (x ** 2, y ** 2)


def sq_f(x, y):
    return x ** 2, y ** 2


print(sq(3, 4))
print(sq_f(3, 4))


# Задача 3. Вызываемые Объекты

class Rect():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


rect = Rect(3, 4)
print(rect())


