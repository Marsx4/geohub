from django.shortcuts import render
import folium
from folium.plugins import MarkerCluster,BeautifyIcon
#from .models import Facility
import pandas as pd
import os

def home(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #read external files
    data=pd.read_excel(os.path.join(BASE_DIR,"final.xlsx"))
    districts=os.path.join(BASE_DIR,"districts.geojson")
    provinces=os.path.join(BASE_DIR,"provinces.geojson")

    cso_names=[]
    for index,row in data.iterrows():
        
        name=str(row['cso_name'])
        name=name.replace(",","")
        cso_names.append(name)
    #unique csos    
    cso_names=list(set(cso_names))
    #colors
    colors=['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray','green','brown','red']
    #create the map
    m=folium.Map(location=[data['lat'].mean(),data['lon'].mean()],zoom_start=6)
    #track cso index for color coding
    cso_index=0
    org_legend=""""""
    for name in cso_names:
        name+=","
        org_df=data.loc[data['cso_name']==name]
        name=name.replace(",","")
        #create cluster for each cso
        mc=MarkerCluster(name=name)
        #create marker and add to cluster
        for i,row in org_df.iterrows():
            #add to database
            html=f"<div><div class='card-panel center-align pink-text'><b>Name</b><br> {row['cso_name']}<br><b>Estab.</b><br>{row['year_joined']}<br><b>Phone </b><br>{row['phone']}<br><b>Focus</b><br>{row['focus']}<br><b>Service(s)</b><br>{row['service_type']}</div><br><a href='localhost:8000/detail/{row['cso_name']}' target='top'>More Info</a></div>"
            iframe=folium.IFrame(html=html,width=500,height=200)
            marker=folium.Marker([row['lat'],row['lon']],folium.Popup(iframe,max_width=500),tooltip=row['cso_name'],icon=folium.Icon(color=colors[cso_index]))
            mc.add_child(marker)
            
        #add cluster to map
        m.add_child(mc)
        cso_index+=1
        #add to legend
        org_legend+=f"""&nbsp;<span style='color:{colors[cso_index]}'> <strong>{row['cso_name']}</strong> </span> &nbsp;<br>"""
    #add districts and provinces
    folium.GeoJson(districts,name="Districts").add_to(m)
    folium.GeoJson(provinces,name="Provinces").add_to(m)
    #add layer control    
    folium.LayerControl().add_to(m)

    legend_html = """
     <div style='position: fixed;background-color:white;color:black; 
     top: 100px; left: 10px; width: 370px; min-height: 90px; 
     border:1px solid grey; z-index:9999; font-size:14px;border-radius:4px;
     font-size:12px;'><br>&nbsp;&nbsp;<strong>Legend</strong><br><br>
     """
    legend_html+=org_legend
    legend_html+="""<br></div>"""

    m.get_root().html.add_child(folium.Element(legend_html))
    #generate map
    m.save("mysite/static/html/map.html")
    #return the view
    return render(request,'home.html',{})

def detail(request,organization):
    org_name=organization
    #get data about the organization
    #create context
    context={"name":org_name}
    #render page
    return render(request,'detail.html',context)