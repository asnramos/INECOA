# Import libraries
import pandas as pd
import folium
import os
 
# Load the shape of the zone (US states)
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
# You have to download this file and set the directory where you saved it
state_geo = os.path.join('D:/00000-MARCOS-VAIRA/SCRIPTS/ecorregiones-info/', 'us-states.json')
 
# Load the unemployment value of each state
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
state_unemployment = os.path.join('D:/00000-MARCOS-VAIRA/SCRIPTS/ecorregiones-info/', 'US_Unemployment_Oct2012.csv')
state_data = pd.read_csv(state_unemployment)
 
# Initialize the map:
m = folium.Map(location=[37, -102], zoom_start=5)
#m = folium.Map(location=[-23.5791908, -65.404902], zoom_start = 8)
 
# Add the color for the chloropleth:
m.choropleth(
 geo_data=state_geo,
 name='Capa_EEUU',
 data=state_data,
 columns=['State', 'Unemployment'],
 key_on='feature.id',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.2,
 legend_name='Unemployment Rate (%)'
)
folium.LayerControl().add_to(m)
 
# Save to html
m.save('folium_chloropleth_USA2.html')
