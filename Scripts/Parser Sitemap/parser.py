import requests
from bs4 import BeautifulSoup

# URL вашего sitemap
sitemap_url = "https://trainer-giri.ru/sitemap.xml"  # замените на точную ссылку, если отличается

# Загружаем sitemap
resp = requests.get(sitemap_url)
resp.raise_for_status()
soup = BeautifulSoup(resp.text, "xml")

# Получаем все URL
urls = [loc.text for loc in soup.find_all("loc")]

# Проходим по каждой ссылке, получаем заголовок и выводим результат
for url in urls:
    r = requests.get(url)
    r.raise_for_status()
    page = BeautifulSoup(r.text, "html.parser")
    h1 = page.find("h1")
    title = h1.text.strip() if h1 else (page.title.text.strip() if page.title else "Нет заголовка")
    print(f"{url} - {title}")
