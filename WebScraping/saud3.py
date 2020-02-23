import requests
from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs")
listDetail = r.html.find('.list.detail', first = True)
Title = listDetail.find('.overview-top h4 a')
for i in range(0, len(Title)):
    print(Title[i].text)
    print()