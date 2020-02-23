import requests
from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.imdb.com/chart/top/?sort=ir,desc&mode=simple&page=1")
listerList = r.html.find('.lister-list', first = True)
print(listerList)

Title = listerList.find('.titleColumn')
#print(Title)

rating = listerList.find('.ratingColumn strong')
image = listerList.find('.posterColumn a img')
for i in (range(0,1000):
    #print(Rating[i].text)
    print(Title[i].text, rating[i].text)
    #for i in image:   
    print(i.attrs['src'])
    print()
