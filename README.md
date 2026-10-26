## Sistema de Vendas para cadastrar produtos

O Sistema de Vendas é um aplicativo simples feito em Python com Streamlit. Ele permite cadastrar vendas, exibir os registros e acompanhar o faturamento por meio de indicadores e gráficos.
Arquivos
- vendas.py: contém o código do aplicativo.
- vendas.csv: armazena as vendas cadastradas. As colunas são data, vendedor, produto, quantidade e valor.
Como funciona
1. Ao iniciar, o programa lê vendas.csv usando o Pandas.
2. Na barra lateral, apresenta um formulário para escolher a data, o vendedor e o produto, e informar quantidade e valor.
3. Ao clicar em Cadastrar venda, acrescenta os dados à tabela e grava o CSV.
4. Exibe as vendas cadastradas em uma tabela.
5. Calcula e mostra o faturamento total.
6. Gera um gráfico de barras com o valor por vendedor, colorido por produto, e um gráfico de pizza com a participação de cada produto no valor das vendas.
O cadastro aceita vendedores predefinidos (Ana, Bruno e Carla) e produtos predefinidos (Notebook, Celular e Fone).
Tecnologias usadas
- Python: linguagem do aplicativo.
- Streamlit: interface web e interação.
- Pandas: leitura, manipulação e gravação dos dados.
- Plotly Express: gráficos interativos.
- CSV: armazenamento simples dos registros.
Como executar
No terminal do VS Code, abra a pasta do projeto e rode:

streamlit run vendas.py
