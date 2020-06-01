name = input('이름 입력 : ')
kor = int(input('kor 입력 : '))
eng = int(input('eng 입력 : '))
math = int(input('math 입력 : '))

total = kor+eng+math
avg = total/3

grade = '' # 학점 평가

if avg >= 90 :
    grade = 'A'
elif avg >= 80 :
    grade = 'B'
elif avg >= 70 :
    grade = 'C'
elif avg >= 60 :
    grade = 'D'
else:
    grade = 'F'

print(f'이름 : {name}\n'
      f'총점 : {total}\n'
      f'평균 : {avg:.0f}\n'
      f'학점 : {grade}')