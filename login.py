# Tela de login
if 'page' not in st.session_state:
    st.session_state.page = "login"

# Se a página for login
if st.session_state.page == "login":
    st.title("Tela de Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario == "admin" and senha == "admin":  # Exemplo de validação simples
            st.session_state.page = "conta_virtual"  # Após login, redireciona para a tela de conta virtual
            st.experimental_rerun()  # Atualiza a página para mostrar a tela de conta virtual
        else:
            st.error("Usuário ou senha incorretos!")
