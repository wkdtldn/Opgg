import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome()
url = "https://www.op.gg/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

champion_tap = driver.find_element(By.XPATH, '//*[@id="__next"]/header/div[3]/nav/ul/li[2]/a/div')
champion_tap.click()
time.sleep(2)

search_champ = "파이크" # input("챔피언 검색: ")
input = driver.find_element(By.XPATH, '//*[@id="searchChampion"]')
input.send_keys(search_champ)
time.sleep(2)

champion = driver.find_element(By.CSS_SELECTOR, '#content-header > div > div:nth-child(1) > div.recent-search-container > div.css-79elbk.eedfmla1 > div > form > div.search-wrapper.focused.active-pc-typing > div > div > nav > a > div').click()
time.sleep(3)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# time.sleep(2)
# pre_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     cur_height = driver.execute_script("return document.body.scrollHeight")
#     if pre_height == cur_height:
#         break
#     pre_height == cur_height

# time.sleep(3)


rune_page = driver.find_element(By.XPATH, '//*[@id="content-header"]/div[2]/div/a[2]')
rune_page.click()

time.sleep(3)

html_source = BeautifulSoup(driver.page_source, 'html.parser')

time.sleep(2)

post = html_source.select_one('#content-container > main > section > table > tbody > tr:nth-child(1) > td.css-g7r3ai.e10rr7d40')