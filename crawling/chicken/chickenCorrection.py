# 전처리를 하기위한 공용 모듈을 저장하고 있는 파일
import pandas as pd
import numpy as np

class Chickencorrection :
    myencoding = 'utf-8'

    def __init__(self,workfile):
        self.workfile = workfile # 작업 처리할 파일명
        # print(workfile)

        # 작업파일 df 변환
        self.myframe = pd.read_csv(self.workfile, encoding=self.myencoding)
        self.correctionSido()
        self.correctionGungu()
        self.showMergeResult()

        savedFile = 'studydata/allStoreModified.csv'
        self.myframe.to_csv(savedFile,encoding=self.myencoding)

    # 보정 처리 결과 확인 테스트 메소드
    def showMergeResult(self): # 표준 행정 구역과 비교
        district = pd.read_csv('studydata/district.csv',
                               encoding=self.myencoding)
        mergedData = pd.merge(self.myframe,district,on=['sido','gungu'],
                              how='outer',suffixes=['',' '],indicator=True)
        # print(mergedData)
        result = mergedData.query('_merge == "left_only"')
        print('좌측에만 있는 행')
        print(result[['sido','gungu','address']])
        print(self.myframe.loc[self.myframe['sido']=='인천광역시','gungu'].unique())
        print(type(result))
        # bad.csv : 표준 행정 구역과 다른 것들, 어떻게 수정해야 하나
        result[['sido','gungu','address']].to_csv('studydata/bad.csv',encoding=self.myencoding,index=False)
        pass

    def correctionSido(self):

        # print('before sido')
        # print(np.sort(self.myframe['sido'].unique()))

        sidofile = open('studydata/sido_correction.txt','r',encoding=self.myencoding)
        linelists = sidofile.readlines()

        sido_dict = {} # 시도 보정을 위한 사전
        for oneline in linelists :
            mydata = oneline.replace("\n",'').split(':')
            sido_dict[mydata[0]] = mydata[1]

        self.myframe.sido = self.myframe.sido.apply(lambda x : sido_dict.get(x,x))
        self.myframe = self.myframe.loc[self.myframe['sido']!='00']
        self.myframe = self.myframe.loc[self.myframe['sido'] != '테스트']
        # print('after sido')
        # print(np.sort(self.myframe['sido'].unique()))

    def correctionGungu(self):

        # print('before gungu')
        # print(self.myframe['gungu'].unique())

        sidofile = open('studydata/gungu_correction.txt', 'r', encoding=self.myencoding)
        linelists = sidofile.readlines()

        gungu_dict = {}  # 군구 보정을 위한 사전
        for oneline in linelists:
            mydata = oneline.replace("\n", '').split(':')
            gungu_dict[mydata[0]] = mydata[1]

        self.myframe.gungu = self.myframe.gungu.apply(lambda x: gungu_dict.get(x, x))
        # print('after gungu')
        # print(self.myframe['gungu'].unique())