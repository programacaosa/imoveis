import streamlit as st
import os
import json
from PIL import Image

# Função para salvar os dados do usuário
def save_user_data(user_id, name, email, phone, password, folder="cadastro"):
    user_folder = os.path.join(folder, user_id)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
    
    user_data = {
        "Nome": name.strip(),
        "Email": email.strip(),
        "Telefone": phone.strip(),
        "Senha": password.strip()
    }
    
    with open(os.path.join(user_folder, "dados.json"), "w") as f:
        json.dump(user_data, f, indent=4)
    
    return user_folder

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
            user_id = email.replace("@", "_at_").replace(".", "_dot_")
            user_folder = save_user_data(user_id, name, email, phone, password)
            st.session_state["user_folder"] = user_folder
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
        user_id = email.replace("@", "_at_").replace(".", "_dot_")
        user_folder = os.path.join("cadastro", user_id)
        
        if os.path.exists(user_folder):
            with open(os.path.join(user_folder, "dados.json"), "r") as f:
                user_data = json.load(f)
            
            if user_data["Senha"] == password:
                st.session_state["user_folder"] = user_folder
                st.session_state["logged_in"] = True  # Marca o login como bem-sucedido
                st.success("Login bem-sucedido!")
                
                # Redireciona para o Dashboard após o login
                st.experimental_rerun()  # Redireciona para a tela do Dashboard
            else:
                st.error("Senha incorreta.")
        else:
            st.error("Usuário não encontrado.")

# Tela de Dashboard
def dashboard():
    st.title("Dashboard")
    
    if "user_folder" in st.session_state:
        user_folder = st.session_state["user_folder"]
        with open(os.path.join(user_folder, "dados.json"), "r") as f:
            user_data = json.load(f)
        
        st.write(f"Bem-vindo, {user_data['Nome']}!")
        st.write(f"Email: {user_data['Email']}")
        st.write(f"Telefone: {user_data['Telefone']}")
    else:
        st.warning("Você precisa fazer login para acessar o Dashboard.")

# Função principal
def main():
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/a/a7/Streamlit_logo.svg", width=200)
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
