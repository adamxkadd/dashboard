import requests
import streamlit as st

# data = requests.get("'https://jsonplaceholder.typicode.com/todos/1'").json()
data = requests.get('https://api-mu-nine.vercel.app/').json()
# data = requests.get("'https://api-mu-nine.vercel.app/'").json()


st.write(data)


# import requests

# # URL de l'API que vous souhaitez appeler
# url = "https://scoring.streamlit.app/donnees"

# # Effectuer la requête GET à l'API
# response = requests.get(url)

# # Vérifier si la requête a réussi (code de statut 200)
# if response.status_code == 200:
#     # Récupérer les données JSON de la réponse
#     donnees = response.json()
#     print("Données de l'API:")
#     print(donnees)
# else:
#     print("La requête à l'API a échoué avec le code de statut:", response.status_code)



# import streamlit as st
# import requests

# st.title("Application Streamlit avec API FastAPI")

# if st.button("Appeler l'API"):
#     response = requests.get("https://api-mu-nine.vercel.app/") 
#     st.write("Réponse de l'API:", response.json())
