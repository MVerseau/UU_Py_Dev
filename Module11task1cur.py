import requests
import pandas as pd
from io import StringIO


def get_rate():
    headers = {'content-type': 'text/xml'}
    body = '<?xml version="1.0" encoding="utf-8"?><soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"><soap12:Body><MainInfoXML xmlns="http://web.cbr.ru/" /></soap12:Body></soap12:Envelope>'
    url = 'https://cbr.ru/DailyInfoWebServ/DailyInfo.asmx'
    response = requests.post(url, data=body, headers=headers)
    keyrate = response.text.split("<stavka_ref")[1].split("</stavka_ref>")[0]
    return keyrate

print(get_rate())
# r = requests.get('https://cbr.ru/currency_base/daily/', params='13.07.2024')
# print(f'{r=}')
# print(f'{r.url=}')
# print(f'{r.headers=}')
# print(f'{r.encoding=}')
# print(f'{r.cookies=}')
# print(f'{r.status_code=}')
# print(f'{r.elapsed=}')
# print(f'{r.reason=}')
# # print(r.text)
# url='http://www.cbr.ru/scripts/XML_dynamic.asp'
# url = '"http://web.cbr.ru/KeyRateXML.xml'
# df = pd.read_xml(url)
# with open('df.csv', 'w', encoding='utf8') as file:
#     df.to_csv(file)
# print(df)

# https://www.cbr.ru/development/SXML/
