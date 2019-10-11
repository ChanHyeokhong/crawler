#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen

def press(url):
    data = urlopen(url)
    soup = BeautifulSoup(data, "html.parser")
    for div in soup.find_all('div', 'press_logo'):
        img = div.find('img', alt=True)
        return img['alt']
