examdata = [(50,70),(60,75),(55,80)]
for (midexam,finalexam) in examdata:
    print('중간고사 %d' %(midexam),end=' ')
    print('기말고사 %d' % (finalexam))

midsum = 0
finalsum = 0
for (midexam,finalexam) in examdata:
    midsum += midexam
    finalsum += finalexam
print(f'midsum : {midsum} finalsum : {finalsum}')

midsum = 0
finalsum = 0
for i in range(len(examdata)):
    midsum += examdata[i][0]
    finalsum += examdata[i][1]
print(f'midsum : {midsum} finalsum : {finalsum}')

fm,m,fmsum,msum = 0,0,0,0
somedata = [('홍길동','남자',100),('강감찬','남자',200),('박영희','여자',300),('신사임당','여자',400)]
for i in range(len(somedata)):
    if somedata[i][1] == '남자':
        fm += 1
        fmsum += somedata[i][2]
    else :
        m += 1
        msum += somedata[i][2]
print(f'남자 : {fm}명 , 여자 : {m}명\n남자 총점 : {fmsum} 여자 총점 : {msum/m:.0f}')
