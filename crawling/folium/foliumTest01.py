import folium

latitude = 37.566345
longitude = 126.977893

map_osm = folium.Map(location=[latitude,longitude])
print(type(map_osm))
map_osm.save('concat_data/map1.html')

map_osm = folium.Map(location=[latitude,longitude],zoom_start=16)
map_osm.save('concat_data/map2.html')

map_osm = folium.Map(location=[latitude,longitude],zoom_start=17,tiles='Stamen Terrain')
map_osm.save('concat_data/map3.html')

map_osm = folium.Map(location=[latitude,longitude],zoom_start=17)
folium.Marker([latitude,longitude],
              popup='서울 시청',
              icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)
map_osm.save('concat_data/map4.html')

folium.CircleMarker([37.566345,126.977893], radius=150,color='blue',
                    fill_color='red', fill=False, popup='덕수궁').add_to(map_osm)
map_osm.save('concat_data/map5.html')
print('finsihed')