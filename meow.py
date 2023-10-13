import streamlit as st
import tyt

st.title("Vacation planner")

continent = st.sidebar.selectbox("Pick a Continent", ("Asia", "Africa", "North America", "South America", "Europe","Australia","Antarctica"))

if continent:
    response = tyt.get_country_city_places(continent)
    st.header(response['country_name'].strip())
    places= response['place_to_visit'].strip().split(",")
    st.write("**Places to visit**")
    for item in places:
        st.write("-", item)
