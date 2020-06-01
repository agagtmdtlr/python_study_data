a,b = map(int,input('가로,높이 : ').split(','))
lists = list(map(int,input('가로,높이 : ').split(',')))
leng = (a+b)*2
area = a*b

format1 = f'''가로 : [{a:^10}]
높이 : [{b:^10}]
둘레 : [{leng:^10}]
넓이 : [{area:^10}]'''

print(format1)

leng = (lists[0]+lists[1])*2
area = lists[0]*lists[1]

format1 = f'''가로 : [{lists[0]:^10}]
높이 : [{lists[1]:^10}]
둘레 : [{leng:^10}]
넓이 : [{area:^10}]'''

print(format1)