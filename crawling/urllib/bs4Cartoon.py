from bs4 import BeautifulSoup
import urllib.request as req

url = 'https://comic.naver.com/webtoon/weekday.nhn'

htmldoc = req.urlopen(url)

soup = BeautifulSoup(htmldoc,features='html.parser')

print(soup)