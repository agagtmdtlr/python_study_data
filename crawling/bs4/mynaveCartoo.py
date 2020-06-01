from bs4 import BeautifulSoup
import urllib.request as req
import os
myencoding = 'utf-8'
myparser = 'html.parser'

url = 'https://comic.naver.com/webtoon/weekday.nhn'

selector = '#content > div > div > div > ul > li > div.thumb > a'

html = req.urlopen(url)
soup = BeautifulSoup(html,myparser)
a_list = soup.select(selector)
print(len(a_list))

webtoondict = dict()

cnt = 0
for a in a_list:
    img = a.find('img')
    title = img.attrs['title']
    src = img.attrs['src']
    href = a.attrs['href'].split('?')[1].split('&')
    step1 = [st.split('=') for st in href]
    titleid = step1[0]
    weekday = step1[1]

    if not webtoondict.get(title):
        webtoondict[title] = dict()
        webtoondict[title]['title'] = title
        webtoondict[title]['img'] = src

    webtoondict[title]['titleid'] = titleid[1]
    print(cnt)
    cnt += 1
    if not webtoondict[title].get('weekday'):
        webtoondict[title]['weekday'] = set()
        webtoondict[title].get('weekday').add(weekday[1])
    else:
        if not weekday[1] in webtoondict[title]['weekday']:
            webtoondict[title]['weekday'].add(weekday[1])

sortlist = sorted(webtoondict,key=lambda x : webtoondict.get(x).get('title'))
for key in sortlist:
    print(f'{key} : ',webtoondict[key])

print(len(webtoondict))

with open('data/naverCartoo.csv',mode='w',encoding=myencoding) as file:
    for key in sortlist :
        item = webtoondict[key]
        line = item['title']
        line += ',' + item['titleid']
        line += ',' + item['img']
        line += ','+'/'.join(item['weekday'])+'\n'
        file.write(line)