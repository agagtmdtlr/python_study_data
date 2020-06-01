import folium
import urllib.request
import urllib.parse
import json

api_key = '234F63A6-F1CC-37A4-8F4A-A5143DEC0894'
address = '서울 마포구 신수동 451번지 세양청마루아파트 상가 101호'

base_url = 'http://api.vworld.kr/req/address?service=address&request=getCoord'
base_url += '&key='+api_key+'&'

values = {'address':address,'type':'PARCEL'}

parameter = urllib.parse.urlencode(values)
print(parameter)
print(type(parameter))

url = base_url+parameter
req = urllib.request.Request(url)
print(type(req))
response = urllib.request.urlopen(req)
print(type(response))
response_data = response.read().decode()
print(response_data)
print(type(response_data))

# json.loads : str을 json 형식으로 바꿔주는 gkatn
geo_info = json.loads(response_data)
print(type(geo_info))
# JSON
# {"response" :
#      {"service" :
#           {"name" : "address",
#            "version" : "2.0",
#            "operation" : "getCoord",
#            "time" : "634(ms)"},
#       "status" : "OK",
#       "input" :
#           {"type" : "PARCEL",
#            "address" : "서울 마포구 신수동 451번지 세양청마루아파트 상가 101호"},
#       "refined" :
#           {"text" : "서울특별시 마포구 신수동 451",
#            "structure" :
#                {"level0" : "", "level1" : "", "level2" : "", "level3" : "", "level4L" : "", "level4LC" : "", "level4A" : "", "level4AC" : "", "level5" : "", "detail" : ""}},
#       "result" :
#           {"crs" : "EPSG:4326",
#            "point" : {"x" : "126.936808841117", "y" : "37.5478305782939"}}}}
#

longtitude = geo_info['response']['result']['point']['x']
latitude = geo_info['response']['result']['point']['y']
print(tuple([longtitude,latitude]))
shopinfo = '교촌 신수점'
map_osm = folium.Map(location=[latitude,longtitude],zoom_start=16)
folium.Marker(location=[latitude,longtitude],popup=shopinfo,
              icon=folium.Icon(color='red',icon='info-sign')).add_to(map_osm)

folium.CircleMarker([latitude,longtitude],radius=150,color='blue',
                    fill_color='red',fill=False,popup=shopinfo).add_to(map_osm)

map_osm.save('concat_data/sinsookyochon.html')
