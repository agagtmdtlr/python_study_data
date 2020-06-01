import urllib.request

url = 'https://uta.pw/shodou/img/28/214.png'
savename = 'concat_data/sample.png'

# retrieve 빼내다.
urllib.request.urlretrieve(url,savename)

print(url + '을',end='')
print(savename+'으로 저장')