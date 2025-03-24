import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def conta_virtual_screen():
    # Configuração da tela
    st.title("💳 Conta Virtual")
    st.markdown("---")
    
    # Cria 4 colunas para os cards
    col1, col2, col3, col4 = st.columns(4)
    
    # Card 1 - Saldo
    with col1:
        st.markdown("""
        <div style='
            background: linear-gradient(135deg, #667eea, #764ba2);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            height: 180px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin-bottom: 20px;
        '>
            <div style='font-size: 40px;'>💵</div>
            <div style='font-size: 18px; font-weight: bold;'>Saldo Disponível</div>
            <div style='font-size: 22px; margin-top: 10px;'>R$ 5.250,00</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Card 2 - Investimentos (os outros cards seguem o mesmo padrão)
    with col2:
        st.markdown("""
        <div style='
            background: linear-gradient(135deg, #f093fb, #f5576c);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            height: 180px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin-bottom: 20px;
        '>
            <div style='font-size: 40px;'>📈</div>
            <div style='font-size: 18px; font-weight: bold;'>Investimentos</div>
            <div style='font-size: 22px; margin-top: 10px;'>R$ 12.745,00</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Card 3 - Transferências
    with col3:
        st.markdown("""
        <div style='
            background: linear-gradient(135deg, #43e97b, #38f9d7);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            height: 180px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin-bottom: 20px;
        '>
            <div style='font-size: 40px;'>🔄</div>
            <div style='font-size: 18px; font-weight: bold;'>Transferências</div>
            <div style='font-size: 22px; margin-top: 10px;'>R$ 1.200,00</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Card 4 - Cartões
    with col4:
        st.markdown("""
        <div style='
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            height: 180px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin-bottom: 20px;
        '>
            <div style='font-size: 40px;'>💳</div>
            <div style='font-size: 18px; font-weight: bold;'>Investimentos imóveis</div>
            <div style='font-size: 22px; margin-top: 10px;'>3 ativos</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Adicionando gráficos (dados fictícios)
    st.markdown("---")
    
    # Gráfico de Investimentos ao longo do tempo (dados fictícios)
    st.subheader("Evolução dos Investimentos")
    x = np.arange(1, 13)
    y = np.random.randint(500, 1500, size=12)
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', color='purple')
    ax.set_title("Investimentos Mensais")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Valor (R$)")

    # Tornando o fundo do gráfico transparente
    fig.patch.set_facecolor('none')  # Fundo da figura transparente
    ax.set_facecolor('none')  # Fundo do eixo transparente
    st.pyplot(fig)

    # Gráfico de Saldo de Conta (dados fictícios)
    st.subheader("Saldo Mensal da Conta")
    saldo = np.random.randint(5000, 10000, size=12)
    fig2, ax2 = plt.subplots()
    ax2.bar(x, saldo, color='green')
    ax2.set_title("Saldo Mensal")
    ax2.set_xlabel("Mês")
    ax2.set_ylabel("Valor (R$)")

    # Tornando o fundo do gráfico transparente
    fig2.patch.set_facecolor('none')
    ax2.set_facecolor('none')
    st.pyplot(fig2)

    # Gráfico de Transferências realizadas (dados fictícios)
    st.subheader("Transferências Realizadas")
    transferencias = np.random.randint(100, 500, size=12)
    fig3, ax3 = plt.subplots()
    ax3.bar(x, transferencias, color='blue')
    ax3.set_title("Transferências por Mês")
    ax3.set_xlabel("Mês")
    ax3.set_ylabel("Valor (R$)")

    # Tornando o fundo do gráfico transparente
    fig3.patch.set_facecolor('none')
    ax3.set_facecolor('none')
    st.pyplot(fig3)

    # Conteúdo adicional (opcional)
    st.markdown("---")
    st.write("Mais informações da conta...")
