from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv

session = HTMLSession()
urls = []

for i in range(1, 3):
    urls.append(f'https://www.zomato.com/mumbai/order-food-online?utm_source=google&utm_medium=cpc&utm_term=zomato&utm_campaign=Gsearch_P-MWeb_O-NA_C-Brand_A-NewUser_SC-Generic_L-Mumbai&gclid=EAIaIQobChMIx_DA25vE5wIVlIKRCh0U5AFzEAAYASAAEgJ2OvD_BwE&page={i}')

csv_file = open('zomato.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator = '\n')

csv_writer.writerow(['Restaurant', 'Rating', 'ImageUrl'])
count = 1
for url in urls:
    source = session.get(url).html.html
    soup = BeautifulSoup(source, 'lxml')

    block = soup.find('div', class_= 'row')
    elements = box.find_all('li')
    restaurant = []
    rating = []
    picture = []
    for element in elements:
        name = element.select(".row.result-order-flow-title.hover_feedback.zred.bold.fontsize0.ln20")
        restaurant.append(name)
        rate = element.find('_blank', class_='gr••••••ey-text nowrap').text
        rating.append(rate)••••••
        image = element.select('feat-img')[0]['s••••••rc']
        image_url = r'https://www.zomato.com/'+image
        picture.append(image_url)••••••
        csv_writer.writerow([name••••••_url])
        print(count, end =' ')
        count += 1
'''••••••
csv_file.close()