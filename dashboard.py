import requests
import streamlit as st

data = requests.get("https://flask-hello-world-tan-zeta.vercel.app/").json()
st.write(data)



# API_URL = 'https://flask-hello-world-tan-zeta.vercel.app/'
# data = {'input' : 'ENTER SOME INPUT HERE'}
# response = rq.get(API_URL,params=data)
# json_values = response.json()
# rq_input, timestamp, letter_count = json_values['input'], json_values['timestamp'], json_values['letter_count']
# print(f'Input is: {rq_input}')
# print(f'Date is: {datetime.fromtimestamp(timestamp)}')
# print(f' Letter count is: {Ietter_count}')


# import requests
# import streamlit as st

# # data = requests.get("https://api-mu-nine.vercel.app/").json()
# # st.write("My 2")

# # url = "https://api-mu-nine.vercel.app/"
# # myobj = {'somekey': 'somevalue'}
# # response = requests.post(url, data = myobj)
# response = requests.post("https://api-mu-nine.vercel.app/").json()
# st.write("My 'API")
# if response.status_code == 200:
#   st.write("My 2")
#   st.write(response.text)
  
# else:
#   st.write("ERR")
  
#   st.write(response.status_code)
  
#   st.write(response.text)
#   print("Erreur lors de la requête à l'API")
  
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
