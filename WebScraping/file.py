import requests_html
from requests_html import HTMLSession, HTML, HTML, HTMLResponse
import csv

session = HTMLSession()
source = session.get('https://www.imdb.com/movies-in-theaters/?ref_=cs_inth')
csv_file = open('movies.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator = '\n')

csv_writer.writerow(['TITLE', "PLOT", 'RUNTIME'])
title = []
plot = []
runtime = []
count = 1
boxes = soup.find