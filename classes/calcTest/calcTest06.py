class Saram:

    nation = '대한민국' # 클래스 변수

    def __init__(self):
        print('생성자')

    def __del__(self):
        print('소멸자')

    def showInfo(self):
        name = '한국인'
        print(name)

soo = Saram() # 객체 인스턴스쉐이션 (실체화)
print('국적 01',soo.nation)
print('국적 02',Saram.nation)

print('메소드 호출')
print('Bound Method Call : ', soo.showInfo()) # 연결고리가 있다 : 바운딩
print('UnBound Method Call : ',Saram.showInfo(soo)) # 연결고리가 없어 직접 연결 : 언 바운딩

print(isinstance(soo,Saram))