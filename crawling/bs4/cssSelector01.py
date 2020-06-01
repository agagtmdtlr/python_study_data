from bs4 import BeautifulSoup

myencoding = 'utf-8'
myparser = 'html.parser'
filename = 'data/css01.html'

html = open(filename,encoding=myencoding)
soup = BeautifulSoup(html,myparser)
# print(soup)


# select_one,find
h1 = soup.select_one('div#cartoon > h1').string
print('h1\n',h1)

# lists...
li_list = soup.select('div#cartoon > ul.elements > li')
for li in li_list:
    print(li.string)
print('-'*50)

# use lambda
choice = lambda  x : print(soup.select_one(x).string)
choice('#item5')
choice('li#item4')
choice('ul > li#item3')
choice('#itemlist #item3')
choice('ul#itemlist > li#item2')

print(soup.select('li')[1].string)
print(soup.select('li')[3].string)

print(soup.select_one('li:nth-of-type(4)').string)
li_list = soup.select('li:nth-of-type(4)')
for li in li_list:
    print(li.string)

# com
result = soup.select('a[href$=".com"]')
for item in result :
    print(item['href'])
print('-'*40)
# daum
result = soup.select('a[href*="daum"]')
for item in result :
    print(item['href'])

result = soup.select('a[href^="www"]')
for item in result :
    print(item['href'])

cond = {'id':'ko','class':'cn'}
print(soup.find(id='vegatables').find('li',cond).string)
'''
#은 id 속성
.은 class 속성
div#cartoon : div 태그 주에서 id 속서이 cartoon인 항목
>는 바로 하위 child
nth-of-type(n) : 부모로부터 n번째 항목
^= : ~으로 시작하는
$= : ~으로 끝나는
*= : ~을 포함하고 있는
[attribute[^,$,*]='str']
'''

print('--------------------------------')
print('정규표현식')
import re
li = soup.find_all(href=re.compile(r'^https://'))
for item in li :
    print(item.attrs['href'])