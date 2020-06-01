def triangle(myliist):
    result=[]
    for i in mylist:
        l = sorted(i)
        if i[2]>(i[0]+i[1]):
            result.append('불충분')
        else:
            s = pow(i[0],2)+pow(i[1],2)
            b = pow(i[2],2)
            if b > s :
                result.append('둔각')
            elif b < s :
                result.append('예각')
            else:
                result.append('직각')
    return result

mylist = [(3.0,4.0,5.0),(5.0,12.0,10.0),(1.0,2.0,100.0),(7.0,20.0,25.0)]

result = triangle(mylist)
print(result)