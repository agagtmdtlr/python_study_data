from bs4 import BeautifulSoup
import urllib.request as req

url = 'http://www.naver.com'

res = req.urlopen(url)
print(type(res))

soup = BeautifulSoup(res,'html.parser')
# print(soup)

title = soup.find(('title')).string
print(title)
print(soup.title)