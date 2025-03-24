import streamlit as st

# Tela de login
st.title("Tela de Login")
usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    if usuario == "admin" and senha == "admin":  # Exemplo de validação simples
        st.success("Login realizado com sucesso!")
        # Realize o redirecionamento ou lógica de sucesso aqui
    else:
        st.error("Usuário ou senha incorretos!")
