import folium
import json
import urllib.parse
import urllib.request
import pandas as pd

api_key = '234F63A6-F1CC-37A4-8F4A-A5143DEC0894'
base_url = 'http://api.vworld.kr/req/address?service=address&request=getCoord'
base_url += '&key='+api_key+'&'

def getGeoCoder(address):
    # 주소에 대한 위도와 경도를 tuple 형태로 반환합니다.

    # PARCEL : 지번주소, ROAD: 도로명주소
    values = {'address':address, 'type':'PARCEL'}

    parameter = urllib.parse.urlencode(values)
    url = base_url+parameter
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        response_data = response.read().decode()
        # print(response_data) # 무슨 format인지 분석하자.

        geo_info = json.loads(response_data)
        # print(geo_info)

        longitude = geo_info['response']['result']['point']['x']
        latitude = geo_info['response']['result']['point']['y']
        print('('+longitude+', '+latitude+')')
        return (latitude,longitude)

    except KeyError as err:
        # print(err)
        return None
    except Exception as err:
        # print(err)
        print(response.getcode())
        return None


def makeMap(brand, store, geoInfo):
    # 브랜드이름(brand), 상호명(store), 위도경도(geoInfo)

    brand_dict = {'cheogajip': '처갓집', 'goobne': '굽네', 'kyochon': '교촌', 'nene': '네네', 'pelicana': '페리카나'}
    shopinfo = store + '('+brand_dict[brand]+')' # 가게이름(브랜드)
    mycolor = {'nene':'red','goobne':'blue','pelicana':'yellow','kyochon':'pink','cheogajip':'green'}
    marker = folium.Marker(geoInfo,popup=shopinfo,icon=folium.Icon(color=mycolor[brand],icon='info-sign')).add_to(mapObject)


# 지도의 기준점
mylatitude = 37.56
mylongitude = 126.92
mapObject = folium.Map([mylatitude,mylongitude],zoom_start=13)



csv_file = 'data/allStoreModified.csv'
myframe = pd.read_csv(csv_file, index_col=0, encoding='utf-8')

# 마포구의 교촌만 ....
where = '마포구'
brandName = 'kyochon'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName

mapData = myframe.loc[condition1 & condition2]
print(mapData)

for idx in range(len(myframe.index)):
    brand = myframe.iloc[idx]['brand']
    store = myframe.iloc[idx]['store']
    address = myframe.iloc[idx]['address']
    geoInfo = getGeoCoder(address)
    if geoInfo == None:
        print(address)
    else :
        # print('오케이 :' + brand + ' '+address)
        makeMap(brand,store,geoInfo)

filename = 'data/mapresult.html'
mapObject.save(filename)