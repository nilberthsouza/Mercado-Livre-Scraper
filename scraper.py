from bs4 import BeautifulSoup
import requests
import time
import smtplib

page = requests.get('https://produto.mercadolivre.com.br/MLB-698976428-peruca-cosplay-branca-prata-prontaentrega-_JM')

soup = BeautifulSoup(page.text, 'html.parser')
title = soup.find(class_='item-title__primary')
print(title.string)

soup = BeautifulSoup(page.text,'html.parser')
price = soup.find(class_='price-tag-fraction')
price_conv =int(price.string)
print(price_conv)

def email_sender():
    mail_from = 'Home@nilberth.com'
    mail_to = ['nilberthsouza@gmail.com']
    mail_subject = 'O seu produto baixou de preço'
    mail_message_body = 'https://produto.mercadolivre.com.br/MLB-698976428-peruca-cosplay-branca-prata-prontaentrega-_JM'
    mail_to_string = ', '.join(mail_to)
    mail_message = f'''
    from: {mail_form}
    To: {mail_to_string}
    Subect:{mail_subject}

    {mail_message_body}
    '''

    server = smtplib.SMTP('localhost')
    server.sendmail(mail_from, mail_to, mail_subject, mail_message)
    server.quit()

def price_checker():
    if price_conv < 100:
        email_sender()
    else:
        print("sistema funcionando")
        pass


while(True):
    price_checker()
    time.sleep(100)
