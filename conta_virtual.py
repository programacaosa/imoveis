import streamlit as st
from streamlit.components.v1 import html

# Configuração da página
st.set_page_config(page_title="Conta Virtual", page_icon="💳", layout="wide")

# Título da página
st.title("📲 Conta Virtual")
st.markdown("---")

# Criando 4 colunas para os cards
col1, col2, col3, col4 = st.columns(4)

# Card 1 - Saldo Disponível
with col1:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        ">
            <div style="font-size: 50px;">💵</div>
            <div style="font-size: 20px; font-weight: bold;">Saldo Disponível</div>
            <div style="font-size: 24px;">R$ 5.250,00</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Card 2 - Investimentos
with col2:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        ">
            <div style="font-size: 50px;">📈</div>
            <div style="font-size: 20px; font-weight: bold;">Investimentos</div>
            <div style="font-size: 24px;">R$ 12.745,00</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Card 3 - Transferências
with col3:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        ">
            <div style="font-size: 50px;">🔄</div>
            <div style="font-size: 20px; font-weight: bold;">Transferências</div>
            <div style="font-size: 24px;">R$ 1.200,00</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Card 4 - Cartões
with col4:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        ">
            <div style="font-size: 50px;">💳</div>
            <div style="font-size: 20px; font-weight: bold;">Cartões</div>
            <div style="font-size: 24px;">3 ativos</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Conteúdo adicional da página
st.markdown("## 📊 Resumo Financeiro")
# Aqui você pode adicionar gráficos ou outras seções
