#반지름을 입력 받아서, 원의 면적과 둘레를 구하는 프로그램을 작성하세요
#면적은 소수점 2자리까지 , 둘레는 소수점 3자리까지 표현하세요
pi = 3.141592 # 원주율

# 반지름 : 5
# 둘레 : 2 * pi * 반지름 (31.416)
# 면적 : 반지름 ** 2 *pi (49.35)

radius = int(input('반지름 : '))
length = 2*radius*pi
area = (radius*radius)*pi
result = """반지름 : %d
둘레 : %.3f
면적 : %.2f"""
print(result %(radius,length,area))