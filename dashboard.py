import streamlit as st

# Interface Streamlit
st.title("Application Streamlit avec API FastAPI")

# Afficher un texte d'introduction
st.write("Ceci est une démonstration d'une API FastAPI intégrée dans Streamlit.")

# Utilisation de l'API FastAPI dans Streamlit
if st.button("Appeler l'API"):
    # Fait une requête HTTP à l'API FastAPI pour obtenir une réponse
    response = app_fastapi.get("/")
  
    # Affiche la réponse de l'API dans Streamlit
    st.write("Réponse de l'API:", response.json())
