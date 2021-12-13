import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')


movie_list = soup.find_all('tr')
print(movie_list)
for movie in movie_list:
    if movie.find('img', alt='up'):
        print(movie.find('div', class_='tit3').text.strip())
    
