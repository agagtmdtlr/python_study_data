print('# 파일에 기록합니다.')
myfile01 = open(file='newfile.txt',mode='w',encoding='utf-8')

for idx in range(1,11):
    data = '%2d번째 줄입니다.\n' %(idx)
    myfile01.write(data)

myfile01.close()

print('# 파일 여러 개 만들기')
for idx in range(1,11):
    filename = 'somefile'+str(idx).zfill(2)+'.txt'
    myfile = open(filename,'w',encoding='utf-8')
    data = '%2d번째 줄입니다.\n' %(idx)
    myfile.write(data)
    myfile.close()

print('# 기존 파일에 추가하기')
myfile02 = open('newfile.txt','a',encoding='utf-8')
for idx in range(11,101):
    data = '%3d 데이터가 들어가요.\n'%(idx)
    myfile02.write(data)
myfile02.close()
print('finished')