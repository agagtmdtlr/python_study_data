from itertools import count
from pyy.crawling.chicken.ChickenUtil import ChickenStore
import re
###############################################################
brandName = 'cheogajip'
base_url = 'http://www.cheogajip.co.kr/bbs/board.php?bo_table=store'
#############################################################
def getData():
    savedData = []
    for page_idx in range(1,115+1):
        url = base_url+'&page='+str(page_idx)
        chknStore = ChickenStore(brandName,url)
        soup = chknStore.getSoup()
        tr_list = soup.select('tbody > tr')
        for tr in tr_list:
            store = tr.select_one('td:nth-of-type(2)').string
            address = tr.select_one('.td_subject').string
            reg_ex = '\s.*'
            pattern = re.compile(reg_ex)


            imsi = address.split()
            sido = tr.select_one('td:nth-of-type(1)').string
            gungu = imsi[1]
            mymatch = pattern.search(address)
            imsi_add = mymatch.group()
            address = sido+imsi_add
            mydata = [brandName, store, sido, gungu, address]
            savedData.append(mydata)

    # end for
    # csv 파일로 저장하세요.
    chknStore.save2Csv(savedData)
#######################################################
print(brandName+'크롤링 시작')
getData()
print(brandName+'크롤링 끝')

#############################################################