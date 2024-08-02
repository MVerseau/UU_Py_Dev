import sqlite3
import random

connection = sqlite3.connect('Module14task4_products.db')
cursor = connection.cursor()


def fill_in_the_table():
    for i in range(random.randint(1, 10)):
        cursor.execute('INSERT INTO Products(id, title, description, price) VALUES (?,?,?,?)',
                       (f'{i}', f'Product{i}', f'Description{i}', f'Price{i * 100}'))
    connection.commit()
    return cursor.execute('SELECT * FROM Products').fetchall()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL);
    ''')
    connection.commit()


def get_all_products():
    initiate_db()
    cursor.execute('SELECT * FROM Products')
    prods = cursor.fetchall()
    #АВТОЗАПОЛНЕНИЕ ПУСТОЙ ТАБЛИЦЫ
    # if len(prods) == 0:
    #     prods = fill_in_the_table()
    return prods

