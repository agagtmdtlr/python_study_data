# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) / sys.stdout:모니터
print('안녕','반가워')
print('안녕','반가워',sep='^^',end=' ')
print('안녕','반가워',sep='#')

# round(number[, ndigits])
su = 12.34567
print(round(su))
print(round(su,2))
print(round(su,-1))

# abs(x) x : 스칼라 데이터 (한개의 원소)
mylist = [10,-20]
print(ascii(mylist))
# print(abs(mylist))

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# TypeError: open() missing required argument 'file' (pos 1) /
# required argument : pos 1
somfile = 'aaa.txt'
myfile = open(file=somfile)
print(type(myfile))
print(myfile)
print(next(myfile))