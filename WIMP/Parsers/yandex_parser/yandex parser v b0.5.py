import requests
from selectolax.parser import HTMLParser as HP #да да хюлет пакарт ака эйч пи ака ноутбуки XD
from fake_useragent import UserAgent
import json
import os
import random
import sys

#прокси сервера
proxies = {
  'https': 'http://Fx4sFy:xtg85C@70.38.2.8:13043',
}
#путь к каталогу где сохраняется файл scrip.json
current_dir = os.getcwd()

#юсер агент
ua = UserAgent()
headers = {'User-Agent': ua.opera}

# получение количества страниц

page_rndm = str(random.randint(99, 999))

url = 'https://realty.ya.ru/moskva/snyat/kvartira/bez-posrednikov/?page=' + page_rndm
response = []
response = requests.get(url, proxies=proxies)

# проверка на капчу (Если её нет то записывается кол-во страниц)

if response.url[21] == 's' and response.url[31] == 'a':
    print('БЛЯ КАПЧА')
    sys.exit()
else:
    fi = str(response.url[-2])
    se = str(response.url[-1])
    x = int(fi + se)
    print('КОЛЛИЧЕСТВО СТРАНИЦ - ', x)

def main():
    read_file()

def create_file():

    html = r.text

    tree = HP(html)
    script = tree.css_first('script[id="initial_state_script"]').text()
    script = script[23:-1]

    data = json.loads(script)

    with open('scrip.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False,)

def read_file():

    create_file()

    file_js = json.load(open('scrip.json', 'r', encoding='utf-8'))

    offers = file_js['map']['offers']['points']

    for offer in offers:

        url_off = offer['url']
        area = offer['area']['value']
        price = offer['price']['value']
        adres = offer['location']['address']
        
        print(area, price, url_off, adres, sep=', ')


y = 0
z = 1
while x > y:
    
    print('СТРАНИЦА - ', y + 1)

    z = str(z)

    url = 'https://realty.ya.ru/moskva/snyat/kvartira/bez-posrednikov/?page=' + z
    z = int(z)
    if z % 5 == 0:
        proxies = {
        'https': 'http://Fx4sFy:xtg85C@70.38.2.8:13043',
        }
    elif z % 4 == 0:
        proxies = {
        'https': 'http://ZKjAGJ:3Tvg29@45.32.56.105:10601',
        }
    elif z % 3 == 0:
        proxies = {
        'https': 'http://ENWavf:8k2bvc@45.153.20.209:12732',
        }
    elif z % 2 == 0:
        proxies = {
        'https': 'http://eSKv5q:PA5xSE@45.91.209.157:12822',
        }
    else :
        proxies = {
        'https': 'http://srRTwD:0wPGjt@45.153.20.209:12731',
        }
    r = requests.get(url, headers=headers, proxies=proxies)

    if __name__ == '__main__':
        main()
    
    z+=1
    y+=1
    
print('все страницы спарсились')