import folium
map = folium.Map(location=[38.35,-99.09], zoom_start=6, tiles="Stamen Terrain") #this creates the coordinates and add tiles to the map
map.add_child(folium.Marker(location=[38.2,-99.1], popup="Hi I am a Marker", icon=folium.Icon(color="green"))) #this adds a market on the map object
map.save("Map1.html") #this saves the map as html which makes the images reflect on a browser tab

#This is another way to add child objects. It is neater
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location= [38.2,-99.1], popup="Hi I am a Marker", icon=folium.Icon(color="green")))
map.add_child(fg)
map.save("Map1.html")

#How to add multiple markers on your map with the for loop
for coordinates in [[38.2, -99.1],[39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color="green")))
map.add_child(fg)
map.save("Map1.html")

#How to get the lat & lon data from a csv file
import pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
map = folium.Map(location=[38.35,-99.09], zoom_start=6, tiles="Stamen Terrain") #this creates the coordinates and add tiles to the map
fg = folium.FeatureGroup(name="My Map")
for lt, ln in zip(lat, lon): #this does the iterations
    fg.add_child(folium.Marker(location=[lt,ln], popup="Hi I am a Marker", icon=folium.Icon(color="green")))
map.add_child(fg)
map.save("Map1.html")

#How to make the elevation points on the VOlcanoes text doc the maker pop ups
import pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
map = folium.Map(location=[38.35,-99.09], zoom_start=6, tiles="Stamen Terrain") #this creates the coordinates and add tiles to the map
fg = folium.FeatureGroup(name="My Map")
for lt, ln, el in zip(lat, lon, elev): #this does the iterations
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+" m", icon=folium.Icon(color="green"))) #the str(el) converts el to a string instead of float
map.add_child(fg)
map.save("Map1.html")
