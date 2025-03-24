import streamlit as st

# Configuração inicial
st.set_page_config(page_title="App Principal", layout="wide")

# Tela principal
def main_screen():
    st.title("🏠 Tela Principal")
    st.write("Clique no botão abaixo para acessar sua conta virtual:")
    
    if st.button("Acessar Conta Virtual", type="primary"):
        # Ativa a flag para mostrar a tela da conta virtual
        st.session_state.show_conta_virtual = True
        st.rerun()

# Verifica qual tela mostrar
if not st.session_state.get('show_conta_virtual', False):
    main_screen()
else:
    # Importa e mostra a tela da conta virtual
    from conta_virtual import conta_virtual_screen
    conta_virtual_screen()
    
    # Botão para voltar
    if st.button("Voltar para Tela Principal"):
        del st.session_state.show_conta_virtual
        st.rerun()
