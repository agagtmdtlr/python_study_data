from bs4 import BeautifulSoup

myencoding = 'utf-8'
myparser = 'html.parser'
filename = 'data/bs01.html'

html = open(filename,encoding=myencoding)
# print(html.read())
soup = BeautifulSoup(html,myparser)

# print(type(soup))
# # print(soup)
#
# # id = (unique)
# title = soup.find(id='title').string
# print(title)
# hohoho = soup.find(id='hohoho').string
# print(hohoho)
#
# # 직접 태그를 언급하는 방법
# # soup attribute
# print(soup.td)
# print('td'*20)
# print(soup.div)
# print('div'*20)
# mytag = soup.a
# print(mytag)
# print(mytag.name)
# print('c'*20)

# # 속성 가져오기
# mytag = soup.td
# print('속성 정보 :')
# print(mytag['class'])
# # 해당 태그의 속성들 불러오기
# print(mytag.attrs) # return dict
#
# print(soup.body.h1.string)
# print('c'*20)
#
# mytag = soup.find('td',attrs={'class':'title'})
# mytag = soup.find('div',attrs={'class':'tit3'})
# print(mytag)
# print(mytag['id'])


# 여러 요소 불러오기 : find_all()
mytag = soup.find_all('span',attrs={'class','split'})
print(len(mytag),type(mytag))
# fin_all 요소들 : 불러오 요소들 하나씩 불러와 처리하기
for item in mytag :
    print(item.name)
    content = item.string
    # 해당 태그 다음에 나오는 target(value) 이후는 next, 이전은 previous
    previ = item.previous_sibling.strip()
    aside = item.next_sibling.strip()
    print(previ,'/',content,'/',aside)

mytag = soup.find_all('a',limit=2)
print(len(mytag))
for item in mytag :
    content = item.string
    href = item['href']
    print(content,'(',href,')')

mybody = soup.find('body')
print(mybody.get_text())

mybody = soup.find('body')
print(mybody.get_text(' ',strip=True))
