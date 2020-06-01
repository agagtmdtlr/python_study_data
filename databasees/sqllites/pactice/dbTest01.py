# 3가지 테이블 생성
from pyy.databasees.sqllites.pactice.superClass import SuperDao

dbname = 'mall.db'

mydb = SuperDao(dbname)
mydb.createTable()
print('finished')