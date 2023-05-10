import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup

web_page = requests.get('https://live.skillbox.ru/playlists/code/python/')

soup = BeautifulSoup(web_page.text, 'html.parser')

soup.find(class_='playlist-inner-card__title hover-card__text playlist-inner-card__title--big').text
relative_url = soup.find(class_='playlist-inner-card hover-card').attrs['href']

abs_url = 'https://live.skillbox.ru' + relative_url

def exelBook():
    # Создаем книгу Excel
    table = [[1, 2, 3], [4, 5, 6]]

    work_book = Workbook()
    work_sheet = work_book.active

    # Коллекция для генерации таблицы
    items = soup.find_all(class_='playlist-inner__item')

    for elem in items:
        title = elem.find(class_='playlist-inner-card__title hover-card__text playlist-inner-card__title--big').text
        relative_url = elem.find(class_='playlist-inner-card hover-card').attrs['href']
        url = 'https://live.skillbox.ru' + relative_url
        row = [title, url]
        print(row)
        work_sheet.append(row)

    work_book.save('Вебинары про Python от Skillbox2.xlsx')

exelBook()