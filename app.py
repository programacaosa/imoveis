import streamlit as st

# Configuração inicial (ÚNICO lugar onde isso deve aparecer)
st.set_page_config(page_title="App Principal", layout="wide")

# Tela principal
def main_screen():
    # Logo centralizada
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png", width=200)
    
    st.title("🏠 CADASTRO")
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
