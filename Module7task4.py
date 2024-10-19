import os
import time

directory=input('Введите адрес папки (директории): ')
for root, dirs, files in os.walk(directory):
    for file in files:

        full_path=os.path.join(root,file)
        filetime=time.gmtime(os.path.getmtime(full_path))
        human_time=time.strftime('%d.%m.%Y %H:%M',filetime)
        filesize=os.path.getsize(full_path)
        dir_name=os.path.dirname(full_path)
        print(f'Обнаружен файл {file}, путь: {full_path}, размер {filesize} байт, время изменения: {human_time}, родительская директория: {os.path.dirname(full_path)}')
        break


# print(*os.walk(directory))
# filename=input('Введите имя файла: ')
# full_path=os.path.join(input('Введите адрес папки, где находится файл: '),filename)
# print(f'Полный адрес файла: {full_path}')
# time_=time.gmtime(os.path.getmtime(full_path))
# print(f'Время с момента последнего изменения {os.path.getmtime(full_path)} сек., т.е. {time_.tm_mday}.{time_.tm_mon}.{time_.tm_year}')
# print(f'Размер файла в байтах: {os.path.getsize(full_path)}')
# print(f'Файл находится в папке: {os.path.dirname(full_path)}')

