def test(seps="It's seps param", *args, **kwargs):
    print(seps, *args, *kwargs.items(), sep='\n')
    for k, v in kwargs.items():
        print(f'{k}: {v}')


test('Changed seps param', 1, 2, 3, 4, 5, 6, name='Me', age=None, title=True)


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# for i in range(0, int(input('До какого числа Вы хотите вывести факториал? ')) + 1):
#     print(f'{i}! = {factorial(i)}')

print(factorial(int(input())))
