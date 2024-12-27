import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import st_folium
import pandas as pd
from shapely import wkt

graffiti1 = Image.open("Images/Leapers1.jpg")
palazzo1 = Image.open("Images/Palazzo1.jpg")
palazzo2 = Image.open("Images/Palazzo2.jpg")
palazzo3 = Image.open("Images/Palazzo3.jpg")
palazzo4 = Image.open("Images/palazzo4.jpg")
piscina1 = Image.open("Images/piscina1.jpg")
piscina2 = Image.open("Images/piscina2.jpg")
piscina3 = Image.open("Images/piscina3.jpg")
piscina4 = Image.open("Images/piscina4.jpg")
reel_palazzo1 = open("Images/ReelPalazzo.mp4", "rb")
reel_palazzo1 = reel_palazzo1.read()
BlueMarkers = 'csv/BlueMarkersR.csv'
CoveredSpots = "csv/CoveredSpotsR.csv"
DecentSpots = "csv/DecentSpotsR.csv"
GoodSpots = "csv/GoodSpotsR.csv"
MilansFinest = "csv/MilansFinestR.csv"
bm = pd.read_csv(BlueMarkers)
cs = pd.read_csv(CoveredSpots)
ds = pd.read_csv(DecentSpots)
gs = pd.read_csv(GoodSpots)
mf = pd.read_csv(MilansFinest)


def estrai_poligono(wkt_str):
    if isinstance(wkt_str, str) and wkt_str.startswith("POLYGON"):
        try:
            coords = wkt_str.replace("POLYGON ((", "").replace("))", "").split(", ")
            return [[float(c.split()[1]), float(c.split()[0])] for c in coords]
        except Exception as e:
            st.write(f"Errore durante l'estrazione del poligono: {e}")
            return None
    return None






def blue_markers():
    added_points = set()
    for _, row in bm.dropna(subset=['latitudine', 'longitudine']).iterrows():
        lat, lon = row['latitudine'], row['longitudine']

        if (lat, lon) in added_points:
            continue

        # Aggiungi il marker
        folium.Marker(
            location=[lat, lon],
            popup=f"{row['name']}<br>{row['description']}",
            tooltip=row['name'],
            icon=folium.Icon(color="blue", icon="")
        ).add_to(map)

        poligono_coords = estrai_poligono(row['WKT'])
        if poligono_coords:
            # Aggiungi il poligono
            folium.Polygon(
                locations=poligono_coords,
                color="blue",
                fill=True,
                fill_color="blue",
                fill_opacity=0.3,
                tooltip=row['name']
            ).add_to(map)

            # Aggiungi solo un marker per il primo punto del poligono
            first_point = poligono_coords[0]
            if (first_point[0], first_point[1]) not in added_points:
                folium.Marker(
                    location=first_point,
                    popup=f"{row['name']}<br>{row['description']}",
                    tooltip=row['name'],
                    icon=folium.Icon(color="blue", icon="")
                ).add_to(map)
                added_points.add((first_point[0], first_point[1]))

        added_points.add((lat, lon))






def covered_spots():
    added_points = set()
    for _, row in cs.dropna(subset=['latitudine', 'longitudine']).iterrows():
        lat, lon = row['latitudine'], row['longitudine']

        if (lat, lon) in added_points:
            continue

        # Aggiungi il marker
        folium.Marker(
            location=[lat, lon],
            popup=f"{row['name']}<br>{row['description']}",
            tooltip=row['name'],
            icon=folium.Icon(color="black", icon="")
        ).add_to(map)

        # Aggiungi il punto all'insieme
        added_points.add((lat, lon))







def decent_spots():
    added_points = set()
    ds_unique = ds.drop_duplicates(subset=['latitudine', 'longitudine'])

    for _, row in ds_unique.dropna(subset=['latitudine', 'longitudine']).iterrows():
        lat, lon = row['latitudine'], row['longitudine']

        if (lat, lon) in added_points:
            continue
        poligono_coords = estrai_poligono(row['WKT'])
        if poligono_coords:
            # Aggiungi il poligono
            folium.Polygon(
                locations=poligono_coords,
                color="green",
                fill=True,
                fill_color="green",
                fill_opacity=0.3,
                tooltip=row['name']
            ).add_to(map)

            # Aggiungi solo un marker per il primo punto del poligono
            first_point = poligono_coords[0]
            if (first_point[0], first_point[1]) not in added_points:
                folium.Marker(
                    location=first_point,
                    popup=f"{row['name']}<br>{row['description']}",
                    tooltip=row['name'],
                    icon=folium.Icon(color="green", icon="")
                ).add_to(map)
                added_points.add((first_point[0], first_point[1]))

        added_points.add((lat, lon))

st.set_page_config(page_title="Leapers", page_icon=":heartpulse:", layout="wide")







def good_spots():
    added_points = set()
    for _, row in gs.dropna(subset=['latitudine', 'longitudine']).iterrows():
        lat, lon = row['latitudine'], row['longitudine']

        if (lat, lon) in added_points:
            continue

        poligono_coords = estrai_poligono(row['WKT'])
        if poligono_coords:
            # Aggiungi il poligono
            folium.Polygon(
                locations=poligono_coords,
                color="orange",
                fill=True,
                fill_color="orange",
                fill_opacity=0.3,
                tooltip=row['name']
            ).add_to(map)

            # Aggiungi solo un marker per il primo punto del poligono
            first_point = poligono_coords[0]
            if (first_point[0], first_point[1]) not in added_points:
                folium.Marker(
                    location=first_point,
                    popup=f"{row['name']}<br>{row['description']}",
                    tooltip=row['name'],
                    icon=folium.Icon(color="orange", icon="")
                ).add_to(map)
                added_points.add((first_point[0], first_point[1]))

        added_points.add((lat, lon))





def milans_finest():
    added_points = set()
    for _, row in mf.dropna(subset=['latitudine', 'longitudine']).iterrows():
        lat, lon = row['latitudine'], row['longitudine']

        if (lat, lon) in added_points:
            continue

        poligono_coords = estrai_poligono(row['WKT'])
        if poligono_coords:
            # Aggiungi il poligono
            folium.Polygon(
                locations=poligono_coords,
                color="red",
                fill=True,
                fill_color="red",
                fill_opacity=0.3,
                tooltip=row['name']
            ).add_to(map)

            # Aggiungi solo un marker per il primo punto del poligono
            first_point = poligono_coords[0]
            if (first_point[0], first_point[1]) not in added_points:
                folium.Marker(
                    location=first_point,
                    popup=f"{row['name']}<br>{row['description']}",
                    tooltip=row['name'],
                    icon=folium.Icon(color="red", icon="")
                ).add_to(map)
                added_points.add((first_point[0], first_point[1]))

        added_points.add((lat, lon))

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")
nav = option_menu(
    menu_title="",
    options=["About", "Graffiti", "Urbex", "Parkour Spots"],
    icons=["book-fill", "brush-fill", "house-door-fill", "map-fill"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "15!important", "background-color": "#2f2f2f"},
        "icon": {"color": "#ffffff", "font-size": "25px"},
        "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px", "--hover-color": "#1d1d1d"},
        "nav-link-selected": {"background-color": "#1d1d1d"},
    }
)

if nav == "About":
    st.write("---")
    st.title("WE ARE LEAPERS :wave:")
    st.subheader("A Parkour Group")
    st.write("We are a friend group who likes Parkour, Freerunning and Acrobatics.")
    st.write("Social: [Instagram](https://www.instagram.com/leapers_pk/)")

elif nav == "Graffiti":
    with st.container():
        st.write("---")
        st.title("Cool Graffiti :lower_left_paintbrush:")
        left_column, center_column, right_column = st.columns(3)
        with left_column:
            st.image(graffiti1, caption=("Garibaldi"))

elif nav == "Urbex":
    with st.container():
        st.write("---")
        st.title("Urbex :flashlight::derelict_house_building:")
        st.subheader("About Urbex")
        st.write(
            "Urban exploration, often abbreviated as urbex, is the practice of exploring man-made structures, usually abandoned ruins or hidden components of the built environment.")
        st.write(
            "This activity can also involve visiting places that are off-limits or not easily accessible to the public, such as old factories, hospitals, tunnels, amusement parks, or historical buildings.")
        st.title("PHOTOS")

        with st.expander("Abandoned Buildings"):
            st.subheader("Abandoned Buildings")
            col1, col2, col3 = st.columns(3)
            palazzo1 = palazzo1.resize((600, 600))
            palazzo2 = palazzo2.resize((600, 600))
            palazzo3 = palazzo3.resize((600, 600))
            palazzo4 = palazzo4.resize((600, 600))
            with col1:
                st.image(palazzo1)
                st.image(palazzo3)
            with col2:
                st.image(palazzo2)
                st.image(palazzo4)
            with col3:
                st.video(reel_palazzo1_bytes)
        with st.expander("Abandoned Swimming Pools"):
            st.subheader("Abandoned Swimming Pools")
            col1, col2, col3, col4 = st.columns(4)
            piscina1 = piscina1.resize((600, 600))
            piscina2 = piscina2.resize((600, 600))
            piscina3 = piscina3.resize((600, 600))
            piscina4 = piscina4.resize((600, 600))
            with col1:
                st.image(piscina1, width=400)
            with col2:
                st.image(piscina2, width=400)
            with col3:
                st.image(piscina3, width=400)
            with col4:
                st.image(piscina4, width=400)

else:
    with st.container():
        st.write("---")
        st.title("Parkour Spots")
        map = folium.Map(location=[45.46910803978604, 9.33], zoom_start=11)
        filter = st.multiselect("Filters", ["A few jumps possible", "Decent Spots", "Good Spots", "Milan's Finest", "Covered Spots"], default=["A few jumps possible", "Decent Spots", "Good Spots", "Milan's Finest", "Covered Spots"])
        if "A few jumps possible" in filter:
            blue_markers()
        if "Decent Spots" in filter:
            decent_spots()
        if "Good Spots" in filter:
            good_spots()
        if "Milan's Finest" in filter:
            milans_finest()
        if "Covered Spots" in filter:
            covered_spots()
        st_map = st_folium(map, width=1920)
