import streamlit as st

# Função de login
def login():
    st.title("Tela de Login")

    # Campos de entrada de usuário e senha
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    # Verifica se algum dado foi preenchido
    if username and password:  # Se ambos os campos tiverem algo
        st.session_state.logged_in = True  # Alterar o estado de login
        st.session_state.username = username
        st.success("Login realizado com sucesso!")
        st.experimental_rerun()  # Atualiza a página para redirecionar o usuário
    else:
        st.info("Preencha o usuário e a senha para continuar.")

# Verificar se o usuário está logado
if not st.session_state.get("logged_in", False):
    login()  # Chama a função de login se o usuário não estiver logado
else:
    st.write(f"Bem-vindo, {st.session_state.username}!")
    # Exemplo de redirecionamento após login bem-sucedido
    if st.button("Ir para Depósitos e Conta Virtual"):
        # Exibe a tela de Depósitos e Conta Virtual
        st.write("Tela de Depósitos e Conta Virtual")
