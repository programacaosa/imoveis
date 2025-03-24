# conta_virtual.py
import streamlit as st

def conta_virtual():
    st.title("Conta Virtual e Depósitos")

    st.subheader("Depósitos e Conta Virtual")
    st.write("Aqui você pode fazer depósitos via Pix, boleto ou transferência bancária.")
    st.write("O saldo fica disponível para investimentos na plataforma.")

    # Exibir saldo do usuário
    st.write(f"Saldo atual: R$ 1000,00 (Exemplo)")

    # Outras funcionalidades da conta, como histórico de transações, etc.

if st.session_state.get("logged_in", False):  # Verifica se o usuário está logado
    conta_virtual()  # Chama a função de depósito
else:
    st.warning("Você precisa estar logado para acessar esta página.")
