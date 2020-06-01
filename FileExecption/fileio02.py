filename = 'test.txt'
myenc = 'utf-8'
try:
    print('#readline()함수 사용') #한줄씩 읽는다. 맨끝에 도달하면 None을 리턴해줍니다.
    myfile01 = open(file=filename,mode='rt',encoding=myenc)
    while True:
        line = myfile01.readline().strip('\n')
        if not line :
            break
        print(line)
    myfile01.close()
    print('#readlines()함수 사용') #모든 라인을 읽어서 list로 반환해 줍니다.
    myfile02 = open(file=filename, mode='rt', encoding=myenc)
    mylist = [text.strip() for text in myfile02.readlines()]
    print(mylist)
    myfile02.close()

    print('#read()함수 사용')
    myfile03 = open(file=filename, mode='rt', encoding=myenc)
    data = myfile03.read()
    print(data)
    myfile03.close()

except Exception as err:
    print(err)
finally:
    print('finished')