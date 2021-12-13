import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

movie_list = soup.find_all('div', class_= 'tit3')

for movie in movie_list:
    print(movie.find('a').text)
