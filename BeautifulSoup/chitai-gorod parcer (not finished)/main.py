import datetime
import csv
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import time

def collect_data():
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    ua = UserAgent()
    #print(ua.random)

    cookies = {
        '__ddg1_': 'JdqEprrEPsmXUrNNen8d',
        'refresh-token': '',
        'access-token': 'Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXIucHJvZC5jZ29yb2QucHciLCJzdWIiOiI3NTg3MzQ1ZDZjM2I4MjEzYmNhNWQ0MDRmMDllYzk1YjkyYTIxMjU2NmMxZjJlMTQ5Y2EzY2VjYjZmNmFmN2IyIiwiaWF0IjoxNjg1NjIwNTg1LCJleHAiOjE2ODU3OTMzODUsInR5cGUiOjEwfQ.R3bYhjDbWgZxn-mhfRbTqQI7bczoPhvPG2gOcEaSboE',
        'partner_name': 'Programmatic',
        'deduplication_cookie': 'Programmatic',
        'deduplication_cookie': 'Programmatic',
        '_ga': 'GA1.1.1971031828.1685620532',
        'tmr_lvid': 'a28292f653f18286e703b4091a6943af',
        'tmr_lvidTS': '1685620531696',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '71f3bd77-326f-4e52-b311-01f95107a1e0',
        '_userGUID': '0:lid2xyd4:2hmdxwShDGbEkQaLfieiI2k6Ni2_75_C',
        'dSesn': 'a0d0328a-8411-1100-9b90-55b1e994d953',
        '_dvs': '0:lid2xyd4:dZdRbVnqRrhLzOz5aeiVPRDVN5npUWFT',
        'digi_uc': 'W10=',
        '_bge_ci': 'BA1.1.5459106153.1685620532',
        'tt_deduplication_cookie': 'Programmatic',
        'tt_deduplication_cookie': 'Programmatic',
        'tt_deduplication_cookie': 'Programmatic',
        '_ym_uid': '168562053249600317',
        '_ym_d': '1685620532',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '_ym_isad': '2',
        'adrdel': '1',
        'adrcid': 'A3JG_s5DJaWOQ-7JwDUkp9g',
        'chg_visitor_id': '20ded2fb-5995-4662-b253-cb0f0fa3fe53',
        'flocktory-uuid': 'a117be71-7d9d-471e-a9ab-9ecd7db7c430-1',
        'adid': '168562053340042',
        '_ga_W0V3RXZCPY': 'GS1.1.1685620531.1.1.1685620543.0.0.0',
        'mindboxDeviceUUID': 'c64e3a21-1c86-4c2d-95cb-bd0729eaf7d3',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22c64e3a21-1c86-4c2d-95cb-bd0729eaf7d3%22%7D',
        '_ga_LN4Z31QGF4': 'GS1.1.1685620531.1.1.1685620545.46.0.0',
        'tmr_detect': '0%7C1685620546239',
    }

    headers = {
        'authority': 'www.chitai-gorod.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': '__ddg1_=JdqEprrEPsmXUrNNen8d; refresh-token=; access-token=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXIucHJvZC5jZ29yb2QucHciLCJzdWIiOiI3NTg3MzQ1ZDZjM2I4MjEzYmNhNWQ0MDRmMDllYzk1YjkyYTIxMjU2NmMxZjJlMTQ5Y2EzY2VjYjZmNmFmN2IyIiwiaWF0IjoxNjg1NjIwNTg1LCJleHAiOjE2ODU3OTMzODUsInR5cGUiOjEwfQ.R3bYhjDbWgZxn-mhfRbTqQI7bczoPhvPG2gOcEaSboE; partner_name=Programmatic; deduplication_cookie=Programmatic; deduplication_cookie=Programmatic; _ga=GA1.1.1971031828.1685620532; tmr_lvid=a28292f653f18286e703b4091a6943af; tmr_lvidTS=1685620531696; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=71f3bd77-326f-4e52-b311-01f95107a1e0; _userGUID=0:lid2xyd4:2hmdxwShDGbEkQaLfieiI2k6Ni2_75_C; dSesn=a0d0328a-8411-1100-9b90-55b1e994d953; _dvs=0:lid2xyd4:dZdRbVnqRrhLzOz5aeiVPRDVN5npUWFT; digi_uc=W10=; _bge_ci=BA1.1.5459106153.1685620532; tt_deduplication_cookie=Programmatic; tt_deduplication_cookie=Programmatic; tt_deduplication_cookie=Programmatic; _ym_uid=168562053249600317; _ym_d=1685620532; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ym_isad=2; adrdel=1; adrcid=A3JG_s5DJaWOQ-7JwDUkp9g; chg_visitor_id=20ded2fb-5995-4662-b253-cb0f0fa3fe53; flocktory-uuid=a117be71-7d9d-471e-a9ab-9ecd7db7c430-1; adid=168562053340042; _ga_W0V3RXZCPY=GS1.1.1685620531.1.1.1685620543.0.0.0; mindboxDeviceUUID=c64e3a21-1c86-4c2d-95cb-bd0729eaf7d3; directCrm-session=%7B%22deviceGuid%22%3A%22c64e3a21-1c86-4c2d-95cb-bd0729eaf7d3%22%7D; _ga_LN4Z31QGF4=GS1.1.1685620531.1.1.1685620545.46.0.0; tmr_detect=0%7C1685620546239',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.3.706 Yowser/2.5 Safari/537.36',
    }

    params = {
        'utm_source': 'Programmatic',
        'utm_medium': 'PRG1',
        'utm_campaign': 'cmp-78234660',
        'utm_content': 'gr-5020209660',
        'utm_term': 'ad-14292918879_ph-41473430917',
        'yclid': '6044422022507528191',
    }

    response = requests.get(
        'https://www.chitai-gorod.ru/catalog/books/fantastika-fentezi-9692',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    
    #with open(f'index.html', 'w') as file:
    #    file.write(response.text)

    with open('index.html') as file:
         src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    cards = soup.find_all('article', class_='product-card')
    #price = soup.find_all('div', class_='product-price')
    #discount = soup.find_all('div', class_='product-price__value--discount')

    books = []
    for card in cards:
        card_title = card.find('div', class_='product-title__head').text.strip()
        links = card.find('a', class_='product-card__picture')['href']
        card_url = f'https://www.chitai-gorod.ru{links}'

        try:
            card_price = card.find('div', class_='product-price__value--discount').text.strip()
        except AttributeError:
            continue

        books.append(
            [card_title, card_price, card_url]
        )

    #with open(f'books_{cur_time}.json', 'w') as file:
    #    json.dump(books, file, indent=4, ensure_ascii=False)

        #print(len(books))
        #print(card_url)

        print(books)

    #return books


    
    #print(len(cards))
    #print(len(price))
    #print(len(discount))



def main():
    start_time = time.time()
    collect_data()
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print("Время выполнения функции collect_data(): ", elapsed_time, " секунд.")

if __name__ == '__main__':
    main()