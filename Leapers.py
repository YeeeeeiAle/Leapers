import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

#--------Immagini

graffiti1 = Image.open("Images/Leapers1.jpg")
palazzo1 = Image.open("Images/Palazzo1.jpg")
palazzo2 = Image.open("Images/Palazzo2.jpg")
palazzo3 = Image.open("Images/Palazzo3.jpg")
piscina1 = Image.open("Images/piscina1.jpg")
piscina2 = Image.open("Images/piscina2.jpg")
piscina3 = Image.open("Images/piscina3.jpg")
piscina4 = Image.open("Images/piscina4.jpg")

#--------Pagina iniziale

st.set_page_config(page_title="Leapers", page_icon=":heartpulse:", layout="wide")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")
nav = option_menu(
    menu_title= "",
    options=["About", "Graffiti", "Urbex"],
    icons=["book-fill", "brush-fill", "house-door-fill"],
    default_index = 0,
    orientation = "horizontal",
    styles={
        "container": {"padding": "15!important", "background-color": "#2f2f2f"},
        "icon": {"color": "#ffffff", "font-size": "25px"},
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#1d1d1d"},
        "nav-link-selected": {"background-color": "#1d1d1d"},
    }
)


#--------Inizio
if nav == "About":
    st.write("---")
    st.title("WE ARE LEAPERS :wave:")
    st.subheader("A Parkour Group")
    st.write("We are a friend group who likes Parkour, Freerunning and Acrobatics.")
    st.write("Social: [Instagram](https://www.instagram.com/leapers_pk/)")

#--------Graffiti
elif nav == "Graffiti":
    with st.container():
        st.write("---")
        st.title("Cool Graffiti :lower_left_paintbrush:")
        left_column, center_column, right_column = st.columns(3)
        with left_column:
            st.image(graffiti1, caption=("Garibaldi"))

#---------Urbex
elif nav == "Urbex":
    with st.container():
        st.write("---")
        st.title("Urbex :flashlight::derelict_house_building:")
        st.subheader("About Urbex")
        st.write("Urban exploration, often abbreviated as urbex, is the practice of exploring man-made structures, usually abandoned ruins or hidden components of the built environment.")
        st.write("This activity can also involve visiting places that are off-limits or not easily accessible to the public, such as old factories, hospitals, tunnels, amusement parks, or historical buildings.")
        st.title("PHOTOS")

        with st.expander("Abandoned Buildings"):
            st.subheader("Abandoned Buildings")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(palazzo1, width=400)
            with col2:
                st.image(palazzo2, width=400)
            with col3:
                st.image(palazzo3, width=700)
        with st.expander("Abandoned Swimming Pools"):
            st.subheader("Abandoned Swimming Pools")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.image(piscina1, width=400)
            with col2:
                st.image(piscina2, width=400)
            with col3:
                st.image(piscina3, width=400)
            with col4:
                st.image(piscina4, width=400)
