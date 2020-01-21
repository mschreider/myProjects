import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
#html = """<h4>Volcano information:</h4>
#Height: %s m
#"""

def color_producer(elevation):
    if el > 3000:
        return 'red'
    elif el < 3000 and el > 1000:
        return 'orange'
    elif el < 1000:
        return 'green'

map = folium.Map(location=[38.58, -99.09],zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

#for i, j in zip([1,2,3], [4,5,6]):
#    print(i, "and", j)

for lt, ln, el in zip(lat, lon, elev):
    
    #iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    #fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + "m", 
    fill_color=color_producer(el), color="grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")