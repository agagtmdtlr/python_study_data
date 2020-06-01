def myfunc(su1,su2):
    if su2 == 0 :
        x = su1
    else :
        x = su1//su2
    return (su1+su2,su1-su2,su1*su2,x)

su1 = 14
su2 = 5
result = myfunc(14,5)
print(type(result),result)
print(myfunc(14,0))
