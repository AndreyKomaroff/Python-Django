from selenium import webdriver
#from seleniumwire import webdriver
import time
from selenium.webdriver.common.keys import Keys
#from proxy_auth import login, password

#url = 'https://trainer-giri.ru/'

#user_agent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

#proxy

#options.add_argument('--proxy-server=168.81.3.230:8000:aHvsKc:kvY9kp')
#proxy_options = {
#    "proxy": {
#        "https": f'https://{login}:{password}@168.81.3.230:8000'
#    }
#}

driver = webdriver.Chrome(executable_path='/home/andrew/Документы/Python/Selenium/first_parcer/chrome/chromedriver', options=options)

try:
    driver.get("https://vk.com/")
    time.sleep(5)

    email_input = driver.find_element("id", "index_email")
    email_input.clear()
    email_input.send_keys("komarov.andrey1988@mail.ru")
    time.sleep(3)
    email_input.send_keys(Keys.ENTER)
    time.sleep(3)

    password_input = driver.find_element("name", "password")
    password_input.clear()
    password_input.send_keys("Kamap999!999!")
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)
    time.sleep(60)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()