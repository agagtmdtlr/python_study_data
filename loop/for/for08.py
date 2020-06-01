#시작 단수 : 4
#끝 단수 : 2
begins = int(input('시작 단수 : '))
ends = int(input('끝 단수 : '))
if begins > ends :
    begins,ends = ends,begins
for i in range(begins,ends+1):
    for j in range(1,10):
        print(f'{i}*{j}={i*j:2d}',end=' ')
    print()