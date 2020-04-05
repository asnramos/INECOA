import pandas as pd
import folium

from folium.map import *
from folium import plugins
from folium.plugins import MeasureControl
from folium.plugins import FloatImage
from folium.plugins import MarkerCluster

datos = pd.read_csv('COORDENADAS-INECOA.tsv', delimiter="\t", encoding='utf-8') #encoding="latin-1"
print(list(datos.columns.values))

#datos.columns = ['Unnamed: 0', 'Latitud', 'Longitud', 'Altura', 'Taxa', 'Mes', 'Anio', 'Titulo', 'Descripcion', 'Institucion', 'Fuente', 'Contacto']

datos.columns = ['Unnamed: 0', 'Unnamed: 0.1', 'Latitud', 'Longitud', 'Altura', 'Taxa', 'Mes', 'Anio', 'Titulo', 'Descripcion', 'Institucion', 'Fuente', 'Contacto']

mapa = folium.Map(location=[-23.5791908, -65.404902], zoom_start = 8)

marker_cluster = folium.plugins.MarkerCluster(name="INECOA").add_to(mapa)

locations = datos[['Latitud', 'Longitud']]
locationlist = locations.values.tolist()

##for point in range(0, len(locationlist)):
##    folium.Marker(locationlist[point], popup=datos['Altura'][point]).add_to(mapa)
##    print(point)
##
##
for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point], popup=datos['Titulo'][point]).add_to(marker_cluster)
    print(point)

datos02 = pd.read_csv('COORDENADAS-UNT.tsv', delimiter="\t", encoding='utf-8') #encoding="latin-1"
print(list(datos02.columns.values))

#datos.columns = ['Unnamed: 0', 'Latitud', 'Longitud', 'Altura', 'Taxa', 'Mes', 'Anio', 'Titulo', 'Descripcion', 'Institucion', 'Fuente', 'Contacto']

datos02.columns = ['Unnamed: 0', 'Unnamed: 0.1', 'Latitud', 'Longitud', 'Altura', 'Taxa', 'Mes', 'Anio', 'Titulo', 'Descripcion', 'Institucion', 'Fuente', 'Contacto']

marker_cluster02 = folium.plugins.MarkerCluster(name="UNT").add_to(mapa)

locations02 = datos02[['Latitud', 'Longitud']]
locationlist02 = locations02.values.tolist()

for point02 in range(0, len(locationlist02)):
    folium.Marker(locationlist02[point02], popup=datos02['Altura'][point02]).add_to(marker_cluster02)
    print(point02)


folium.TileLayer(tiles='Stamen Toner',name="Modo Toner").add_to(mapa)
folium.TileLayer(tiles='Stamen Terrain',name="Modo Terreno").add_to(mapa)
folium.LayerControl().add_to(mapa)

#mapa.add_child(MeasureControl())
mapa.save('mapainecoa13.html')
