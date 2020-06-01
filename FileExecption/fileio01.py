#메모리의 효율을 더 좋게 하기위한 파일 생성 구문
#변수에 file 객체를 할당하는 것보다 메모리 사용이 효율적이다.
# with open 구문 as 파일별칭 :
#     읽거나 쓰기
#
# with 구문은 암시적으로 close()를 수행합니다.

with open('test.txt','w',encoding='utf-8') as myfile :
    myfile.write('메롱\n')
    myfile.write('하하\n')
    print('가나다라',file=myfile)
#with 구문은 close()하지 않아도 됩니다.

with open('test.txt','r',encoding='utf-8') as myfile :
    print(myfile.read())
#with 구문은 close()하지 않아도 됩니다.


print('finished')