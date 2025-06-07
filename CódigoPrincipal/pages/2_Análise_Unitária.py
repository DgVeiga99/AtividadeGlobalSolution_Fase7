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
import plotly.express as px
from Banco_de_Dados import ConexaoServidor, ListaCompleta

#Usuário para acessar o banco de dados
user = "RM560658"
password = "010199"
server = 'oracle.fiap.com.br:1521/ORCL'


#=============================================================================================================
#                                      PROCEDIMENTOS E FUNÇÕES
#=============================================================================================================


# Análise Univariada dos dados
def AnaliseUnivariada(df: pd.DataFrame):

    numeric_columns = ["Precipitacao (mm)","Pressão Atmosférica (mB)","Pressão Máxima (mB)",
                       "Pressão Mínima (mB)","Radiacao Global (KJ/m²)","Temperatura do Ar (°C)",
                       "Ponto de Orvalho (°C)","Temperatura Mínima (°C)","Temperatura Máxima (°C)",
                       "Temperatura Orvalho Máxima (°C)","Temperatura Orvalho Mínima (°C)",
                       "Umidade Máxima (%)","Umidade Mínima (%)","Umidade Relativa (%)",
                       "Direção Vento (°)","Vento máximo (m/s)","Vento hora (m/s)"]

    categorical_columns = ['Cidade']

    # Histogramas das variáveis numéricas
    st.subheader('Distribuições das Variáveis Numéricas')
    for col in numeric_columns:
        st.write(f'**{col}**')
        fig = px.histogram(df, x=col, nbins=30, title=f'Distribuição de {col}')
        st.plotly_chart(fig, use_container_width=True)


    # Distribuição das variáveis categóricas
    st.subheader('Distribuições das Variáveis Categóricas')
    for col in categorical_columns:
        st.write(f'**{col}**')
        fig = px.histogram(df, x=col, title=f'Distribuição de {col}')
        st.plotly_chart(fig, use_container_width=True)


# ============================================================================================================
#                                         PROGRAMA PRINCIPAL
# ============================================================================================================


# Configurações da página e título
st.set_page_config(
    page_title='Análise Unitária',
    page_icon='📊',
    layout='wide'
    )
st.title('Análise Unitária')


# Carregamento dos Dados
conexao = ConexaoServidor(user, password, server)

# Visão Geral dos Dados
if conexao == True:
    banco = ListaCompleta()
    AnaliseUnivariada(banco)
else:
    st.error("Falha de conexão com o banco de dados")

