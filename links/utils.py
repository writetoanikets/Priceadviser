import csv
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
from pathlib import Path
import os

# def get_data(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
#         "Accept-Language": "en",
#     }
#     page = requests.get(url, headers)

# soup = BeautifulSoup(r.text, "lxml")
# name = soup.select_one(selector=".B_NuCI").getText()
# name = name.strip()

# price = soup.select_one(selector="._30jeq3").getText()
# ruppee_price = price[1:]
# price = ruppee_price.replace(',', '')
# price = float(price)
# return name, price


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
# }
# page = requests.get(URL, headers)
# soup1 = BeautifulSoup(page.content, 'html.parser')
# soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
# print(soup2)
# title = soup2.find(id="producttitle").get_text()
# print(title)

# print(soup2)
# #currency price #currencyINR
# url = 'https://www.amazon.in/LG-inches-Ultra-55BXPTA-Silver/dp/B08J97B3LN/ref=sr_1_39?crid=1OI0548X6PVP4&keywords=lg+tv&qid=1652102525&sprefix=lg+%2Caps%2C615&sr=8-39'


# def get_data(url):
#     DRIVER_PATH = str(Path('links\geckodriver').resolve())
#     options = webdriver.FirefoxOptions()
#     options.headless = True
#     driver = webdriver.Firefox(executable_path=DRIVER_PATH, options=options)
#     driver.get(url)
#     text = driver.page_source
#     soup = BeautifulSoup(text, 'html.parser')
#     name = soup.find(
#         'span', {'class': 'a-size-large product-title-word-break'}).getText()
#     name = name.strip()
#     price = soup.find('span', {'class': 'a-offscreen'}).getText()
#     # price = soup.select_one(selector="._30jeq3").getText()
#     ruppee_price = price[1:]
#     price = ruppee_price.replace(',', '')
#     price = float(price)
#     print(name, price)
#     return name, price


# make driver config
def load_driver():
    options = webdriver.FirefoxOptions()

    # enable trace level for debugging
    options.log.level = "trace"

    options.add_argument("-remote-debugging-port=9224")
    options.add_argument("-headless")
    options.add_argument("-disable-gpu")
    options.add_argument("-no-sandbox")

    binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))

    firefox_driver = webdriver.Firefox(
        firefox_binary=binary,
        executable_path=os.environ.get('GECKODRIVER_PATH'),
        options=options)

    return firefox_driver


# get_data(url)
def get_data(url):
    # DRIVER_PATH = str(Path('links/geckodriver').resolve())
    # options = webdriver.FirefoxOptions()
    # options.headless = True
    # driver = webdriver.Firefox(executable_path=DRIVER_PATH, options=options)
    # driver.get(url)
    # text = driver.page_source
    # driver.close()

    driver = load_driver()
    driver.get(url)
    text = driver.page_source
    driver.close()
    soup = BeautifulSoup(text, 'html.parser')
    if url[12:21] == 'amazon.in':
        try:
            name = soup.find(
                'span', {'class': 'a-size-large product-title-word-break'}).getText()
            name = name.strip()
        except AttributeError:
            name = 'NoneType'
        try:
            price = soup.find('span', {'class': 'a-offscreen'}).getText()
            ruppee_price = price[1:]
            price = ruppee_price.replace(',', '')
            price = float(price)
        except AttributeError:
            price = 'NoneType'

        print(name, price)
        # return name, price
    elif url[12:24] == 'flipkart.com':
        try:
            # name = soup.find('span', {'class': 'B_NuCI'}).getText()
            name = soup.select_one(selector=".B_NuCI").getText()
            name = name.strip()
        except AttributeError:
            name = 'NoneType'
        try:
            price = soup.select_one(selector="._30jeq3").getText()
            # price = soup.find('div', {'class': '_30jeq3 _16Jk6d'}).getText()
            ruppee_price = price[1:]
            price = ruppee_price.replace(',', '')
            price = float(price)
        except AttributeError:
            price = 'NoneType'
        print(name, price)
    return name, price
