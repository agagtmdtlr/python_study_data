import json
import math
import datetime
import urllib.parse
import urllib.request

access_key = "ieU6gdettDBVUNo3lkXP8SqbMgC5fsExkGIVp7vFce1Yi6zPdMGjJ4Nk2QuEjRFj1fRG7IMDtPtH2Q4nN%2BLTtw%3D%3D"

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s] Url Request Success' % (datetime.datetime.now()))
            return  response.read().decode('utf-8')
    except Exception as err:
        print(err)
        print('[%s] Error for Url : %s' % (datetime.datetime.now(), url))
        return None

def getTourData(yyyymm, sido, gungu, nPagenum, maxRecords):
    # request url
    end_point = "http://openapi.tour.go.kr/openapi/service"
    end_point += "/TourismResourceStatsService"  # 서비스명
    end_point += "/getPchrgTrrsrtVisitorList"  # 오퍼레이션명

    parameter = '?_type=json'
    parameter += '&serviceKey=' + access_key
    parameter += '&YM=' + yyyymm
    parameter += '&SIDO=' + urllib.parse.quote(sido)
    parameter += '&GUNGU=' + urllib.parse.quote(gungu)
    parameter += '&RES_NM=' + ''
    parameter += '&pageNo=' + str(nPagenum)
    parameter += '&numOfRows' + str(maxRecords)

    url = end_point + parameter

    result = getRequestUrl(url)
    if result == None:
        return None
    else : # loads : 문자열을 dict 형태로 변환해주는 함수
        return json.loads(result)

def tourPointCorrection(item, yyyymm, jsonResult):
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd'] # 지역코드
    sido = '' if 'sido' not in item.keys() else item['sido']  # 지역코드
    gungu = '' if 'gungu' not in item.keys() else item['gungu']  # 지역코드
    resNm = '' if 'resNm' not in item.keys() else item['resNm']  # 지역코드
    rnum = 0 if 'rnum' not in item.keys() else item['rnum']  # 지역코드
    Fornum = 0 if 'csForCnt' not in item.keys() else item['csForCnt']  # 지역코드
    NatNum = 0 if 'csNatCnt' not in item.keys() else item['csNatCnt']  # 지역코드

    jsonResult.append({'addrCd':addrCd,'sido':sido,'gungu':gungu,'resNm':resNm,
                       'rnum':rnum,'Fornum':Fornum,'NatNum':NatNum,'yyyymm':yyyymm})
    return None
def main():
    jsonResult = [] # 전체 목록을 저장할 리스트
    sido = '서울특별시' #
    gungu = '' #
    nPagenum = 1 # 페이지 번호
    nTotal = 0 # 조회된 전체 관광지의 갯수
    maxRecords = 100 # 조회된 레코드(행)의 최대 수
    nStartYear = 2015 # 검색 시작 년도
    nEndYear = 2019 # 검색 종료 년도

    for year in range(nStartYear,nEndYear+1):
        for month in range(1, 13):
            yyyymm = '%s%s' % (str(year),str(month).zfill(2))
            print(yyyymm)

            while(True):
                jsonData = getTourData(yyyymm,sido,gungu,nPagenum,maxRecords)
                print(jsonData)
                if jsonData['response']['header']['resultMsg'] == 'OK':
                    nTotal = jsonData['response']['body']['totalCount']
                    print(nTotal) # 조회된 결과수
                    if nTotal == 0 : break

                    for item in jsonData['response']['body']['items']['item']:
                        tourPointCorrection(item,yyyymm,jsonResult)

                    nPage = math.ceil(nTotal/100)
                    if(nPagenum==nPage):
                        break # 마지막 페이지에 도달했어요

                    nPagenum += 1
                else :
                    break
        # end inner for
    # end outer for

    savedFilename = 'concat_data/touristResourceStat(%s %d~%d).json'
    with open(savedFilename % (sido,nStartYear,nEndYear),'wt',encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult,indent=4, sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

    print(savedFilename + ' 파일 저장됨')
if __name__ == '__main__':
    main()