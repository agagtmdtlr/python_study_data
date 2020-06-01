# 사용자의 실수나 문법적인 오류 사항들을 사전에 막음 조치하는것
# try :
#     개발자가 코딩하는 영역
# except:
#     예외 처리할 영역
# else:
#     예외가 발생하지 않으면 실행
# finally:
#     예외 발생 여부에 상관없이 무조건 실행

try:
    x = 4
    y = 2
    y += 'str'
    mylist = [1,2,3]
    print(mylist[5])
    z=x/y
    print(z)

    print('문제가 생기면 나는 실행이 안되요')
except ZeroDivisionError as err:
    print('#0으로 나누시면 안되요.')
    print(err)
except IndexError as err:
    print('#인덱싱 오류 발생.')
    print(err)
except Exception as err:
    print('나머지 오류 발생')
    print(err)
else:
    print('#예외 없으면 실행')
finally:
    print('나는 무조건 실행되요')