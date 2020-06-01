mydict = dict()
while True:
    name = input('이름 입력 : ')
    if name == 'quit': break
    age = int(input('나이 입력 : '))
    mydict[name] = age
print(mydict)