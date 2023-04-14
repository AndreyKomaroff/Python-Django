import requests
from bs4 import BeautifulSoup

# Задаем url страницы, которую нужно спарсить
url = 'https://www.силаруков.рф/'

# Отправляем GET-запрос на указанный url
response = requests.get(url)

# Получаем HTML-код страницы
soup = BeautifulSoup(response.text, 'html.parser')

# Находим заголовок страницы
title = soup.find_all(class_='text')
sorted_tags = sorted(title, key=lambda tag: tag.name)

with open('list.ods', 'a') as file:
    for tag in sorted_tags:
        file.write(f'{tag.text}\n')
        print(tag.text)

# Находим описание страницы на основе мета-тега с атрибутом name="description"
#description = soup.find('meta', attrs={'name': 'description'})['content']

# Выводим заголовок и описание страницы
