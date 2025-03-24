import streamlit as st

def login():
    st.title("Tela de Login")

    username = st.text_input("Usuário").strip()  # Remover espaços extras
    password = st.text_input("Senha", type="password").strip()  # Remover espaços extras

    # Exibir as credenciais para depuração (remover após testar)
    st.write(f"Usuário (debug): '{username}'")
    st.write(f"Senha (debug): '{password}'")

    if st.button("Entrar"):
        # Verificar as credenciais
        if username == "admin" and password == "123":
            st.session_state.logged_in = True  # Alterar estado de login
            st.session_state.username = username
            st.success("Login realizado com sucesso!")
            st.experimental_rerun()  # Atualiza para abrir a tela de depósito
        else:
            st.error("Usuário ou senha incorretos.")

# Verificar se o usuário está logado
if not st.session_state.get("logged_in", False):
    login()  # Chama a função de login
else:
    st.write("Bem-vindo, você está logado como:", st.session_state.username)
