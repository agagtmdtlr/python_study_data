#부서와 사원테이블 조인
from pyy.databasees.sqllites.pactice.subClass import Composite

obj = Composite('mall.db')
result = obj.getData()
# print(result)

for dname, ename, jikcode in result:
    print(f'부서명 : {dname}, '
          f'이름 : {ename:}, '
          f'직급 : {jikcode}')