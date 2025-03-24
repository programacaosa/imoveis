import streamlit as st
import subprocess
import os

def main():
    st.title("Tela Principal")
    
    st.write("Clique no botão abaixo para abrir a tela da Conta Virtual:")
    
    # Botão para abrir a conta_virtual.py
    if st.button("Abrir Conta Virtual"):
        # Verifica se o arquivo existe
        if os.path.exists("conta_virtual.py"):
            # Abre o arquivo conta_virtual.py usando o comando streamlit run
            subprocess.Popen(["streamlit", "run", "conta_virtual.py"])
            st.success("Tela da Conta Virtual aberta com sucesso!")
        else:
            st.error("Arquivo conta_virtual.py não encontrado!")

if __name__ == "__main__":
    main()
