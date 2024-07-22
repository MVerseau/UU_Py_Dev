import asyncio


async def start_strongman(name, power):
    balls = 0
    print(f'Силач {name} начал соревнования.')
    while balls <= 5:
        balls += 1
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {balls}')
    print(f'Силач {name} закончил соревнование')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('A', 5))
    task2 = asyncio.create_task(start_strongman('B', 3))
    task3 = asyncio.create_task(start_strongman('C', 1))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
