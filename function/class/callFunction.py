def square(su):
    return pow(su,2)
def getmax(su1,su2):
    # return max(su1,su2)
    result = 0
    if su1 > su2:
        result = su1
    else:
        result = su2
    return result
def sub(su1,su2):
    return su1-su2
def squareHab(su1,su2):
    return square(su1)+square(su2)

su1 = 3
su2 = 6
newsu1 = squareHab(su1,su2)
print(square(su1),square(su2),getmax(su1,su2),newsu1,sub(newsu1,6))