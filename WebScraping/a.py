'''import requests
from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
listerList = r.html.find('.lister-list', first = True)
print(listerList)

Title = listerList.find('.titleColumn')
for i in range(0, len(Title)):
    print(Title[i].text) 
    print()
'''
from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'lxml')
title = soup.find_all(class_='titleColumn')
for i in title:
    print(i.get_text())