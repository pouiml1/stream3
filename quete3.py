import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

lesDonneesDesComptes = {'usernames': {'nico': {'name': 'utilisateur',
   'password': 'cc',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
      with st.sidebar:
        selected = option_menu("Main Menu", ["Accueil", 'Les photos de mon chat'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
        selected
      if selected == "Accueil" :
            st.title("Bienvenue sur ma page")
            st.image("https://www.shutterstock.com/shutterstock/photos/2269063761/display_1500/stock-photo-the-crowd-in-a-fan-zone-in-a-concert-hall-raised-hands-during-a-music-show-2269063761.jpg")
      elif selected == "Les photos de mon chat" :
            st.title("Bienvenue dans l'album de mes chats")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.header("Voici Gilbert")
                st.image("https://www.coeurcoeur.fr/wp-content/uploads/2021/01/Les-5-races-de-chats-les-plus-moches-du-monde.jpg")

            with col2:
                st.header("Puis Bernard")
                st.image("https://m1.quebecormedia.com/emp/jdx-prod-images/ad345059-0e3f-4da6-a53e-e134053fbe4d_ORIGINAL.jpg?impolicy=resize&quality=80&width=640")

            with col3:
                st.header("Sans oublier Frank")
                st.image("https://www.ipnoze.com/wp-content/uploads/2020/04/chat-avec-plis-sphynx-xherdan-027.jpg")

if st.session_state["authentication_status"]:
  accueil()

  # Le bouton de déconnexion
  authenticator.logout("Déconnexion")

  
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
