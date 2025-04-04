import streamlit as st
import os
import json
import mysql.connector
from PIL import Image

# Função para criar a conexão com o banco de dados MySQL
def create_connection():
    return mysql.connector.connect(
        host="108.181.92.72",  # IP do servidor MySQL
        user="investimentos",    # Substitua com seu usuário
        password="azevedo39",  # Substitua com sua senha
        database="investimentos"   # Substitua com o nome do banco de dados
    )

# Função para salvar os dados do usuário no MySQL
def save_user_data_to_db(name, email, phone, password):
    connection = create_connection()
    cursor = connection.cursor()

    # Inserir dados do usuário na tabela "usuarios"
    query = """
    INSERT INTO usuarios (nome, email, telefone, senha) 
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name.strip(), email.strip(), phone.strip(), password.strip()))
    connection.commit()

    cursor.close()
    connection.close()

# Função para verificar o login do usuário no MySQL
def login_db(email, password):
    connection = create_connection()
    cursor = connection.cursor()

    # Consultar dados do usuário no banco
    query = "SELECT * FROM usuarios WHERE email = %s"
    cursor.execute(query, (email,))
    user_data = cursor.fetchone()

    cursor.close()
    connection.close()

    if user_data and user_data[4] == password:  # Verifica se a senha está correta (index 4 é a senha)
        return user_data
    return None

# Função para salvar a foto do usuário
def save_uploaded_file(uploaded_file, user_folder):
    file_extension = os.path.splitext(uploaded_file.name)[-1]
    file_name = f"foto{file_extension}"
    file_path = os.path.join(user_folder, file_name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path

# Tela de Cadastro
def cadastro():
    st.title("Cadastro de Usuário")
    st.write("Passo 1: Preencha seus dados")
    
    # Inputs com ícones no botão
    name = st.text_input("Nome", placeholder="Digite seu nome", key="name_input")
    email = st.text_input("Email", placeholder="Digite seu e-mail", key="email_input")
    phone = st.text_input("Telefone", placeholder="Digite seu telefone", key="phone_input")
    password = st.text_input("Senha", type="password", placeholder="Digite sua senha", key="password_input")
    
    # Botão para salvar dados do usuário
    if st.button("Salvar Dados"):
        if all([name, email, phone, password]):
            save_user_data_to_db(name, email, phone, password)
            st.success("Dados salvos com sucesso! Agora envie sua foto.")
        else:
            st.error("Por favor, preencha todos os campos corretamente.")
    
    # Etapa de envio de foto
    st.write("Passo 2: Envie sua foto")
    uploaded_file = st.file_uploader("Escolha uma foto", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        if "user_folder" in st.session_state:
            image = Image.open(uploaded_file)
            st.image(image, caption="Pré-visualização da Foto", use_column_width=True)
            
            if st.button("Salvar Foto"):
                file_path = save_uploaded_file(uploaded_file, st.session_state["user_folder"])
                st.success(f"Foto salva com sucesso em: {file_path}")
        else:
            st.error("Por favor, salve primeiro os dados antes de enviar a foto.")

# Tela de Login
def login():
    st.title("Login")
    
    email = st.text_input("Email", placeholder="Digite seu e-mail", key="email_input_login")
    password = st.text_input("Senha", type="password", placeholder="Digite sua senha", key="password_input_login")
    
    # Lógica para verificar o login
    if st.button("Entrar"):
        user_data = login_db(email, password)
        if user_data:
            st.session_state["user_folder"] = user_data[0]  # Atribui o ID do usuário (index 0) à sessão
            st.session_state["logged_in"] = True  # Marca o login como bem-sucedido
            st.success("Login bem-sucedido!")
            # Redireciona para o Dashboard após o login
            st.experimental_rerun()  # Redireciona para a tela do Dashboard
        else:
            st.error("Usuário ou senha incorretos.")

# Tela de Dashboard
def dashboard():
    st.title("Dashboard")
    
    if "user_folder" in st.session_state:
        user_folder = st.session_state["user_folder"]
        
        # Consultar dados do usuário no banco de dados
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT nome, email, telefone FROM usuarios WHERE id = %s"
        cursor.execute(query, (user_folder,))
        user_data = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if user_data:
            st.write(f"Bem-vindo, {user_data[0]}!")
            st.write(f"Email: {user_data[1]}")
            st.write(f"Telefone: {user_data[2]}")
        else:
            st.warning("Usuário não encontrado.")
    else:
        st.warning("Você precisa fazer login para acessar o Dashboard.")

# Função principal
def main():
    st.sidebar.image("https://static.vecteezy.com/ti/vetor-gratis/p1/8124777-logo-logo-casa-logotipo-casa-logo-simbolo-sinal-gratis-vetor.jpg", width=200)
    st.sidebar.title("Menu")
    
    # Verificar se o usuário está logado
    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        dashboard()  # Se o usuário estiver logado, mostra o Dashboard
    else:
        menu_option = st.sidebar.radio("Escolha uma opção", ["Cadastro", "Login"])
        
        # Dependendo da opção do menu, exibe a tela correspondente
        if menu_option == "Cadastro":
            cadastro()
        elif menu_option == "Login":
            login()

if __name__ == "__main__":
    main()
