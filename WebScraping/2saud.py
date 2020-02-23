import requests
from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs")

listDetail = r.html.find('.list.detail', first = True)
title = listDetail.find(".overview-top")
for i in range(0, len(title)):
    print(title[i].text)
    print("No rating")

