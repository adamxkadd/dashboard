import streamlit as st
import requests

st.title("Application Streamlit avec API FastAPI")

if st.button("Appeler l'API"):
    response = requests.get("https://api-mu-nine.vercel.app/") 
    st.write("Réponse de l'API:", response.json())
