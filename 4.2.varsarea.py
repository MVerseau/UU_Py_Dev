def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
        # inner_function()  "Бесконечная" рекурсия

    inner_function()


# inner_function() - код "не видит" функцию
test_function()
