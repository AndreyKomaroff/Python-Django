from selenium import webdriver
import time


url = 'https://vk.com/'
driver = webdriver.Firefox(executable_path='/home/andrew/Документы/Python/Selenium/first_parcer/firefox/geckodriver')

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()