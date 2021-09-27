# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:05:41 2020

@author: samjm
"""

text="What is 2+2"
search=text.replace(" ","+")
link="https://www.google.com/search?q="+search
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
source=requests.get(link,headers=headers).text
soup=BeautifulSoup(source,"html.parser")
answer=soup.find('span',id="cwos")

self.respond(answer.text)
