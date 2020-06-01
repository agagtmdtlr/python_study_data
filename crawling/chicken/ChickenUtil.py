import time
import datetime
import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd
from selenium import webdriver

class ChickenStore:
    mycolumns = ['brand','store','sido','gungu','address']
    myencoding = 'utf-8'
    def __init__(self,brandName,url):
        self.brandName = brandName
        self.url = url

        if self.brandName != 'goobne':
            self.soup = self.get_request_url()
            # self.wd = None
        else : # 굽네 치킨
            self.soup = None
            filepath='d:/chromedriver.exe'
            self.driver = webdriver.Chrome(filepath)
            self.driver.get(url)

    def getWebDriver(self,cmdJavaScript):
        self.driver.execute_script(cmdJavaScript)
        wait = 5
        time.sleep(5)
        mypage = self.driver.page_source
        #getPageSource()

        return BeautifulSoup(mypage,'html.parser')

    def get_request_url(self):
        try:
            response = urllib.request.urlopen(self.url)
            if response.getcode() == 200 : # 응답 ok
                return response
            else :
                return None
        except Exception as err:
            print(err)
            now = datetime.datetime.now()
            msg = '[%s] error for url %s' % (now,self.url)
            print(msg)
            return None

    def getSoup(self):
        if self.soup == None :
            return None
        else :
            return BeautifulSoup(self.soup,'html.parser') # default html.parser



    def save2Csv(self,savedData):
        data = DataFrame(savedData,columns=self.mycolumns)
        data.to_csv('concat_data/'+self.brandName+'.csv',encoding=self.myencoding,index=True)
        print('생성됨')