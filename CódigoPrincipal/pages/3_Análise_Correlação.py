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
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Banco_de_Dados import ConexaoServidor, ListaCompleta


#Usuário para acessar o banco de dados
user = "RM560658"
password = "010199"
server = 'oracle.fiap.com.br:1521/ORCL'


#=============================================================================================================
#                                      PROCEDIMENTOS E FUNÇÕES
#=============================================================================================================


# Análise de Correlação dos dados
def AnaliseCorrelacao(df: pd.DataFrame):

    # Mapa de calor de correlação
    st.subheader('Mapa de Calor de Correlação')

    # Selecionar apenas colunas numéricas
    numeric_df = df.select_dtypes(include=[np.number])
    corr = numeric_df.corr()
    fig_heatmap, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig_heatmap)


# ============================================================================================================
#                                         PROGRAMA PRINCIPAL
# ============================================================================================================


# Configurações da página e título
st.set_page_config(
    page_title='Análise de Correlação',
    page_icon='📊',
    layout='wide'
    )
st.title('Análise de Correlação')


# Carregamento dos Dados
conexao = ConexaoServidor(user, password, server)

# Visão Geral dos Dados
if conexao == True:
    banco = ListaCompleta()
    AnaliseCorrelacao(banco)
else:
    st.error("Falha de conexão com o banco de dados")



