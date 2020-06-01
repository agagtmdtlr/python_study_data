from pyy.databasees.sqllites.pactice.subClass import Department
# Department 데이터 넣은 후 조회

dbname = 'mall.db'
csvfile = 'departments.csv'
dept = Department(dbname,csvfile)

dept.insert()
mycursor = dept.getAllData()
for dno, name, locations, tel in mycursor:
    print(f'부서번호 : {dno}, '
          f'이름 : {name}, '
          f'위치 : {locations}, '
          f'번호 : {tel}')
print('finished')