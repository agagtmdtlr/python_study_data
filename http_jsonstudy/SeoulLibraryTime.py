import urllib.request
import json
from pandas import DataFrame


url = 'http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTime/1/5/'
req = urllib.request.Request(url)
res = urllib.request.urlopen(req)
print(res) # <http.client.HTTPResponse object at 0x000002D9E6360C18>
# response document read()로 추출후
# decode()를 통해 byte 표현식을 str로 변환
res_str = res.read().decode()
print(res_str)
json_data = json.loads(res_str)
print(json_data.keys())
seoul = json_data['SeoulLibraryTime']
print(seoul.keys())
#dict_keys(['list_total_count', 'RESULT', 'row'])
# 데이터가 있는 'row'키의 값만 추출
row = seoul['row']
#dict_keys(['LBRRY_NAME', 'CODE_VALUE', 'ADRES', 'FDRM_CLOSE_DATE', 'TEL_NO', 'XCNTS', 'YDNTS'])
print(row[0].keys())
print(type(row[0].values()))
savedData = []
for line in row:
    savedData.append(list(line.values()))

cols = ['LBRRY_NAME', 'CODE_VALUE', 'address', 'FDRM_CLOSE_DATE', 'phone', 'latitude', 'longitude']
cols = [x.lower() for x in cols]

myframe = DataFrame(savedData,columns=cols)
myframe.to_csv('concat_data/seoullbrry.csv',index=False,encoding='utf-8')

# 지도에 표시해보기
import folium

# 서울 한 가운데를 기본 위치로 설정하기
maps = folium.Map([37.5642135,127.0016985], zoom_start=15)
# 저장한 리스트 데이터에서 위도 경도 가져오기
# or dataframe에서 가져 올수도 있음
for data in savedData:
    lat = data[-2]
    lon = data[-1]
    folium.Marker([lat,lon],popup=data[0],icon=folium.Icon(color='red',icon='info-sign')).add_to(maps)

filename = 'data/seoullbrry_map.html'
maps.save(filename)