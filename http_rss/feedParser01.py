import feedparser

myurl = 'http://www.aladin.co.kr/rss/special_new/351'

fdparser = feedparser.parse(myurl)
print(type(fdparser))
print(len(fdparser.entries))

myentries = fdparser.entries

for entry in myentries:
    # print(entry)
    # print(type(entry))
    print('타이틀 : ', entry.title, sep='')
    print('카테고리 : ', entry.category, sep='')
    print('링크 : ', entry.link, sep='')
    print('-'*30)