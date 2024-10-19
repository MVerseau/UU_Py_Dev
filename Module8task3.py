class InvalidDataException(Exception):
    def __init__(self):
        self.name = self.__class__.__name__


class ProcessingException(Exception):
    def __init__(self):
        self.name = self.__class__.__name__


def f(a: str, b: int, c=0):
    try:
        if not isinstance(b, (float, int)) or not isinstance(a, str) or not isinstance(c, (int, float)):
            raise InvalidDataException
        elif c == 0 or c > len(a):
            raise ProcessingException
    except ProcessingException as pe:
        return f'{pe.name}: деление на ноль невозможно либо строка слишком короткая.'
    except InvalidDataException as ide:
        return f'{ide.name}: неправильный тип данных.'
    else:
        return b / c, a[-c:]
    finally:
        print('Результат обработки:')


print(f('kzkz', 4, 5))
