import os, json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

# 상관 관계 분석 결과를 저장할 리스트
corr_list = []
mychart = './mychart/' # 차트들을 그래프로 저장할 폴더

# 상관계수 : correation
def correation(x, y):
    bar_x = x.mean()
    bar_y = y.mean()

    bunja = np.sum((x - bar_x)*(y- bar_y))
    print('분자 : '+str(bunja))

    left = np.sum((x-bar_x)**2)
    right = np.sum((y-bar_y)**2)
    bunmo = np.sqrt(left*right)
    print('분모 : '+str(bunmo))
    if bunmo == 0 :
        return 0
    else :
        return bunja/bunmo

def setScatterGraph(tour_table, visit_table, tourpoint):
    # 해당 관광지에 대한 각 나라의 상관 계수를 구하고, 산점도 그래프를 그려 줍니다.
    # tour_table(관광지 입장 정보)
    # visit_table(3개국 관광객수)
    # tourpoint : 관광지 이름(경복궁)

    # 'resNm' : 관광지 이름(경복궁)
    tour = tour_table[tour_table['resNm'] == tourpoint]
    merge_table = pd.merge(tour,visit_table,left_index=True,right_index=True)
    # print(merge_table)
    mylist = [['chaina','중국인'],['japan','일본인'],['usa','미국인']]

    fig = plt.figure()
    imsi = []
    imsi.append(tourpoint)

    print(tourpoint+'작업중')
    for onedata in mylist :
        plt.xlabel(onedata[1]+'입국 수')
        plt.ylabel('외국인 입장객 수')
        # print(merge_table)
        x = np.array(list(merge_table[onedata[0]])) # 중국인 방문객
        # print(x)
        y = np.array(list(merge_table['ForNum'])) # 관광지 외국인 방문객 수
        # print(y)
        corr = correation(x,y) # 상관계수

        corr = round(corr,6)

        if corr == 0 :
            print('상관 계수가 0입니다.')
            return
        # print(corr)
        # 경복궁-중국인 상관 관계 분석(0.123456)
        plt.title(f'{tourpoint}-{onedata[1]} 상관 관계 분석({corr:=.6f})')
        print(len(list(merge_table[onedata[0]])))
        print(len(list(merge_table['ForNum'])))
        plt.scatter(list(merge_table[onedata[0]]),list(merge_table['ForNum']),
                    edgecolors='none',alpha=0.7,s=6,c='black')
        # ./mychart/+경복궁 ( 중국인 ).png
        fig.savefig(mychart+tourpoint+'('+onedata[1]+').png')
        mytuple = (onedata[1], corr)
        imsi.append(mytuple)

    corr_list.append(imsi)
def main():
    # 각 나라의 파일을 읽어서 하나의 데이터 플레임으로 합칩니다.


    if not os.path.exists(mychart):
        os.mkdir(mychart)

    myfile = 'concat_data/touristResourceStat(서울특별시 2015~2019).json'
    jsonTable = json.loads(open(myfile,'rt',encoding='utf-8').read())
    # print(jsonTable)
    tourTable = pd.DataFrame(jsonTable,columns=('yyyymm','resNm','ForNum'))
    tourTable = tourTable.set_index('yyyymm')

    
    myfile = 'concat_data/immigrationTouristStat 미국(275)_(2015~2019).json'
    jsonTable = json.loads(open(myfile, 'rt', encoding='utf-8').read())
    usaTable = pd.DataFrame(jsonTable,columns=('yyyymm','visit_cnt'))
    usaTable = usaTable.rename(columns={'visit_cnt':'usa'})
    usaTable = usaTable.set_index('yyyymm')
    # print(usaTable)

    myfile = 'concat_data/immigrationTouristStat 일본(130)_(2015~2019).json'
    jsonTable = json.loads(open(myfile, 'rt', encoding='utf-8').read())
    jpanTable = pd.DataFrame(jsonTable, columns=('yyyymm', 'visit_cnt'))
    jpanTable = jpanTable.rename(columns={'visit_cnt': 'japan'})
    jpanTable = jpanTable.set_index('yyyymm')
    # print(jpanTable)
    
    myfile = 'concat_data/immigrationTouristStat 중국(112)_(2015~2019).json'
    jsonTable = json.loads(open(myfile, 'rt', encoding='utf-8').read())
    chainaTable = pd.DataFrame(jsonTable, columns=('yyyymm', 'visit_cnt'))
    chainaTable = chainaTable.rename(columns={'visit_cnt': 'chaina'})
    chainaTable = chainaTable.set_index('yyyymm')
    # print(chainaTable)

    fv_table = pd.merge(chainaTable,jpanTable,left_index=True,right_index=True)
    fv_table = pd.merge(fv_table, usaTable, left_index=True, right_index=True)

    # print(fv_table.index)

    resNm = tourTable.resNm.unique()
    for tourpoint in resNm  :
        # tourpoint : 관광지(경복궁...)
        # 두 테이블의 상관계수 구하기
        setScatterGraph(tourTable,fv_table,tourpoint)

if __name__ == '__main__':
    main()