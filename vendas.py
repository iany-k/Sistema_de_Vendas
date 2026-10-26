import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Título do Sistema e Carregamento de Dados
st.write('# Sistema de Vendas')
tabela = pd.read_csv('vendas.csv')

# 2. Formulário de Cadastro na Sidebar
st.sidebar.write('## Cadastrar venda')
data = st.sidebar.date_input('Data')
vendedor = st.sidebar.selectbox('Vendedor', ['Ana', 'Bruno', 'Carla'])
produto = st.sidebar.selectbox('Produto', ['Notebook', 'Celular', 'Fone'])
quantidade = st.sidebar.number_input('Quantidade', step=1)
valor = st.sidebar.number_input('Valor')
botao = st.sidebar.button('Cadastrar venda')

# 3. Lógica para Salvar Nova Venda
if botao:
    nova_venda = [data, vendedor, produto, quantidade, valor]
    tabela.loc[len(tabela)] = nova_venda
    tabela.to_csv('vendas.csv', index=False)
    st.success('Venda cadastrada!')

# 4. Exibição da Tabela de Vendas
st.write('## Vendas cadastradas')
st.dataframe(tabela)

# 5. Dashboard Visual e Métricas
st.write('## Dashboard')
soma = tabela['valor'].sum()
st.metric('Faturamento total', f'R${soma:.2f}')

grafico = px.bar(tabela, x='vendedor', y='valor', color='produto')
st.plotly_chart(grafico)

grafico2 = px.pie(tabela, names='produto', values='valor')
st.plotly_chart(grafico2)
