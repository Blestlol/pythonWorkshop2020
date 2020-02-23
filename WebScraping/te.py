from bs4 import BeautifulSoup
import requests

url = 'http://programmersclub.co.in/'
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'lxml')
print(soup.prettify())