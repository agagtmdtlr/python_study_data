name = input('이름 입력 : ')
score = int(input('점수 입력 : '))
grade = '' # 학점 평가

if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else:
    grade = 'F'

print(f'이름 : {name}\n'
      f'점수 : {score}\n'
      f'학점 : {grade}')