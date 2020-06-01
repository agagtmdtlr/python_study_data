# 판매부 직원들의 고객 정보
from pyy.databasees.sqllites.pactice.subClass import Composite

obj = Composite('mall.db')
result = obj.getData3('판매부')

for cid,name,tel in result:
    print(f'아이디 : {cid}, '
          f'고객 이름 : {name}, '
          f'번호 : {tel}')