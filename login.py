import streamlit as st
from streamlit.components.v1 import html

# Configuração da página
st.set_page_config(page_title="Sistema Principal", layout="wide", page_icon="🏠")

# CSS personalizado
st.markdown("""
<style>
    /* Cards principais */
    .main-card {
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        text-align: center;
        cursor: pointer;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        margin: 10px;
    }
    
    .main-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    
    .card-icon {
        font-size: 50px;
        margin-bottom: 15px;
    }
    
    /* Modal */
    .modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0,0,0,0.5);
    }
    
    .modal-content {
        background: white;
        margin: 5% auto;
        padding: 30px;
        border-radius: 15px;
        width: 50%;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        animation: modalopen 0.5s;
    }
    
    @keyframes modalopen {
        from {opacity: 0; transform: translateY(-50px);}
        to {opacity: 1; transform: translateY(0);}
    }
    
    /* Campos de formulário */
    .stTextInput>div>div>input, .stFileUploader>div>div {
        border-radius: 20px !important;
        padding: 10px 15px !important;
    }
    
    .stButton>button {
        border-radius: 20px !important;
        padding: 8px 24px !important;
    }
</style>
""", unsafe_allow_html=True)

# JavaScript para controle do modal
modal_js = """
<script>
function openModal(modalId) {
    document.getElementById(modalId).style.display = 'block';
}
function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}
</script>
"""

html(modal_js)

# Título principal
st.title("🏠 Sistema Principal")
st.markdown("---")

# Container dos cards
col1, col2, col3 = st.columns(3)

# Card de Cadastro
with col1:
    st.markdown("""
    <div class="main-card" style="background: linear-gradient(135deg, #667eea, #764ba2);" onclick="openModal('cadastroModal')">
        <div class="card-icon">📝</div>
        <h3>Cadastro</h3>
        <p>Crie sua conta no sistema</p>
    </div>
    """, unsafe_allow_html=True)

# Card de Login
with col2:
    st.markdown("""
    <div class="main-card" style="background: linear-gradient(135deg, #43e97b, #38f9d7);" onclick="openModal('loginModal')">
        <div class="card-icon">🔑</div>
        <h3>Login</h3>
        <p>Acesse sua conta</p>
    </div>
    """, unsafe_allow_html=True)

# Card de Painel
with col3:
    st.markdown("""
    <div class="main-card" style="background: linear-gradient(135deg, #ff9a9e, #fad0c4);" onclick="openModal('painelModal')">
        <div class="card-icon">📊</div>
        <h3>Painel</h3>
        <p>Visualize seus dados</p>
    </div>
    """, unsafe_allow_html=True)

# Modal de Cadastro
st.markdown("""
<div id="cadastroModal" class="modal">
    <div class="modal-content">
        <div style="text-align: right;">
            <button onclick="closeModal('cadastroModal')" style="background: none; border: none; font-size: 20px;">×</button>
        </div>
        <h2 style="color: #667eea;">📝 Cadastro</h2>
        <div style="margin-top: 30px;">
""", unsafe_allow_html=True)

# Formulário de Cadastro (dentro do modal)
with st.form("form_cadastro"):
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome Completo", placeholder="Digite seu nome")
    with col2:
        email = st.text_input("E-mail", placeholder="Digite seu e-mail")
    
    col1, col2 = st.columns(2)
    with col1:
        senha = st.text_input("Senha", type="password", placeholder="Crie uma senha")
    with col2:
        confirma_senha = st.text_input("Confirmar Senha", type="password", placeholder="Repita a senha")
    
    documentos = st.file_uploader("📄 Envie seus documentos (PDF ou imagem)", type=["pdf", "png", "jpg"], accept_multiple_files=True)
    
    if st.form_submit_button("Cadastrar", type="primary"):
        if senha == confirma_senha:
            st.success("Cadastro realizado com sucesso!")
        else:
            st.error("As senhas não coincidem!")

st.markdown("""
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Modal de Login (similar ao de cadastro)
st.markdown("""
<div id="loginModal" class="modal">
    <div class="modal-content">
        <div style="text-align: right;">
            <button onclick="closeModal('loginModal')" style="background: none; border: none; font-size: 20px;">×</button>
        </div>
        <h2 style="color: #43e97b;">🔑 Login</h2>
        <div style="margin-top: 30px;">
""", unsafe_allow_html=True)

with st.form("form_login"):
    email = st.text_input("E-mail", placeholder="Digite seu e-mail")
    senha = st.text_input("Senha", type="password", placeholder="Digite sua senha")
    
    if st.form_submit_button("Entrar", type="primary"):
        st.success("Login realizado com sucesso!")

st.markdown("""
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Modal de Painel
st.markdown("""
<div id="painelModal" class="modal">
    <div class="modal-content">
        <div style="text-align: right;">
            <button onclick="closeModal('painelModal')" style="background: none; border: none; font-size: 20px;">×</button>
        </div>
        <h2 style="color: #ff9a9e;">📊 Painel do Usuário</h2>
        <div style="margin-top: 30px;">
            <p>Bem-vindo ao seu painel administrativo!</p>
            <div style="background: #f5f5f5; padding: 20px; border-radius: 10px; margin-top: 20px;">
                <h4>📌 Informações da Conta</h4>
                <p>Nome: João Silva</p>
                <p>E-mail: joao@exemplo.com</p>
                <p>Cadastrado em: 15/05/2023</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
