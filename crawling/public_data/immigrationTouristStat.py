import json
import urllib.request
import datetime
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

plt.rc('font', family='Malgun Gothic')

access_key='ieU6gdettDBVUNo3lkXP8SqbMgC5fsExkGIVp7vFce1Yi6zPdMGjJ4Nk2QuEjRFj1fRG7IMDtPtH2Q4nN%2BLTtw%3D%3D'

def getRequestUrl(url):
    req = urllib.request.Request(url)
    
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
#             print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


#[CODE 1]
def getNatVisitor(yyyymm, nat_cd, ed_cd):
    # yyyymm : 6자리의 년월에 해당하는 날짜
    # nat_cd : 3자리 국가 코드(예 : 100, 275 등등)
    # ed_cd : 출국/입국 중에 하나(D:국민 해외 관광객, E:방한 외래 관광객)
    
    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    parameters = "?_type=json" # json 형식으로 ....
    parameters += "&serviceKey=" + access_key    
    parameters += "&YM=" + yyyymm # 년월 (p132 참고 요망)
    parameters += "&NAT_CD=" + nat_cd # 국가 코드
    parameters += "&ED_CD=" + ed_cd # 출국이냐 입국이냐~~ 
    
    url = end_point + parameters
    
    # print( '유알엘')
    # print( url )
    # print('-----------')
    
    retData = getRequestUrl(url)
    
    if (retData == None):
        return None
    else:
        return json.loads(retData)
    
def main():
    # 결과를 저장할 리스트
    # 요소들은 모두 사전 형식으로 되어 있다.
    jsonResult = [] 
    
    # 중국 : 112 / 일본 : 130 / 미국 : 275 / 영국 : 316
    nation = '미국'
    national_code = "275" # 나라별 코드
    ed_cd = "E" # 방한한 외국인 관광객

    nStartYear = 2015
    nEndYear = 2020
    
    for year in range(nStartYear, nEndYear):
        for month in range(1, 13):
            yyyymm = "{0}{1:0>2}".format(str(year), str(month))
            # print( yyyymm )
            jsonData = getNatVisitor(yyyymm, national_code, ed_cd)    
            # print( jsonData )

            print (json.dumps(jsonData, indent=4, 
                        sort_keys=True, ensure_ascii=False))

            if (jsonData['response']['header']['resultMsg'] == 'OK'):
                # krName : 국가명이다(미국, 일본, 중국)
                krName = jsonData['response']['body']['items']['item']["natKorNm"]
                krName = krName.replace(' ', '')
                
                # 총 방문 횟수
                iTotalVisit = jsonData['response']['body']['items']['item']["num"]
                print('%s_%s : %s' %(krName, yyyymm, iTotalVisit))
                jsonResult.append({'nat_name': krName, 'nat_cd': national_code,
                                 'yyyymm': yyyymm, 'visit_cnt': iTotalVisit})

    # 파일 저장 영역
    savefFilename = 'concat_data/immigrationTouristStat %s(%s)_(%d~%d).json'
    filename = savefFilename % (nation, national_code, nStartYear, nEndYear - 1)
    with open(filename, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print(filename + ' 파일 저장 완료')

    cnVisit = []
    VisitYM = []
    index = []
    i = 0
        
    for item in jsonResult:
        index.append(i)
        cnVisit.append(item['visit_cnt'])
        VisitYM.append(item['yyyymm'])
        i = i + 1
        
    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.xticks(index, VisitYM)
    plt.plot(index, cnVisit)
    plt.xlabel('방문월')
    plt.ylabel('방문객수')
    plt.grid(True)
    plt.show()    

if __name__ == '__main__':
    main()