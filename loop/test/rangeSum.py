beginnum,endnum = map(int,input('시작, 끝 : ').split(','))
if beginnum > endnum :
    beginnum,endnum = endnum,beginnum
print(sum(range(beginnum,endnum+1)))