from itertools import count
from pyy.crawling.chicken.ChickenUtil import ChickenStore
###############################################################
brandName = 'kyochon'
base_url = 'http://www.kyochon.com/shop/domestic.asp'
#############################################################
def getData():
    savedData = [] # 엑셀로 저장할 리스트

    for sido1 in range(1,18):
        for sido2 in count(): # 0 base

            url = base_url
            url += f'?sido1={sido1}'
            url += f'&sido2={sido2+1}' # 0+1 1부터 시작

            chknStore = ChickenStore(brandName,url)
            soup = chknStore.getSoup()
            if soup is None:
                break

            ultag = soup.find('ul',attrs={'class','list'})

            # 페이지는 로딩 되는데 , 매장이 0개
            if ultag.find('a').find('strong') is None:
                continue

            for myitem in ultag.find_all('a'):
                # print(myitem)
                try:
                    store = myitem.span.strong.string
                    # print(store)
                    myhref = myitem['href']
                    myhref = myhref.replace("javascript:mapchange('","")
                    # print(myhref)
                    # string.find('') 해당 인자의 위치 찾기
                    quote = myhref.find("'")
                    address = myhref[0:quote]
                    # print(address)
                    imsi = address.split(' ')
                    sido = imsi[0]
                    gungu = imsi[1]

                    # 1 row 추가
                    savedData.append([brandName,store,sido,gungu,address])
                except Exception as err :
                    print(f'[{err}] : '+url)
                    print(myitem)
                    continue
    #end for
    chknStore.save2Csv(savedData)
#######################################################
print(brandName+'크롤링 시작')
getData()
print(brandName+'크롤링 끝')

#############################################################