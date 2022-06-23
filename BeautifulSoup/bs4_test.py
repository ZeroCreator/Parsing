import requests
from bs4 import BeautifulSoup

r = requests.get('https://bitskins.com/')
soup = BeautifulSoup(r.content, 'html.parser')