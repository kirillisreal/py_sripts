import requests
from bs4 import BeautifulSoup
import time

url = 'https://telemetr.me/channels/'

with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en"
    }
    resp = se.get(url)

index = BeautifulSoup(resp.content, 'html.parser')

max_page = int(input('Введите предпологаемое количество страниц: '))
pages = []
input_category = input('Введите категорию, учитывая регистр, как на стайте: ')

for x in range(1, max_page + 1):
    time.sleep(5)
    sort = pages.append(se.get(f'https://telemetr.me/channels/cat/{input_category}/?page=' + str(x)))

for sort in pages:
    pars = BeautifulSoup(sort.content, 'html.parser')

    for el in pars.select('.wd-300 '):
        link = el.find('a')
        try:
            print(link.get('href'))
            with open(f'{input_category}.txt', 'a+') as file:
                file.write(f'{link.get("href")}/n')

        except AttributeError as error:
            print(f'Произошла ошибка {error}. Работа скрипта продолжается.')
            continue
