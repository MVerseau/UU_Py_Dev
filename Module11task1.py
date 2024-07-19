'''Программа визуализирует и помещает в файл данные по динамике изменений ключевой ставки ЦБ РФ за выбранный период.

Ошибки не обрабатывались. Соотвественно, если введённые даты будут выходить за пределы того периода, который есть
на сайте, программа вернёт ошибку и завершит работу. Программа также вернёт ошибку и завершит работу, если конечная дата
диапазона окажется меньше начальной.

При выборе диапазона конечную дату можно опустить - по умолчанию будет взята системная дата отправки запроса.

В программе использовано более 3 библиотек, часть из которых не были упомянуты в задании, но без них невозможно
было бы обработать данные (запрос на сайт, обработка результата запроса, дальнейшая обработка для визуализации и т.п.)

Чем больше выбран период, тем дольше (что очевидно) работает программа. Это можно было бы решить потоками, но
данная работа не имеет целью ускорение процесса обработки, поэтому не стала её "утяжелять" еще одной библиотекой.
'''
import datetime
import re
import matplotlib.pyplot as plt
import requests
import pandas as pd


# Преобразование из строки в тип datetime, принимаемый SQL
def date_to_sql(dt):
    if dt == '':
        return datetime.datetime.strftime(datetime.datetime.today(), '%Y-%m-%dT%H:%M:%S')
    return datetime.datetime.strftime(datetime.datetime.strptime(dt, '%d/%m/%Y'), '%Y-%m-%dT%H:%M:%S')


# Преобразование кортежа со строками в форматы datetime и float
def to_date(dt):
    return datetime.date.fromisoformat(dt[0]), float(dt[1])


# Запрос данных с сайта
def get_rate(fromdate, todate):
    # Из строки преобразуем в формат datetime для SQL - готовим исходные данные к запросу
    fromdate = date_to_sql(fromdate)
    todate = date_to_sql(todate)

    # Собственно запрос данных с сайта
    headers = {'content-type': 'text/xml'}
    body = f'<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><KeyRateXML xmlns="http://web.cbr.ru/"><fromDate>{fromdate}</fromDate><ToDate>{todate}</ToDate></KeyRateXML></soap:Body></soap:Envelope>'
    url = 'https://cbr.ru/DailyInfoWebServ/DailyInfo.asmx'
    response = requests.post(url, data=body, headers=headers)
    keyrate = response.text

    # Из всего response делаем выборку на нужные данные в нужном виде: дата в формате yyyy-mm-dd и ставка
    # Пакет, полученный по SOAP, показалось проще обработать через регулярные выражения, а не через парсинг
    datetime_pattern = r'\d{4}-\d{2}-\d{2}'
    rate_pattern = r'\d+\.\d+'
    match = re.findall(rf'<DT>({datetime_pattern})T.*?</DT>.*?<Rate>({rate_pattern})</Rate>', keyrate, re.DOTALL)

    return match


# Помещение в Pandas.DataFrame полученных с сайта данных
def to_df(match):
    # Преобразование кортежей (дата, ставка) из строкового типа
    dates_n_rates = []
    for i in match:  # Здесь можно "решить" потоками, если диапазон дат для анализа запрошен большим.
        dates_n_rates.append(to_date(i))

    df = pd.DataFrame(dates_n_rates, columns=['Дата', 'Ставка'])

    # Помещаем данные в файл - просто так, на всякий случай задел на будущее
    with open('rates.csv', 'w', encoding='utf8') as file:
        df.to_csv(file, index=False, sep=';')

    return df


def to_plot(df):
    plt.plot(df['Дата'], df['Ставка'])
    plt.xlabel('Дата')
    plt.xticks(rotation=45)
    plt.ylabel('Ставка')
    plt.title(
        f'ВИЗУАЛИЗАЦИЯ ДИНАМИКИ КЛЮЧЕВОЙ СТАВКИ С ИСПОЛЗОВАНИЕМ БИБЛИОТЕКИ MATPLOTLIB\nДинамика ключевой ставки ЦБ РФ за период {datetime.datetime.strftime(df.iloc[-1, 0], '%d.%m.%Y')} - {datetime.datetime.strftime(df.iloc[0, 0], '%d.%m.%Y')}\n')
    plt.show()

    # Второй вариант функции, если не через pandas.DataFrame
    # def to_plot(df):
    # x=[i[0] for i in df]
    # y=[i[1] for i in df]
    #
    # plt.plot(x, y)
    # plt.xlabel('Дата')
    # plt.xticks(rotation=45)
    # plt.ylabel('Ставка')
    # plt.title(
    #     f'ВИЗУАЛИЗАЦИЯ ДИНАМИКИ КЛЮЧЕВОЙ СТАВКИ С ИСПОЛЗОВАНИЕМ БИБЛИОТЕКИ MATPLOTLIB\nДинамика ключевой ставки ЦБ РФ за период {datetime.datetime.strftime(x[-1], '%d.%m.%Y')} - {datetime.datetime.strftime(x[0], '%d.%m.%Y')}')
    # plt.show()


request = get_rate(input('Введите начальную дату диапазона (дд/мм/гггг):'),
                   input('Введите конечную дату диапазона (дд/мм/гггг):'))

# Вывод на консоль - по заданию урока к библиотеке request)))
print(
    f'\nРезультат запроса с сайта с использованием библиотеки request и предварительной обработки данных:\n{request}\n')

df = to_df(request)
print(f'Результат бессмысленной (?) обработки данных - помещения в pandas.DataFrame:\n{df}')

# Визуализация - задание к уроку по библиотеке matplotlib.
to_plot(df)
# to_plot(request) #(для варианта функции to_plot без pandas)
