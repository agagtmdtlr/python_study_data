import urllib.request

url = 'https://uta.pw/shodou/img/28/214.png'
savename = 'concat_data/sample2.png'

result = urllib.request.urlopen(url)
print(type(result))
#<class 'http.client.HTTPResponse'>

print(result.geturl())
# https://uta.pw/shodou/img/28/214.png
print('-'*30)

print(result.info())
print('-'*30)

# request 성공 여부 판단
print(result.getcode()) # http응답코드: 200(성공)
print('-'*30)

# info value를 리스트[튜플] 형태로 반환
print(result.getheaders())
print('-'*30)

data = result.read() # 바이트 형태로 변환
print(type(data)) # <class 'bytes'>
# mode = 'b' : binaray type으로 작업ㅎ나다.
with open(savename, mode='wb') as f :
    f.write(data)
    print(savename+'파일로 저장')
