from bs4 import BeautifulSoup
import requests
x = int(input("Initial Value: "))
y = int (input("Final Value: "))
for i in range (x,y+1):
    url = ("https://www.freepik.com/search?dates=any&format=search&page="+str(i)+"&query=wallpaper&selection=1&sort=popular&type=vector")
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    print(soup.prettify())
    print("++++++++++++++++++END OF", i, '+++++++++++++++++++++++++')
