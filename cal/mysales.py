lists1 = list(map(str,input('품목,수량,단가 : ').split(',')))
lists2 = list(map(str,input('품목,수량,단가 : ').split(',')))

lists1[1],lists2[1] = int(lists1[1]),int(lists2[1])
lists1[2],lists2[2] = int(lists1[2]),int(lists2[2])
toc = lists1[1]+lists2[1]
to1 = lists1[1]*lists1[2]
to2 = lists2[1]*lists2[2]

form = f'''총 판매 대수 : {toc}
1번째 품목
{lists1[0]} : {to1:.1f}

2번째 품목
{lists2[0]} : {to2:.1f}
'''

print(form)