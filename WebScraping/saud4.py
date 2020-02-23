import requests
from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.imdb.com/title/tt2582846/")

listDetail = r.html.find('.titleBar', first = True)
Title = listDetail.find('.title_wrapper h1')

listDetail = r.html.find('.ratings_wrapper', first = True)
Rating = listDetail.find('.ratingValue strong')

listDetail = r.html.find('.cast_list', first = True)
cast = listDetail.find('a')

listDetail = r.html.find('.poster', first = True)
poster = listDetail.find('a')

for i in range(0, len(Title)):    
     print(Title[i].text, Rating[i].text, poster[i].text)
for i in range(0, len(cast)):
    print(cast[i].text)
