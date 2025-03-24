# login.py
import streamlit as st

def login():
    st.title("Tela de Login")

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if username == "admin" and password == "senha123":  # Validar login
            st.session_state.logged_in = True  # Alterar estado de login
            st.session_state.username = username
            st.success("Login realizado com sucesso!")
            st.experimental_rerun()  # Atualiza para abrir a tela de depósito
        else:
            st.error("Usuário ou senha incorretos.")

if not st.session_state.get("logged_in", False):
    login()  # Chama a função de login
