import folium
import pandas as pd
data = pd.read_csv("Volcanoes_USA.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

def get_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

for lat, lon, elev in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location = [lat, lon], radius=5, popup=str(elev) + "m", color = get_color(elev), fill = True, fill_color = get_color(elev), fill_opacity = 0.8))

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))

map.add_child(fg)
map.save("Map1.html")
