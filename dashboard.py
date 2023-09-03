import requests
import streamlit as st

st.title("Dashboard Scoring Bank")

if st.button("Obtenir les données de l API"):
    response = requests.get("https://scoring-bank.vercel.app/").json()
    st.write("Données de l'API :")
    st.write(response)

    st.write("Élément 'text' de l'API :")
    st.write(response['text'])
