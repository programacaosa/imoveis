import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configuração da página
st.set_page_config(
    page_title="Cadastro - Investidores e Incorporadoras",
    page_icon="🏢",
    layout="wide"
)

# Logo em base64 (substitua pela sua logo)
def get_base64_logo():
    # Carregar a logo do arquivo
    img_path = "logo.png"  # Caminho da logo na raiz do projeto
    img = Image.open(img_path)
    
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# CSS personalizado com ícones
st.markdown(f"""
    <style>
        .main {{
            background-color: #f8f9fa;
        }}
        .stButton>button {{
            background-color: #0062cc;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            width: 100%;
        }}
        .stTextInput>div>div>input, .stSelectbox>div>div>select {{
            border-radius: 5px;
            padding: 0.5rem;
            padding-left: 2.5rem !important;
        }}
        .header {{
            color: #003566;
            text-align: center;
        }}
        .file-uploader {{
            border: 2px dashed #ccc;
            border-radius: 5px;
            padding: 20px;
            text-align: center;
            margin-bottom: 20px;
        }}
        .success-message {{
            color: #28a745;
            text-align: center;
            font-weight: bold;
            margin-top: 20px;
        }}
        .input-icon {{
            position: absolute;
            left: 10px;
            top: 50%;
            transform: translateY(-50%);
            color: #6c757d;
            z-index: 2;
        }}
        .input-container {{
            position: relative;
        }}
    </style>
""", unsafe_allow_html=True)

# Cabeçalho com logo
logo_base64 = get_base64_logo()
st.markdown(
    f"""
    <div style="text-align: center; margin-bottom: 2rem;">
        <img src="data:image/png;base64,{logo_base64}" style="max-width: 300px; margin-bottom: 1rem;">
        <h1 class="header">Cadastro de Investidores e Incorporadoras</h1>
        <p>Preencha o formulário abaixo para se cadastrar em nossa plataforma.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Formulário de cadastro com ícones
with st.form("cadastro_form"):
    # Seção de informações básicas
    st.subheader("Informações Básicas")
    col1, col2 = st.columns(2)
    
    with col1:
        # Campo com ícone
        st.markdown("""<div class="input-container"><i class="fas fa-user-tag input-icon"></i></div>""", unsafe_allow_html=True)
        tipo_cadastro = st.selectbox(
            "Tipo de Cadastro*",
            ["Selecione...", "Investidor Individual", "Investidor Institucional", "Incorporadora"],
            index=0
        )
        
        # Campo com ícone
        st.markdown("""<div class="input-container"><i class="fas fa-user input-icon"></i></div>""", unsafe_allow_html=True)
        nome_completo = st.text_input("Nome Completo/Razão Social*")
        
        # Campo com ícone
        st.markdown("""<div class="input-container"><i class="fas fa-id-card input-icon"></i></div>""", unsafe_allow_html=True)
        cpf_cnpj = st.text_input("CPF/CNPJ*")
        
    with col2:
        # Campo com ícone
        st.markdown("""<div class="input-container"><i class="fas fa-envelope input-icon"></i></div>""", unsafe_allow_html=True)
        email = st.text_input("E-mail*")
        
        # Campo com ícone
        st.markdown("""<div class="input-container"><i class="fas fa-phone input-icon"></i></div>""", unsafe_allow_html=True)
        telefone = st.text_input("Telefone*")
        
        # Campo com ícone
        st.markdown("""<div class="input-container"><i class="fas fa-lock input-icon"></i></div>""", unsafe_allow_html=True)
        senha = st.text_input("Senha*", type="password")
    
    # Seção de documentos
    st.subheader("Documentação")
    st.markdown("<div class='file-uploader'>", unsafe_allow_html=True)
    st.write("Envie seus documentos (PDF, JPG ou PNG)")
    
    # Upload com ícones
    col_doc1, col_doc2 = st.columns(2)
    with col_doc1:
        st.markdown("""<div style="margin-bottom: 1rem;"><i class="fas fa-id-card" style="margin-right: 10px;"></i>Documento de Identidade (RG/CNH)*</div>""", unsafe_allow_html=True)
        doc_identidade = st.file_uploader("", type=["pdf", "jpg", "png", "jpeg"], key="doc1", label_visibility="collapsed")
    
    with col_doc2:
        st.markdown("""<div style="margin-bottom: 1rem;"><i class="fas fa-home" style="margin-right: 10px;"></i>Comprovante de Residência*</div>""", unsafe_allow_html=True)
        doc_comprovante = st.file_uploader("", type=["pdf", "jpg", "png", "jpeg"], key="doc2", label_visibility="collapsed")
    
    st.markdown("""<div style="margin-bottom: 1rem;"><i class="fas fa-file-alt" style="margin-right: 10px;"></i>Documentos Adicionais (opcional)</div>""", unsafe_allow_html=True)
    doc_adicional = st.file_uploader("", type=["pdf", "jpg", "png", "jpeg"], accept_multiple_files=True, key="doc3", label_visibility="collapsed")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Termos e condições
    st.subheader("Termos e Condições")
    aceite_termos = st.checkbox("Eu li e concordo com os Termos de Uso e Política de Privacidade*")
    
    # Botão de envio sem unsafe_allow_html
    submitted = st.form_submit_button("Enviar Cadastro")
    
    if submitted:
        # Validação básica
        if tipo_cadastro == "Selecione..." or not nome_completo or not cpf_cnpj or not email or not telefone or not senha or not doc_identidade or not doc_comprovante or not aceite_termos:
            st.error("Por favor, preencha todos os campos obrigatórios (*)")
        else:
            # Processamento do cadastro
            st.markdown("<p class='success-message'><i class='fas fa-check-circle' style='margin-right: 10px;'></i>Cadastro enviado com sucesso! Entraremos em contato em breve.</p>", unsafe_allow_html=True)

# Adicionando Font Awesome para os ícones
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
""", unsafe_allow_html=True)
