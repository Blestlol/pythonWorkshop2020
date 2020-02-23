from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv

session = HTMLSession()
urls = []

for i in range(1, 51):
    urls.append(f'https://www.zomato.com/mumbai/order-food-online?utm_source=google&utm_medium=cpc&utm_term=zomato&utm_campaign=Gsearch_P-MWeb_O-NA_C-Brand_A-NewUser_SC-Generic_L-Mumbai&gclid=EAIaIQobChMIx_DA25vE5wIVlIKRCh0U5AFzEAAYASAAEgJ2OvD_BwE&page={i}')

csv_file = open('zomato.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator = '\n')

csv_writer.writerow(['Restaurant', 'Rating', 'ImageUrl'])
count = 1
for url in urls:
    source = session.get(url).html.html
    soup = BeautifulSoup(source, 'lxml')

    box = soup.find('ol')
    elements = box.find_all('li')
    title = []
    picture = []
    cost = []
    for element in elements:
        name = element.find()
        title.append(name)
        image = element.select('img')[0]['src']
        image_url = r'http://books.toscrape.com/'+image
        picture.append(image_url)
        price = element.find('p', class_='price_color').text
        cost.append(price)
        csv_writer.writerow([name, price, image_url])
        print(count, end =' ')
        count += 1

csv_file.close