tuple01 = ('김철수',40,50,60)
tuple02 = ('박영희',50,60,70)

mytuple = (tuple01,tuple02)
print(mytuple)

total = len(mytuple)
name1 = mytuple[0][0]
name2 = mytuple[1][0]
jumsu1 = mytuple[0][1:]
jumsu2 = mytuple[1][1:]
kim_avg = sum(jumsu1)/len(jumsu1)
park_avg = sum(jumsu2)/len(jumsu2)
kor = jumsu1[0]+jumsu2[0]
eng = jumsu1[1]+jumsu2[1]
math = jumsu1[2]+jumsu2[2]

form = f'''총 인원수 : {total}
평균 점수
김철수 : {kim_avg:=.0f}
박영희 : {park_avg:=.0f}
과목별 총점
국어 : {kor}
영어 : {eng}
수학 : {math}'''

print(form)