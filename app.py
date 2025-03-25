import streamlit as st
import os
import json

# Função para fazer login e verificar credenciais
def login(email, password, folder="cadastro"):
    # Obtém o caminho absoluto do diretório de cadastro
    base_dir = os.path.abspath(os.path.dirname(__file__))  # Diretório onde o script está localizado
    user_folder = os.path.join(base_dir, folder, email.replace("@", "_at_").replace(".", "_dot_"))
    
    # Verifica se a pasta do usuário existe (significa que o usuário se cadastrou)
    if os.path.exists(user_folder):
        with open(os.path.join(user_folder, "dados.json"), "r") as f:
            user_data = json.load(f)
            # Verifica se a senha corresponde
            if user_data["Email"] == email and user_data["Senha"] == password:
                return user_data  # Retorna os dados do usuário se o login for bem-sucedido
    return None  # Retorna None se o login falhar

# Função para a tela de login
def login_screen():
    st.title("Login")
    
    # Campos de entrada de email e senha
    email = st.text_input("Email")
    password = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        if email and password:
            # Verifica se as credenciais são válidas
            user_data = login(email, password)
            if user_data:
                st.session_state["user_data"] = user_data  # Armazena os dados do usuário na sessão
                st.session_state["logged_in"] = True  # Marca o login como bem-sucedido
                st.success(f"Login bem-sucedido! Bem-vindo, {user_data['Nome']}")
                
                # Redireciona automaticamente para o Dashboard
                st.experimental_rerun()  # Redireciona para o Dashboard após login
            else:
                st.error("Credenciais inválidas. Tente novamente.")
        else:
            st.error("Por favor, insira email e senha.")

# Função para a tela do Dashboard
def dashboard():
    st.title("Dashboard")
    
    if "user_data" in st.session_state:
        user_data = st.session_state["user_data"]
        st.write(f"Bem-vindo, {user_data['Nome']}!")
        st.write(f"Email: {user_data['Email']}")
        st.write(f"Telefone: {user_data['Telefone']}")
    else:
        st.warning("Você precisa fazer login para acessar o Dashboard.")

# Função principal para alternar entre as telas
def main():
    # Verificar se o usuário está logado
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        login_screen()  # Se não estiver logado, mostrar a tela de login
    else:
        dashboard()  # Se estiver logado, mostrar o Dashboard

if __name__ == "__main__":
    main()
