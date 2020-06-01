def myfunction(a,b=10,*args,**kwargs):
    print(f'a={a}\nb={b}\nargs={args}\nkwarge={kwargs}')
    print('\n'.join(map(str,args)))
    print('튜플 출력')
    for item in args:
        if type(item) == str :
            print('문자열 : ',item)
        elif type(item) == int :
            print('정수 : ',item)
        elif type(item) == float :
            print('실수 ; ',item)
        else:
            print('기타 : ',item)


myfunction(10, 20, 30, 'abc', 12.345, 50, kim=40, park=30)