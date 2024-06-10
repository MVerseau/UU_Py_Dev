from sys import getsizeof


class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = self.__start__(start)
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.start + 2 <= self.end:
            self.start += 2
            return self.start
        raise StopIteration

    def __start__(self, start):
        self.start = start - 1 if start % 2 else start
        return self.start - 2


en = EvenNumbers(10, 25)

for i in en:
    print(i)
