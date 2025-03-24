import streamlit as st
import os

# Definir a configuração de página
st.set_page_config(
    page_title="Cadastro - Investidores e Incorporadoras",
    page_icon="🏢",
    layout="wide"
)

# Logo em base64
def get_base64_logo():
    # Caminho da logo na raiz do projeto
    img_path = "logo.png"  # Caminho da logo
    img = Image.open(img_path)
    
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Função para redirecionar
def redirecionar_login():
    st.session_state.page = "login"

# Tela principal
if 'page' not in st.session_state:
    st.session_state.page = "cadastro"

# Mostrar a tela de cadastro
if st.session_state.page == "cadastro":
    # Código para a tela de cadastro (que você já tem)
    st.markdown("<h2>Cadastro de Investidores e Incorporadoras</h2>", unsafe_allow_html=True)
    st.button('Fazer Login', on_click=redirecionar_login)

# Caso esteja na página de login
elif st.session_state.page == "login":
    # A tela de login será carregada aqui
    st.markdown("<h2>Tela de Login</h2>", unsafe_allow_html=True)
    st.text_input("Usuário")
    st.text_input("Senha", type="password")
    if st.button('Entrar'):
        # Adicione a lógica de validação de login
        st.success("Login realizado com sucesso!")
