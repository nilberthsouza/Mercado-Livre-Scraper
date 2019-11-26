from bs4 import BeautifulSoup
import requests
import time
page = requests.get('https://produto.mercadolivre.com.br/MLB-698976428-peruca-cosplay-branca-prata-prontaentrega-_JM')

soup = BeautifulSoup(page.text, 'html.parser')
title = soup.find(class_='item-title__primary')
print(title.string)

soup = BeautifulSoup(page.text,'html.parser')
price = soup.find(class_='price-tag-fraction')
price_conv =int(price.string)
print(price_conv)

def email_sender()

def price_checker():
    if price_conv < 100:
        email_sender()
    else:
        pass


while(true):
    price_checker()
        time.sleep(100)
