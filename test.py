#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

r = requests.get("http://192.168.2.1/log/in?un=admin&pw=admin&rd=%2Fuir%2Fstatus.htm&rd2=%2Fuir%2Fwanst.htm&Nrd=1")

data = r.text
soup = BeautifulSoup(data, "html.parser")
a = ""
for td in soup.find_all('td', {'id':'ip3g'}):
    a = td.string
    print (a)
with open('adres.txt', 'w') as out:
    out.write(a)
