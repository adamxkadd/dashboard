st.title("Tableau de bord Streamlit")

# Créez un formulaire pour saisir des données
st.header("Saisissez des données:")
user_input = st.text_input("Entrez des données:", "Exemple de données")

# Bouton pour envoyer les données à l'API
if st.button("Predire"):
    data = {"input_data": user_input}
    response = requests.post(f"{API_URL}/predict/", json=data)
