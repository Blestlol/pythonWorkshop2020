from bs4 import BeautifulSoup
import requests
for i in range (1, 51):
    url = ("http://books.toscrape.com/catalogue/page-{}.html".format(i))
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    print(soup.prettify())
    print("++++++++++++++++++END OF", i , '+++++++++++++++++++++++++')
