import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rpeople.naver'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

actor_list = soup.find_all('td', class_= 'title')

for actor in actor_list:
    print(actor.find('a').text)
