import requests

cookies = {
    'SESS856962402010800860cc1c6885953bde': 'ni2sq105jullfjq06rofa6s103',
    'has_js': '1',
}

headers = {
    'authority': 'www.xn--80aeqjdumew.xn--p1ai',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'SESS856962402010800860cc1c6885953bde=ni2sq105jullfjq06rofa6s103; has_js=1',
    'if-modified-since': 'Fri, 07 Apr 2023 16:52:59 GMT',
    'if-none-match': '"1388287ea62dc0ea361a25750e7cecbe"',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.5.751 Yowser/2.5 Safari/537.36',
}

response = requests.get('https://www.xn--80aeqjdumew.xn--p1ai/', cookies=cookies, headers=headers)

with open('result.html', 'w') as file:
    file.write(response.text)