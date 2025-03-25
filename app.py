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

# Função para o cadastro de usuário
def cadastro_screen():
    st.title("Cadastro")
    
    # Campos de cadastro
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    telefone = st.text_input("Telefone")
    senha = st.text_input("Senha", type="password")
    
    if st.button("Cadastrar"):
        if nome and email and telefone and senha:
            user_id = email.replace("@", "_at_").replace(".", "_dot_")
            user_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), "cadastro", user_id)
            
            # Cria a pasta do usuário
            os.makedirs(user_folder, exist_ok=True)
            
            # Dados do usuário
            user_data = {
                "Nome": nome,
                "Email": email,
                "Telefone": telefone,
                "Senha": senha
            }
            
            # Salva os dados do usuário em um arquivo JSON
            with open(os.path.join(user_folder, "dados.json"), "w") as f:
                json.dump(user_data, f)
            
            st.success(f"Cadastro realizado com sucesso! Bem-vindo, {nome}")
        else:
            st.error("Por favor, preencha todos os campos.")

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
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("Escolha uma opção", ["Login", "Cadastro", "Dashboard"])
    
    if menu == "Login":
        login_screen()  # Se escolher Login, mostrar a tela de login
    elif menu == "Cadastro":
        cadastro_screen()  # Se escolher Cadastro, mostrar a tela de cadastro
    else:
        # Verificar se o usuário está logado
        if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
            st.warning("Você precisa fazer login para acessar o Dashboard.")
        else:
            dashboard()  # Se estiver logado, mostrar o Dashboard

if __name__ == "__main__":
    main()
