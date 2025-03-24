import streamlit as st

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
        '>
            <div style='font-size: 40px;'>💳</div>
            <div style='font-size: 18px; font-weight: bold;'>Cartões</div>
            <div style='font-size: 22px; margin-top: 10px;'>3 ativos</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Conteúdo adicional (opcional)
    st.markdown("---")
    st.write("Mais informações da conta...")
