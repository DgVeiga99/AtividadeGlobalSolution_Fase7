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

import oracledb
import pandas as pd
import streamlit as st

#=============================================================================================================
#                                      PROCEDIMENTOS E FUNÇÕES
#=============================================================================================================


# Realiza conexão com o servidor do banco de dados
def ConexaoServidor(user, password, server) -> bool:
    global conn,bd_comando

    try:
        conn = oracledb.connect(user=user, password=password, dsn=server)
        bd_comando = conn.cursor()

    except Exception:
        conexao = False
    else:
        conexao = True

    return conexao


# Apresenta lista de todos os dados do banco
def ListaCompleta() -> None:
    lista = []
    bd_comando.execute('SELECT * FROM tempestade')
    tabela = bd_comando.fetchall()

    for dt in tabela:
        lista.append(dt)

    # ordena a lista
    lista = sorted(lista)

    # Formatação para apresentar todas a tabela sem exceção
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_rows', None)

    # Gera um DataFrame com os dados da lista utilizando o Pandas
    DadosFormatados = pd.DataFrame.from_records(lista, columns=[
        "ID","Data (YYYY-MM-DD)","Hora (UTC)","Precipitacao (mm)","Pressão Atmosférica (mB)","Pressão Máxima (mB)",
        "Pressão Mínima (mB)","Radiacao Global (KJ/m²)","Temperatura do Ar (°C)","Ponto de Orvalho (°C)",
        "Temperatura Mínima (°C)","Temperatura Máxima (°C)","Temperatura Orvalho Máxima (°C)","Temperatura Orvalho Mínima (°C)",
        "Umidade Máxima (%)","Umidade Mínima (%)","Umidade Relativa (%)","Direção Vento (°)","Vento máximo (m/s)",
        "Vento hora (m/s)","Cidade","Desastre Natural","Hora UTC","Radiação Clobal (Kj/m²)"], index = 'ID')


    if DadosFormatados.empty:
        st.warning("Nenhum registro encontrado!\n")
    else:
        st.dataframe(DadosFormatados)

    return DadosFormatados