from pyy.databasees.sqllites.pactice.subClass import Employee
import csv

# 테스트용 모듈
# csv : comma separator value
em = Employee('mall.db')

em.getData()

with open(file='departments.csv',mode='r',encoding='EUC-KR') as file:
    csvdata = csv.reader(file)
    for data in csvdata:
        print(data)
