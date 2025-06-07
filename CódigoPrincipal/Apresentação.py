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

# =============================================================================================================
#                                 BIBLIOTECAS, LISTAS E DICIONÁRIOS
# =============================================================================================================

import streamlit as st

# =============================================================================================================
#                                        PROGRAMA PRINCIPAL
# =============================================================================================================

# Condiguração da página principal
st.set_page_config(
    page_title='Monitoramento de Tempestades',
    page_icon='⛈️',
    layout='wide'
    )

# Apresentação do titulo da página
st.title('Monitoramento de Tempestades ⛈️')

# Descrição do sistema desenvolvido
st.write('Bem-vindo ao aplicativo de Monitoramento de Tempestades.')
st.markdown("""
       Criar uma solução digital capaz de monitorar tempestades no Brasil com base em dados reais
A aplicação utiliza lógica computacional, estruturas condicionais, laços de repetição e organização
de dados em Python para analisar e responder a eventos naturais extremos.
      A proposta visa mitigar os impactos desses eventos por meio de um sistema automatizado,
coerente e funcional, que processe informações, tome decisões com base em condições ambientais
e ofereça suporte à tomada de ação.
            """)