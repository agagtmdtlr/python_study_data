fruits = [('바나나', 10), ('수박', 20), ('사과', 30),
          ('수박', 30), ('사과', 50), ('오렌지', 15)]
mydict = dict()
for name,cnt in fruits:
    if mydict.get(name) is not None :
        mydict[name] = mydict[name] + cnt
    else:
        mydict[name] = cnt
print(mydict)

mydict = dict()
for name,cnt in fruits:
    if name in mydict :
        mydict[name] = mydict[name] + cnt
    else:
        mydict[name] = cnt
print(mydict)