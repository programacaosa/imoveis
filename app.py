import streamlit as st

# Configuração inicial
st.set_page_config(page_title="App Principal", layout="wide")

# Adiciona CSS para imagem de fundo
def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://i.pinimg.com/736x/8f/75/60/8f75601ff2d00c7e51582f1032b250d5.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        /* Opcional: adiciona overlay para melhor legibilidade do texto */
        .stApp:before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0,0,0,0.3);
            z-index: -1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Chama a função para definir o background
set_background_image()

# Tela principal
def main_screen():
    # Logo centralizada
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png", width=200)
    
    st.title("📝 CADASTRO")
    st.write("Clique no botão abaixo para acessar sua conta virtual:")
    
    if st.button("Acessar Conta Virtual", type="primary"):
        st.session_state.show_conta_virtual = True
        st.rerun()

# Verifica qual tela mostrar
if not st.session_state.get('show_conta_virtual', False):
    main_screen()
else:
    from conta_virtual import conta_virtual_screen
    conta_virtual_screen()
    
    if st.button("Voltar para Tela Principal"):
        del st.session_state.show_conta_virtual
        st.rerun()
