from itertools import count
from pyy.crawling.chicken.ChickenUtil import ChickenStore
###############################################################
brandName = 'goobne'
base_url = 'https://www.goobne.co.kr/store/search_store.jsp'
#############################################################
def getData():
    savedData = []
    chknStore = ChickenStore(brandName,base_url)
    bEndPage = True # 마지막 페이지이면 True이더라


    for page_idx in count():
        print('%s번째 페이지 호출됨' % page_idx)
        bEndPage = False # 마지막 페이지가 아니라는 뜻
        cmdJavaScript = 'javascript:store.getList("%s")' % (str(page_idx + 1))
        soup = chknStore.getWebDriver(cmdJavaScript)

        store_list = soup.find('tbody', attrs={'id':'store_list'})

        mytrlists = store_list.find_all('tr')

        for onestore in mytrlists:
            mytdlists = onestore.find_all('td')

            if len(mytdlists) > 1 :
                store = onestore.select_one('td:nth-of-type(1)').get_text(strip=True)
                address = onestore.select_one('td:nth-of-type(3)').a.string
                imsi = address.split(' ')
                sido = imsi[0]
                gungu = imsi[1]

                savedData.append([brandName,store,sido,gungu,address])
            else : # 마지막 페이지는 <td> 태그가 1개이더라
                bEndPage = True
                break


        # for : false --> last : True --> break for
        if bEndPage == True :
            break
    # end for
    chknStore.save2Csv(savedData)
#######################################################
print(brandName+'크롤링 시작')
getData()
print(brandName+'크롤링 끝')

#############################################################