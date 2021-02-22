

import requests 
from bs4 import BeautifulSoup

response = request.get('https://store.line.me/stickershop/product/14154462/ja')


response = requests.get('http://test.neet-ai.com')
soup = BeautifulSoup(response.text,'lxml')
title = soup.title.string


links = soup.findAll('a')
for link in links:
   print(link.get('href'))

   