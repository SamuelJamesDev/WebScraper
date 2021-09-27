# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:05:55 2020

@author: Samuel James
"""

from bs4 import BeautifulSoup
import requests

URL = 'https://www.timeanddate.com/on-this-day/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='otd-tt1')
print(results.prettify())

def Scrape(this, url, cls):
    response = requests.get(url, headers={'User-Agent': 'Chrome/5.0'})
    html = response.content

    soup = BeautifulSoup(html, features="lxml")

    span = soup.find(this, attrs={'class': cls})
    
       

cls = 'otd-tt1'
url = 'https://www.timeanddate.com/on-this-day/'
print("TODAY IN HISTORY:")
print("____________________")
this = 'p'
Scrape(this, url, cls)
