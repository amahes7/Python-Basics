import folium
import pandas

map= folium.Map(location=[10,10], zoom_start = 3 )
volcano_location = pandas.read_csv("volcanoes.txt")
lat = list(volcano_location.loc[:,"LAT"])
lon = list(volcano_location.loc[:,"LON"])
name= list(volcano_location.loc[:,"NAME"])
elev= list(volcano_location.loc[:,"ELEV"])
status = list(volcano_location.loc[:,"STATUS"])
location = list(volcano_location.loc[:,"LOCATION"])

def color_specification(elev):
    if(elev < 2000):
        return 'green'
    elif(2000 <= elev <=3000):
        return 'black'
    else:
        return 'red'

html = """<h4>Volcano information:</h4><HR>
Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Elevation: %s el
Status: %s status
Location: %s location
"""
fg = folium.FeatureGroup(name="Volcano")

for lt,ln,name,el,status,location in zip(lat,lon,name,elev,status,location):
    iframe = folium.IFrame(html = html % (name,name,el,status,location), width= 200, height =150)
    fg.add_child(folium.Marker(location =[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color=color_specification(el)))) 
    #fg.add_child(folium.CircleMarker(location =[lt,ln],popup=folium.Popup(iframe),fill_color=color_specification(el),fill=True,fill_opacity=0.5)) 

fg2 = folium.FeatureGroup(name="World Population")
fg2.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
style_function = lambda x:{'fillColor':'red' if x['properties']['POP2005'] <2000000 
else 'blue' if 2000000 <= x['properties']['POP2005'] < 10000000 
else 'green'}))

map.add_child(fg)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("Map3.html")