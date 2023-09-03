import streamlit as st
import requests

# Interface Streamlit
st.title("Application Streamlit avec API FastAPI")

if st.button("Appeler l'API"):
    # Fait une requête HTTP à l'API FastAPI pour obtenir une réponse
    response = requests.get("https://api-mu-nine.vercel.app/")  # Assurez-vous de l'URL correcte pour votre API FastAPI
    
    # Affiche la réponse de l'API dans Streamlit
    st.write("Réponse de l'API:", response.json())
