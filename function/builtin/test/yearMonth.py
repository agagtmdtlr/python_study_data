def checkyear(i):
    result = str(i)
    if i > 50:
        result = '19'+result
    else:
        result = '20'+result
    return  result

mylist = [95,96,18,19]

newlist = [checkyear(i)+'년 '+str(j).zfill(2)+'월' for i in mylist for j in range(1,13)]
print(newlist)