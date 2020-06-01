from itertools import count
from pyy.crawling.chicken.ChickenUtil import ChickenStore
###############################################################
brandName = 'pelicana'
base_url = 'https://pelicana.co.kr/store/stroe_search.html'
#############################################################
def getData():
    savedData= [] # 엑셀로 저장할 리스트
    for page_idx in count(): # 0 based 주의하기
        url = base_url+'?page='+str(page_idx+1)
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()

        mytable = soup.find('table',attrs={'class':'table mt20'})

        mytbody = mytable.find('tbody')

        # flag 기법
        shopExist = False # 매장 목록이 없다고 가정
        for mytr in mytbody.findAll('tr'):

            mylist = list(mytr.strings)
            # print(mylist)
            store = mylist[1]
            address = mylist[3]
            shopExist = True

            # 주소 빈칸 예외처리
            if len(address) >= 2 :
                imsi = address.split()
                sido = imsi[0]
                gungu = imsi[1]
                # print(address)
                mydata = [brandName, store, sido, gungu, address]
                savedData.append(mydata)
        if shopExist == False :
            # csv 파일로 저장하세요.
            chknStore.save2Csv(savedData)
            break
        # flag 기법
#######################################################
print(brandName+'크롤링 시작')
getData()
print(brandName+'크롤링 끝')

#############################################################