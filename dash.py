import requests
import streamlit as st

reponse = requests.get("https://scoring.streamlit.app/").json()
st.write("Données de l API :")
st.write(reponse)
