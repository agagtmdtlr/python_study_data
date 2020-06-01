myenc = 'utf-8'
sample = [70,60,50,30,20]
with open(file='sample.txt',mode='w',encoding=myenc) as file:
    file.write('\n'.join(map(str,sample)))

with open(file='sample.txt',mode='r',encoding=myenc) as file:
    lines = [int(i.strip()) for i in file.readlines()]
    sumsam = sum(lines)
    avgsam = sumsam/len(lines)

with open(file='result.txt',mode='w',encoding=myenc) as file:
    file.write('총합 : {}\n'.format(sumsam))
    file.write('평균 : {}\n'.format(avgsam))
