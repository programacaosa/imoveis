import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Definir a configuração da página
st.set_page_config(
    page_title="Cadastro - Investidores e Incorporadoras",
    page_icon="🏢",
    layout="wide"
)

# Logo em base64
def get_base64_logo():
    img_path = "logo.png"  # Caminho da logo
    img = Image.open(img_path)
    
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Função para redirecionar para a tela de cadastro
def redirecionar_cadastro():
    st.session_state.page = "cadastro"

# Função para redirecionar para a tela de login
def redirecionar_login():
    st.session_state.page = "login"

# Definir a página de navegação com base no estado da sessão
if 'page' not in st.session_state:
    st.session_state.page = "cadastro"

# Se a página for cadastro
if st.session_state.page == "cadastro":
    # Cabeçalho com logo
    logo_base64 = get_base64_logo()
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 2rem;">
        <img src="data:image/png;base64,{logo_base64}" style="max-width: 300px; margin-bottom: 1rem;">
        <h1 class="header">Cadastro de Investidores e Incorporadoras</h1>
        <p>Preencha o formulário abaixo para se cadastrar em nossa plataforma.</p>
    </div>
    """, unsafe_allow_html=True)

    # Formulário de cadastro com ícones
    with st.form("cadastro_form"):
        # Seção de informações básicas
        st.subheader("Informações Básicas")
        col1, col2 = st.columns(2)

        with col1:
            tipo_cadastro = st.selectbox(
                "Tipo de Cadastro*",
                ["Selecione...", "Investidor Individual", "Investidor Institucional", "Incorporadora"],
                index=0
            )
            nome_completo = st.text_input("Nome Completo/Razão Social*")
            cpf_cnpj = st.text_input("CPF/CNPJ*")

        with col2:
            email = st.text_input("E-mail*")
            telefone = st.text_input("Telefone*")
            senha = st.text_input("Senha*", type="password")

        # Seção de documentos
        st.subheader("Documentação")
        st.write("Envie seus documentos (PDF, JPG ou PNG)")

        col_doc1, col_doc2 = st.columns(2)
        with col_doc1:
            doc_identidade = st.file_uploader("Documento de Identidade (RG/CNH)*", type=["pdf", "jpg", "png", "jpeg"], key="doc1")
        with col_doc2:
            doc_comprovante = st.file_uploader("Comprovante de Residência*", type=["pdf", "jpg", "png", "jpeg"], key="doc2")
        
        # Termos e condições
        st.subheader("Termos e Condições")
        aceite_termos = st.checkbox("Eu li e concordo com os Termos de Uso e Política de Privacidade*")

        submitted = st.form_submit_button("Enviar Cadastro")
        if submitted:
            if tipo_cadastro == "Selecione..." or not nome_completo or not cpf_cnpj or not email or not telefone or not senha or not doc_identidade or not doc_comprovante or not aceite_termos:
                st.error("Por favor, preencha todos os campos obrigatórios (*)")
            else:
                st.success("Cadastro enviado com sucesso! Entraremos em contato em breve.")

    # Botão de login
    st.button('Fazer Login', on_click=redirecionar_login)

# Se a página for login
elif st.session_state.page == "login":
    # Tela de login
    st.title("Tela de Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    # Botão de Voltar
    if st.button("Voltar ao Cadastro"):
        redirecionar_cadastro()

    if st.button("Entrar"):
        if usuario == "admin" and senha == "admin":  # Exemplo de validação simples
            st.success("Login realizado com sucesso!")
            # Lógica de redirecionamento após login bem-sucedido pode ser colocada aqui
        else:
            st.error("Usuário ou senha incorretos!")
