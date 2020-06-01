# 파일 : asdf.txt을 읽어 들일 때, 파일이 존재않을 때 예외처리
# 의도적으로 예외 발생 시키기
# raise Exception('문자열')
try:
    myfile= open('asdf.txt',mode='r',encoding='utf-8')

    print('읽었다고 치고....')
    print(myfile.read())
    myfile.close()

    print('finished')
except FileNotFoundError as err:
    print(err)
    print('찾으시는 파일이 없습니다.')

else:
    print('no FileExecption')
finally:
    pass