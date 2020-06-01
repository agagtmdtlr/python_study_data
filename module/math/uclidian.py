import math

def ulength(lists):
    ulist = []
    # for i in range(len(lists)):
    #     for j in range(i+1,len(lists)):
    #         ux = math.pow(lists[i][1]-lists[j][1],2)
    #         uy = math.pow(lists[i][2]-lists[j][2],2)
    #         u = math.sqrt(ux+uy)
    #         ulist.append((lists[i][0]+','+lists[j][0],u))

    for i in range(len(lists)):
        for j in range(i+1,len(lists)):
            u = math.hypot(lists[i][1]-lists[j][1],lists[i][2]-lists[j][2])
            ulist.append((lists[i][0] + ',' + lists[j][0], u))
    return ulist

mylist=[('짜장면',2,5),('짬뽕',2,4),('라면',4,5)]
ulist = ulength(mylist)
print(ulist)