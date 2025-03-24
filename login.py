import streamlit as st

# Função de login
def login():
    st.title("Tela de Login")

    # Campos de entrada de usuário e senha, com .strip() para remover espaços extras
    username = st.text_input("Usuário").strip()
    password = st.text_input("Senha", type="password").strip()

    # Se o botão de login for pressionado
    if st.button("Entrar"):
        # Verifica se as credenciais estão corretas
        if username == "admin" and password == "123":
            st.session_state.logged_in = True  # Alterar o estado de login
            st.session_state.username = username
            st.success("Login realizado com sucesso!")
            st.experimental_rerun()  # Atualiza a página para redirecionar o usuário
        else:
            st.error("Usuário ou senha incorretos.")

# Verificar se o usuário está logado
if not st.session_state.get("logged_in", False):
    login()  # Chama a função de login se o usuário não estiver logado
else:
    st.write(f"Bem-vindo, {st.session_state.username}!")
    # Aqui você pode redirecionar para a próxima tela ou funcionalidade após o login
    # Exemplo de exibição da próxima tela
    if st.button("Ir para Depósitos e Conta Virtual"):
        # Chamar a função da próxima tela ou exibir o conteúdo desejado
        st.write("Tela de Depósitos e Conta Virtual")
