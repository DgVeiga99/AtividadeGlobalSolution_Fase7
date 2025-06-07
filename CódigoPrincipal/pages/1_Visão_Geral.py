# ============================================================================================================
#                          ATIVIDADE FASE 7 - Global Solution - 2° Semestre
# ============================================================================================================
#                                   MONITORAMENTO DE TEMPESTADES
# ------------------------------------------------------------------------------------------------------------
"""
# Autor.....: Diego Nunes Veiga
# RM........: 560658
# Turma.....: Graduação - 1TIAOR
# Data......: 01/06/2025
# Assunto...: MONITORAMENTO DE TEMPESTADES
"""

# ============================================================================================================
#                                 BIBLIOTECAS, LISTAS E DICIONÁRIOS
# ============================================================================================================

import streamlit as st
import pandas as pd
import oracledb
import seaborn as sns
import matplotlib.pyplot as plt
from Banco_de_Dados import CarregaDados, ConexaoServidor, ListaCompleta

#Usuário para acessar o banco de dados
user = "RM560658"
password = "010199"
server = 'oracle.fiap.com.br:1521/ORCL'


#=============================================================================================================
#                                      PROCEDIMENTOS E FUNÇÕES
#=============================================================================================================


# Visão geral dos dados carregados
def VisaoGeral(df: pd.DataFrame):


    st.subheader('Informações do DataFrame')
    st.write('Dimensões do DataFrame:')
    st.write(f'*Linhas:* {df.shape[0]}, *Colunas:* {df.shape[1]}')
    st.subheader('Tipos de Dados')

    # Converter os tipos de dados para string
    df_types = pd.DataFrame({
        'Coluna': df.columns,
        'Tipos de Dados': df.dtypes.astype(str)
    })
    st.write(df_types)

    # Verificar valores ausentes
    st.subheader('Valores Ausentes')
    st.write(df.isnull().sum())

    # Estatísticas Descritivas
    st.subheader('Estatísticas Descritivas')
    st.write(df.describe())


# ============================================================================================================
#                                         PROGRAMA PRINCIPAL
# ============================================================================================================


# Configurações da página e título
st.set_page_config(
    page_title='Visão Geral',
    page_icon='📊',
    layout='wide'
    )
st.title('Visão Geral')


# Carregamento dos Dados
conexao = ConexaoServidor(user, password, server)

# Visão Geral dos Dados
if conexao == True:
    banco = ListaCompleta()
    VisaoGeral(banco)
else:
    st.error("Falha de conexão com o banco de dados")





# # ================================================
# # 7. Análise Interativa
# # ================================================
# st.header('7. Análise Interativa')
# # Seleção de variáveis pelo usuário
# st.subheader('Gráfico de Dispersão Interativo')
# col1, col2, col3 = st.columns(3)
# with col1:
#     x_var = st.selectbox('Selecione a variável X:', options=numeric_columns)
# with col2:
#     y_var = st.selectbox('Selecione a variável Y:', options=numeric_columns)
# with col3:
#     color_var = st.selectbox('Selecione a variável para colorir:', options=categorical_columns)
# corr_temp_prod = df[x_var].corr(df[y_var])
# st.write(f"A correlação de Pearson entre {y_var} e {x_var} é: {corr_temp_prod:.2f}")
# # Gráfico de dispersão interativo
# fig = px.scatter(
#     df,
#     x=x_var,
#     y=y_var,
#     color=color_var,
#     title=f'{y_var} vs {x_var} colorido por {color_var}'
# )
# st.plotly_chart(fig, use_container_width=True)