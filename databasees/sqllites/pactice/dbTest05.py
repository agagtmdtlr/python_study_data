from pyy.databasees.sqllites.pactice.subClass import Department
# Department 데이터 넣은 후 조회

dbname = 'mall.db'
dept = Department(dbname)

dept.update(10,'판매부')

print('finished')
