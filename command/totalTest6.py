# diseaseCheck.pyy
# 고혈압/당뇨병 판정 프로그램
# 이름과 혈압 수치와 혈당 수치를 입력 받고,
name,press,ph = input('이름,혈압,혈당 : ').split(',')
press = int(press)
ph = int(ph)
result1 = list()
# 다음 공식에 의하여 결과를 출력하는 프로그램을 작성하세요.
# '혈압 수치'가 140이상이면 '고혈압'이고, 90이하이면
# '저혈압'이라고 합니다.
# '혈당'이 120 이상이면 '당뇨병'을 의심해봐야 합니다.
if press <= 90 :
    result1.append('저혈압')
elif press >= 140 :
    result1.append('고혈압')
if ph >= 120 :
    result1.append('당뇨병')
if len(result1) is 0 :
    print(f'{name} 님은 의심되는 질환인 없습니다.')
else :
    print(f'{name} 님은 {"과 ".join(result1)}이 있습니다')
# 예시 01
# 혈압 수치 : 150
# 혈당 수치 : 130
# 김유신 님은 고혈압과 당뇨병이 있습니다.
# 예시 02
# 혈압 수치 : 130
# 혈당 수치 : 100
# 이순신 님은 의심되는 질환이 없습니다.