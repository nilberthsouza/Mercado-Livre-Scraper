from bs4 import BeautifulSoup
import requests
import time
import smtplib
import tkinter as tk
from tkinter import messagebox
from db import Database

page = requests.get('linkdoproduto')

def get_info(in_value):
    soup = BeautifulSoup(page.text, 'html.parser')
    out_value = soup.find(class_=in_value)
    return out_value.string

def convert_value_to_num(value_str):
    out_value_flt  = float(value_str)
    return out_value_flt


def price_checker(price_conv):
    if price_conv < 100:
        email_sender()
    else:
        print("sistema funcionando")
        pass

while(True):
    get_info('item-title__primary')
    price_conv =convert_value_to_num(get_info('price-tag-fraction'))
    price_checker(price_conv)
    time.sleep(100)




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

import tkinter as tk
from tkinter import messagebox
from db import Database

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        master.title('Mercado Livre Scrapper')
        master.geometry("700x350")
        self.create_widgets()
        self.populate_list()

    def create_widgets(self):
        self.link_text = tk.StringVar()
        self.link_label = tk.Label(
            self.master, text='Link',font=('bold',14),pady=20)
        self.link_label.grid(row=0,column=0,sticky=tk.W)
        self.link_entry = tk.Entry(self.master, textvariable=self.link_text)
        self.link_entry.grid(row=0,column=1)
        self.parts_list = tk.Listbox(self.master, height=8, width=50, border=0)
        self.parts_list.grid(row=1, column=3)
        
    def get_info():
        pass

root = tk.Tk()
app.Application(master=root)
app.mainloop()
