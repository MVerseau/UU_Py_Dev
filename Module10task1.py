from threading import Thread
from time import sleep


def interv(start, end):
    if isinstance(start, str):
        for i in range(ord(start), ord(end) + 1):
            print(chr(i))
            sleep(1)
    else:
        for i in range(start, end + 1):
            print(i)
            sleep(1)


t1 = Thread(target=interv, kwargs=dict(start=1, end=10))
t2 = Thread(target=interv, kwargs=dict(start='a', end='j'))

t1.start()
t2.start()
t1.join()
t2.join()
