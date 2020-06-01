#이순신 이가 당당 고객
from pyy.databasees.sqllites.pactice.subClass import Composite

obj = Composite('mall.db')
result = obj.getData2('이순신')

for cid,name,tel in result:
    print(f'아이디 : {cid}, '
          f'고개 이름 : {name}, '
          f'번호 : {tel}')