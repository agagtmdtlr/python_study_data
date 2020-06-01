def mysum(a,b):
    return a+b

if __name__ == "__main__":
    print('내가 실행한 주체입니다.')
    su1 = 7
    su2 = 9
    print('더하기2 :',mysum(su1,su2))
    print('모듈', __name__, '종료됨')
else:
    print('다른 모듈이 나를 호출했네여')
    print('모듈',__name__,'종료됨')