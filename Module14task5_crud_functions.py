import sqlite3
import random

connection = sqlite3.connect('Module14task5_products.db')
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
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL);
    ''')
    connection.commit()


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username,email,age, balance) VALUES (?,?,?,?)', (username, email, age, 1000))
    connection.commit()


def is_included(username):
    user_exists = cursor.execute('SELECT username FROM Users WHERE username=?', (username,)).fetchall()
    connection.commit()
    return True if len(user_exists) > 0 else False


def get_all_products():
    initiate_db()
    cursor.execute('SELECT * FROM Products')
    prods = cursor.fetchall()
    # АВТОЗАПОЛНЕНИЕ ПУСТОЙ ТАБЛИЦЫ
    # if len(prods) == 0:
    #     prods = fill_in_the_table()
    return prods
