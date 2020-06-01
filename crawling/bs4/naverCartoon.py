import os, shutil # shutil : shell utility (shell core)
from bs4 import BeautifulSoup
import urllib.request
from pandas import DataFrame

myencoding = 'utf-8'
myparser = 'html.parser'
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'

response = urllib.request.urlopen(myurl)
soup = BeautifulSoup(response,myparser)
print(type(soup))

weekday_dict = {'mon':'월요일','tue':'화요일','wed':'수요일',
                'thu':'목요일','fri':'금요일','sat':'토요일','sun':'일요일'}

myfolder = 'C:\\imsi\\'

try:
    for mydir in weekday_dict.values():
        mypath = myfolder + mydir
        if os.path.exists(mypath): #이미 폴더가 존재하는지 확인
            shutil.rmtree(mypath) # 내용물 포함하여 강제 폴더 삭제
        os.mkdir(mypath)
except FileExistsError as err :
    print(err)

mytarget = soup.find_all('div',attrs={'class':'thumb'})
print(len(mytarget))

# div 태그에서 class 속성이 thumb을 찾는다
# 반복문
#   <a>태그의 href 속성을 읽어 온다.
#   replace() 함수로 치환
#   split() 함수를 이용하여 요소 분해
#   <img>태그
#   title 속성을 읽어 와서 제목으로 처리
#   ?와 :은 치환
#   src 속성을 읽어와서 이미지가 존재하는 실제경로

# 필요한 정보를 리스트에 추가한다.
# 데이터 프레임으로 만들어 csv 파일로 저장합니다.

def saveFile(mysrc,myweekday,mytitle):
    image_file = urllib.request.urlopen(mysrc)
    print(type(image_file))
    filename = myfolder+weekday_dict[myweekday]+'\\'+mytitle+'.jpg'
    with open(filename,mode='wb') as file:
        file.write(image_file.read())

mylist = [] # 데이터를 저장할 리스트

for thumb in mytarget :
    myhref = thumb.find('a').attrs['href']
    myhref = myhref.replace('/webtoon/list.nhn?','')
    # print(myhref)
    result = myhref.split('&')
    mytitleid = result[0].split('=')[1]
    myweekday = result[1].split('=')[1]
    # print(mytitleid+'/'+myweekday)

    imgtag = thumb.find('img')
    mytitle = imgtag.attrs['title'].strip()
    # print(mytitle) # don't [: / ? *]
    mytitle = mytitle.replace('?','').replace(':','')
    mysrc = imgtag.attrs['src']
    # print(mytitle+'/'+mysrc)
    # img = urllib.request.urlretrieve(mysrc,mytitle+'.jpg') # download
    mytuple = tuple([mytitleid,weekday_dict.get(myweekday),mytitle,mysrc])
    mylist.append(mytuple)

    # 이미지 저장 함수
    saveFile(mysrc,myweekday,mytitle)
# csv 파일로 저장
mycolumn = ['타이틀 번호','요일','제목','링크']
myframe = DataFrame(mylist, columns=mycolumn)

filename = 'data/cartoon.csv'
myframe.to_csv(filename,encoding=myencoding,index=False)
print(filename+' 파일로 저장')

print('finished')