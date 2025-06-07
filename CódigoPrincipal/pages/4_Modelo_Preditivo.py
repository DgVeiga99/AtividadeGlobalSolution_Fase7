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
import numpy as np
from narwhals import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error,mean_squared_error
from Banco_de_Dados import ConexaoServidor, ListaCompleta

#Usuário para acessar o banco de dados
user = "RM560658"
password = "010199"
server = 'oracle.fiap.com.br:1521/ORCL'


#=============================================================================================================
#                                      PROCEDIMENTOS E FUNÇÕES
#=============================================================================================================


# Filtra a precipitação
def FiltroPrecipitacao(df: DataFrame):
    return st.sidebar.slider(
        'Precipitação (mm):',
        min_value=float(df["Precipitacao (mm)"].min()),
        max_value=float(df["Precipitacao (mm)"].max()),
        value=(float(df["Precipitacao (mm)"].min()), float(df["Precipitacao (mm)"].max())),
    )


# Filtra a pressão atmosférica
def FiltroPressaoAtm(df: DataFrame):
    return st.sidebar.slider(
        'Pressão Atmosférica (mB):',
        min_value=float(df["Pressão Atmosférica (mB)"].min()),
        max_value=float(df["Pressão Atmosférica (mB)"].max()),
        value=(float(df["Pressão Atmosférica (mB)"].min()), float(df["Pressão Atmosférica (mB)"].max())),
    )

# Filtra a pressão atmosférica máxima
def FiltroPressaoAtmMax(df: DataFrame):
    return st.sidebar.slider(
        'Pressão Máxima (mB):',
        min_value=float(df["Pressão Máxima (mB)"].min()),
        max_value=float(df["Pressão Máxima (mB)"].max()),
        value=(float(df["Pressão Máxima (mB)"].min()), float(df["Pressão Máxima (mB)"].max())),
    )


# Filtra a pressão atmosférica mínima
def FiltroPressaoAtmMin(df: DataFrame):
    return st.sidebar.slider(
        'Pressão Mínima (mB):',
        min_value=float(df["Pressão Mínima (mB)"].min()),
        max_value=float(df["Pressão Mínima (mB)"].max()),
        value=(float(df["Pressão Mínima (mB)"].min()), float(df["Pressão Mínima (mB)"].max())),
    )


# Filtra a Radiação Global
def FiltroRadiacaoGlobal(df: DataFrame):
    return st.sidebar.slider(
        'Radiação Global (KJ/m²):',
        min_value=float(df["Radiacao Global (KJ/m²)"].min()),
        max_value=float(df["Radiacao Global (KJ/m²)"].max()),
        value=(float(df["Radiacao Global (KJ/m²)"].min()), float(df["Radiacao Global (KJ/m²)"].max())),
    )


# Filtra a temperatura do ar
def FiltroTemperaturaAr(df: DataFrame):
    return st.sidebar.slider(
        'Temperatura do Ar (°C):',
        min_value=float(df["Temperatura do Ar (°C)"].min()),
        max_value=float(df["Temperatura do Ar (°C)"].max()),
        value=(float(df["Temperatura do Ar (°C)"].min()), float(df["Temperatura do Ar (°C)"].max())),
    )


# Filtra a temperatura de orvalho
def FiltroTemperaturaOrvalho(df: DataFrame):
    return st.sidebar.slider(
        'Ponto de Orvalho (°C):',
        min_value=float(df['Ponto de Orvalho (°C)'].min()),
        max_value=float(df['Ponto de Orvalho (°C)'].max()),
        value=(float(df['Ponto de Orvalho (°C)'].min()), float(df['Ponto de Orvalho (°C)'].max())),
    )


# Filtra a umidade relativa
def FiltroUmidadeRelativa(df: DataFrame):
    return st.sidebar.slider(
        'Umidade Relativa (%):',
        min_value=float(df['Umidade Relativa (%)'].min()),
        max_value=float(df['Umidade Relativa (%)'].max()),
        value=(float(df['Umidade Relativa (%)'].min()), float(df['Umidade Relativa (%)'].max())),
    )


# Filtro da umidade máxima
def FiltroUmidadeMaxima(df: DataFrame):
    return st.sidebar.slider(
        'Umidade Máxima (%):',
        min_value=float(df["Umidade Máxima (%)"].min()),
        max_value=float(df["Umidade Máxima (%)"].max()),
        value=(float(df["Umidade Máxima (%)"].min()), float(df["Umidade Máxima (%)"].max())),
    )


# Filtro da umidade mínima
def FiltroUmidadeMinima(df: DataFrame):
    return st.sidebar.slider(
        'Umidade Mínima (%):',
        min_value=float(df["Umidade Mínima (%)"].min()),
        max_value=float(df["Umidade Mínima (%)"].max()),
        value=(float(df["Umidade Mínima (%)"].min()), float(df["Umidade Mínima (%)"].max())),
    )


# Filtra a direção do vento
def FiltroDirecaoVento(df: DataFrame):
    return st.sidebar.slider(
        'Direção Vento (°):',
        min_value=float(df['Direção Vento (°)'].min()),
        max_value=float(df['Direção Vento (°)'].max()),
        value=(float(df['Direção Vento (°)'].min()), float(df['Direção Vento (°)'].max())),
    )


# Filtra a velocidade máxima do vento
def FiltroVentoMaximo(df: DataFrame):
    return st.sidebar.slider(
        'Vento Máximo (m/s):',
        min_value=float(df['Vento máximo (m/s)'].min()),
        max_value=float(df['Vento máximo (m/s)'].max()),
        value=(float(df['Vento máximo (m/s)'].min()), float(df['Vento máximo (m/s)'].max())),
    )


# Filtra o vento por hora
def FiltroVentoHora(df: DataFrame):
    return st.sidebar.slider(
        'Vento Hora (m/s):',
        min_value=float(df['Vento hora (m/s)'].min()),
        max_value=float(df['Vento hora (m/s)'].max()),
        value=(float(df['Vento hora (m/s)'].min()), float(df['Vento hora (m/s)'].max())),
    )


#Filtra a cidades envolvidas
def FiltroCidade(df: DataFrame):
    return st.sidebar.multiselect(
        'Selecione a Cidade:',
        options=df['Cidade'].unique(),
        default=df['Cidade'].unique(),
    )


# Realiza a aplicação do filtro nos dados
def AplicarFiltros(df: pd.DataFrame):

    # Primeiro: selecionar a cidade ANTES de gerar sliders
    selected_cidade = FiltroCidade(df)
    df_cidade = df[df["Cidade"].isin(selected_cidade)]

    # Agora sim os sliders, baseados SOMENTE nas cidades selecionadas
    precip_min, precip_max = FiltroPrecipitacao(df_cidade)
    pressao_min, pressao_max = FiltroPressaoAtm(df_cidade)
    pressao_max_min, pressao_max_max = FiltroPressaoAtmMax(df_cidade)
    pressao_min_min, pressao_min_max = FiltroPressaoAtmMin(df_cidade)
    radiacao_min, radiacao_max = FiltroRadiacaoGlobal(df_cidade)
    temp_ar_min, temp_ar_max = FiltroTemperaturaAr(df_cidade)
    temp_orv_min, temp_orv_max = FiltroTemperaturaOrvalho(df_cidade)
    umid_rel_min, umid_rel_max = FiltroUmidadeRelativa(df_cidade)
    umid_max_min, umid_max_max = FiltroUmidadeMaxima(df_cidade)
    umid_min_min, umid_min_max = FiltroUmidadeMinima(df_cidade)
    vento_dir_min, vento_dir_max = FiltroDirecaoVento(df_cidade)
    vento_max_min, vento_max_max = FiltroVentoMaximo(df_cidade)
    vento_hora_min, vento_hora_max = FiltroVentoHora(df_cidade)

    # Aplicação de todos os filtros
    df_filtered = df_cidade[
        (df_cidade["Precipitacao (mm)"] >= precip_min) & (df_cidade["Precipitacao (mm)"] <= precip_max) &
        (df_cidade["Pressão Atmosférica (mB)"] >= pressao_min) & (df_cidade["Pressão Atmosférica (mB)"] <= pressao_max) &
        (df_cidade["Pressão Máxima (mB)"] >= pressao_max_min) & (df_cidade["Pressão Máxima (mB)"] <= pressao_max_max) &
        (df_cidade["Pressão Mínima (mB)"] >= pressao_min_min) & (df_cidade["Pressão Mínima (mB)"] <= pressao_min_max) &
        (df_cidade["Radiacao Global (KJ/m²)"] >= radiacao_min) & (df_cidade["Radiacao Global (KJ/m²)"] <= radiacao_max) &
        (df_cidade["Temperatura do Ar (°C)"] >= temp_ar_min) & (df_cidade["Temperatura do Ar (°C)"] <= temp_ar_max) &
        (df_cidade["Ponto de Orvalho (°C)"] >= temp_orv_min) & (df_cidade["Ponto de Orvalho (°C)"] <= temp_orv_max) &
        (df_cidade["Umidade Relativa (%)"] >= umid_rel_min) & (df_cidade["Umidade Relativa (%)"] <= umid_rel_max) &
        (df_cidade["Umidade Máxima (%)"] >= umid_max_min) & (df_cidade["Umidade Máxima (%)"] <= umid_max_max) &
        (df_cidade["Umidade Mínima (%)"] >= umid_min_min) & (df_cidade["Umidade Mínima (%)"] <= umid_min_max) &
        (df_cidade["Direção Vento (°)"] >= vento_dir_min) & (df_cidade["Direção Vento (°)"] <= vento_dir_max) &
        (df_cidade["Vento máximo (m/s)"] >= vento_max_min) & (df_cidade["Vento máximo (m/s)"] <= vento_max_max) &
        (df_cidade["Vento hora (m/s)"] >= vento_hora_min) & (df_cidade["Vento hora (m/s)"] <= vento_hora_max)
    ]

    # Feedback
    if df_filtered.empty:
        st.warning('Nenhum dado corresponde aos filtros selecionados. Por favor, ajuste os filtros.')
        st.stop()
    else:
        st.subheader('✅ Dados Filtrados')
        st.write("Cidades incluídas:", df_filtered['Cidade'].unique())
        st.dataframe(df_filtered)

    return df_filtered


# Realiza a fitlragem dos outliers e substitui colunas vazias por valores da média
def LimpaOutliers(df: pd.DataFrame):
    st.subheader("🔧 Tratamento de Dados Ausentes e Outliers")

    df_limpo = df.copy()
    outlier_counts = {}

    # Apenas colunas numéricas
    colunas_numericas = df_limpo.select_dtypes(include=['float64', 'int64']).columns.tolist()

    # Substituir valores ausentes pela média da coluna
    df_limpo = df_limpo.fillna(df_limpo.mean(numeric_only=True))

    # Tratamento de outliers por coluna
    for coluna in colunas_numericas:
        ExibeValor = True

        while True:
            Q1 = df_limpo[coluna].quantile(0.05)
            Q3 = df_limpo[coluna].quantile(0.95)
            IQR = Q3 - Q1
            limite_inferior = Q1 - 1.5 * IQR
            limite_superior = Q3 + 1.5 * IQR

            outliers = df_limpo[(df_limpo[coluna] < limite_inferior) | (df_limpo[coluna] > limite_superior)]
            num_outliers = len(outliers)

            if ExibeValor:
                outlier_counts[coluna] = num_outliers
                ExibeValor = False

            if num_outliers == 0:
                break
            else:
                mediana = df_limpo[coluna].median()
                df_limpo[coluna] = df_limpo[coluna].apply(
                    lambda x: mediana if x < limite_inferior or x > limite_superior else x
                )

    # Exibição do log dos outliers tratados
    for coluna, count in outlier_counts.items():
        if count > 0:
            st.write(f" Coluna **'{coluna}'** possuía **{count} outliers**, substituídos pela mediana.")

    st.success("✅ Tratamento de valores ausentes e outliers concluído.")

    return df_limpo


# Preparação dos dados de modelagem
def PreparaDados(df: DataFrame):

    # Remover colunas não numéricas que não são úteis para o modelo
    for col in ["Data (YYYY-MM-DD)", "Hora (UTC)", "Hora UTC", "Radiação Clobal (Kj/m²)"]:
        if col in df.columns:
            df = df.drop(columns=col)

    # Se necessário, transformar variáveis categóricas em dummies (como cidade)
    df = pd.get_dummies(df, columns=['Cidade'], drop_first=True)

    # Converter a variável alvo para numérica
    df['Desastre Natural'] = df['Desastre Natural'].astype(int)

    #  Garantir que não há valores NaN após a transformação
    df = df.fillna(df.median(numeric_only=True))
    # Se ainda restar algum NaN (por colunas categóricas), substituir por zero
    df = df.fillna(0)

    # Separar X (variáveis independentes) e y (variável dependente)
    X = df.drop(columns=['Desastre Natural'])
    Y = df['Desastre Natural']

    # Verificar se há dados suficientes
    if len(X) < 2 or Y.nunique() < 2:
        st.warning(
            'Dados insuficientes para treinar o modelo. Por favor, ajuste os filtros para incluir mais dados e mais de uma classe.')
        st.stop()
    else:
        st.write(f'**Total de registros após filtragem:** {len(X)}')
        st.success('✅ Dados prontos para modelagem.')

    return X, Y


# Treinamento do modelo (Floresta Aleatória
def TreinarModelo(X, Y):
    st.header('Treinar o Modelo de Machine Learning')

    # Dividir os dados em treino e teste
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X_train, Y_train)
    Y_pred_modelo = modelo.predict(X_test)

    # Avaliar o modelo
    st.write("Acurácia do modelo (R² no conjunto de teste): {:.4f}".format(modelo.score(X_test, Y_test)))
    st.write("Erro médio absoluto: {:.4f}".format(mean_absolute_error(Y_test, Y_pred_modelo)))
    st.write("Raiz do erro quadrático médio (RMSE): {:.4f}".format(mean_squared_error(Y_test, Y_pred_modelo)))
    st.write("Erro percentual médio absoluto (MAPE): {:.4f}".format(np.mean(np.abs((Y_test - Y_pred_modelo) / Y_test)) * 100))

    return modelo, X_train


# Subalgoritmo para realizar as previsões
def RealizarPrevisao(modelo, X_treinado):
    st.subheader('Insira os Dados para Previsão')

    # Coletar os nomes das colunas
    colunas_entrada = X_treinado.columns.tolist()

    # Inicializar dicionário para inputs
    entrada = {}

    # Inputs manuais numéricos (ajuste conforme suas variáveis reais)
    for col in colunas_entrada:
        if "Cidade_" in col:
            continue  # será tratado depois com dummies
        elif "_(°C)" in col or "Temperatura" in col or "Orvalho" in col:
            entrada[col] = st.number_input(f'{col}', value=20.0)
        elif "Precipitacao" in col or "Precipitação" in col:
            entrada[col] = st.number_input(f'{col}', value=5.0)
        elif "Umidade" in col:
            entrada[col] = st.number_input(f'{col}', value=80.0)
        elif "Vento" in col:
            entrada[col] = st.number_input(f'{col}', value=1.0)
        elif "Pressão" in col:
            entrada[col] = st.number_input(f'{col}', value=1000.0)
        elif "Radiação" in col:
            entrada[col] = st.number_input(f'{col}', value=10000.0)
        else:
            entrada[col] = st.number_input(f'{col}', value=0.0)

    # Cidade: campo categórico dummificado
    cidades_colunas = [col for col in colunas_entrada if col.startswith("Cidade_")]
    cidades_opcoes = [c.replace("Cidade_", "") for c in cidades_colunas]
    cidade_escolhida = st.selectbox("Cidade", cidades_opcoes)

    for cidade_col in cidades_colunas:
        entrada[cidade_col] = 1 if cidade_col == f"Cidade_{cidade_escolhida}" else 0

    # Montar DataFrame com as colunas
    input_df = pd.DataFrame([entrada])

    # Garantir mesma ordem de colunas
    input_df = input_df[X_treinado.columns]

    # Realizar a previsão
    previsao = modelo.predict(input_df)

    st.subheader("🧠 Resultado da Previsão")
    if previsao[0] == 1:
        st.error("⚠️ Existe risco de ocorrência de desastre natural!")
    else:
        st.success("✅ Sem indícios de desastre natural para os parâmetros informados.")


# ============================================================================================================
#                                         PROGRAMA PRINCIPAL
# ============================================================================================================


# Configurações da página e título
st.set_page_config(
    page_title='Modelo Preditivo',
    page_icon='📊',
    layout='wide'
    )
st.title('Modelo Preditivo')


# Carregamento dos Dados
conexao = ConexaoServidor(user, password, server)

if conexao == True:

# ---------------------------VISÃO GERAL DOS DADOS-----------------------------
    # Visão Geral dos Dados
    banco = ListaCompleta()

    #Filtragem de dados
    st.sidebar.title('Filtros de Dados')
    st.sidebar.subheader('Intervalos das Variáveis Numéricas')

    # Chamada dos dados para filtragem
    banco_copy = AplicarFiltros(banco)

# ------------------------PREPARAÇÃO PARA A MODELAGEM--------------------------

    st.header('Preparar os Dados para Modelagem')
    banco_tratado = LimpaOutliers(banco_copy)
    X, Y = PreparaDados(banco_tratado)

# ------------------------TREINAMENTO PARA A MODELAGEM--------------------------

    modelo, X_treinado = TreinarModelo(X,Y)

# ------------------------TREINAMENTO PARA A MODELAGEM--------------------------

    st.header('Fazer Previsões com o Modelo')
    RealizarPrevisao(modelo, X_treinado)

else:
    st.error("Falha de conexão com o banco de dados")