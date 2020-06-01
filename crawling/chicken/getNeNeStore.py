import re
from itertools import count
from pyy.crawling.chicken.ChickenUtil import ChickenStore
###############################################################
brandName = 'nene'
base_url = 'https://nenechicken.com/17_new/sub_shop01.asp'
#############################################################
def getData():
    savedData = []
    for page_idx in range(1,47+1):
        url = base_url+'?page='+str(page_idx)
        chknStore = ChickenStore(brandName,url)
        soup = chknStore.getSoup()
        tablelists = soup.find_all('table',attrs={'class':'shopTable'})
        # print(len(tablelists))
        print(page_idx)
        for onttable in tablelists:
            store = onttable.select_one('.shopName').string
            # print(store)
            temp = onttable.select_one('.shopAdd').string
            # print(temp)
            im_address = onttable.select_one('.shopMap')
            im_address = im_address.a['href']
            # print(im_address)
            try:
                elo = 1
                if temp[-1] == '로':
                    regex = '\d\S*'
                    pattern = re.compile(regex)
                    mymatch = pattern.search(im_address)
                    addr_suffix = mymatch.group().replace("');", '')

                elif temp[-1] == '길':

                    if temp[-2].isnumeric(): # 2길..
                        elo = 2
                        regex = '[길|로]\d\S*'
                        pattern = re.compile(regex)
                        mymatch = pattern.search(im_address)
                        addr_suffix = mymatch.group().replace("');",'').strip('길로')
                    else: # 봉길...
                        temp = temp[1:len(temp)-1]
                        elo = 3
                        regex = '\d\S*'
                        pattern = re.compile(regex)
                        mymatch = pattern.search(im_address)
                        addr_suffix = mymatch.group().replace("');", '')
            except Exception as err:
                print(err)
                print(url)
                print(elo)


            # print(addr_suffix) # 상세주소
            # print(mymatch)

            address = temp + " " + addr_suffix
            imsi = temp.split(' ')
            sido = imsi[0]
            gungu = imsi[1]

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