# 외부 모듈을 불러오는 방법
#   from 경로1.경로2.외부모듈이름 import 함수이름
from pyy.module.outerModule import mysum

su1 = 3
su2 = 5
print('더하기 :',mysum(su1,su2))
print('모듈',__name__,'종료됨')