from bs4 import BeautifulSoup

myencoding = 'utf-8'
myparser = 'html.parser'
filename = 'data/fruits.html'

html = open(filename,encoding=myencoding)
soup = BeautifulSoup(html,myparser)
# print(soup)

# body = soup.select_one('body')
# ptag = body.find('p')
# print(ptag['class']) # ['ptag', 'red']
#
# ptag['class'][1] = 'white'
#
# print(ptag['class'])
# dom : document object model

body_tag = soup.find('body')
idx=0
for child in body_tag.children:
    idx +=1
    # white character 도 element에 포함 된다.
    # print(str(idx)+'번째 요소: ',child)

mydiv = soup.find('div')
print(mydiv)
print('mydiv 부모 태그')
print(mydiv.parent)
print('-'*50)

p_tag = soup.find('p',{'class':'hard'})
print(p_tag)
print(p_tag.find_parent());print(type(p_tag));
print(p_tag.parent);print(type(p_tag));

parents = p_tag.find_parents()
for p in parents:
    print(p.name)

# 모든 p태그의 속성
p_tags = soup.find_all('p')
setp = set()
for p in p_tags:
    setp.update(set(p['class']))
print(setp)
