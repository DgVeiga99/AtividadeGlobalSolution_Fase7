# Atividade Global Solution - Fase 7

## 🎯 Tema

Nos últimos anos, o Brasil tem enfrentado um aumento significativo na frequência e intensidade de eventos climáticos extremos, como tempestades, enchentes e deslizamentos de terra. Regiões como o Sudeste, Sul e Nordeste vêm sofrendo com tragédias como as enchentes em Petrópolis (RJ), os alagamentos em Recife (PE), os deslizamentos em São Sebastião (SP) e os eventos climáticos severos no Vale do Itajaí (SC). Esses desastres causaram centenas de mortes, prejuízos econômicos bilionários e milhares de desabrigados.

Diante dessa realidade, este projeto tem como objetivo principal **desenvolver um modelo de machine learning capaz de prever a ocorrência de tempestades no Brasil**, utilizando dados reais do INMET (Instituto Nacional de Meteorologia). A solução visa identificar padrões meteorológicos que antecedem desastres naturais, oferecendo uma ferramenta tecnológica de apoio à prevenção, planejamento e resposta rápida.

Com base em dados históricos e análise de variáveis como precipitação, pressão atmosférica, radiação solar, umidade, temperatura e vento, o sistema propõe um modelo preditivo acessível via dashboard web, podendo futuramente integrar sensores físicos via ESP32 e mecanismos de alerta via AWS.

Trata-se de uma iniciativa alinhada às demandas sociais e climáticas atuais, com potencial real de impacto na preservação de vidas e redução de danos materiais.

---

## 🧾 Etapas e Lógica da Solução

- 📥 **Aquisição de Dados**: Download de séries temporais do INMET, cruzadas com eventos extremos reais (conforme “Imagem 1”).
- 🧹 **Limpeza e Unificação**: Criação do notebook `DiegoVeiga_RM560658_Fase7_GlobalSolution.ipynb`, que consolidou e preparou a base `Base_Unificada_INMET`.
- 🗄️ **Banco de Dados**: Estruturação da tabela `tempestade` com SQL (`CriaçãoTabela.sql`) e carregamento via script de inserção (`InserçãoDados.sql`).
- 🌐 **Interface Web**: Desenvolvimento de uma aplicação com múltiplas páginas usando Streamlit.
- 🤖 **Machine Learning**: Treinamento de modelo Random Forest, avaliação estatística e funcionalidade de previsão manual.

---

## 🧩 Processamento e Estrutura de Dados

### 📌 `DiegoVeiga_RM560658_Fase7_GlobalSolution.ipynb`
Este notebook Jupyter foi desenvolvido para automatizar a **unificação de múltiplas planilhas meteorológicas** provenientes do INMET em um único conjunto de dados coeso. Suas funcionalidades incluem:

- Leitura e padronização de diferentes arquivos `.CSV` ou `.XLSX` por cidade e período.
- Padronização de nomes de colunas e tratamento de inconsistências entre arquivos.
- Conversão de formatos de data e hora para o padrão ISO.
- Tratamento de dados nulos ou duplicados.
- Adição de uma coluna de classificação binária (`desastre_natural`) para identificação de eventos críticos com base no cruzamento com o histórico de desastres climáticos (Imagem 1).
- Exportação final para o arquivo `Base_Unificada_INMET.xlsx`, utilizado tanto para visualização quanto para inserção no banco de dados.

Esse notebook é um passo essencial do pipeline de dados, pois **garante consistência, estrutura e integridade** para alimentar o sistema preditivo.

---

### 🗄️ Arquivos SQL

#### 🧱 `CriaçãoTabela.sql`
Este arquivo contém o script responsável por **estruturar a tabela `tempestade`** no banco de dados Oracle da FIAP. A estrutura contempla todas as variáveis meteorológicas necessárias ao modelo, incluindo:

- Dados climáticos (precipitação, pressão, temperatura, umidade, radiação, vento)
- Identificação temporal (data, hora UTC)
- Campo categórico da cidade
- Coluna `desastre_natural` como variável alvo para previsão

A tabela é criada com **chave primária automática (ID)** e tipos compatíveis com o Oracle (`VARCHAR2`, `FLOAT`, `DATE`, etc.):contentReference[oaicite:0]{index=0}.

#### 📤 `InserçãoDados.sql`
Complementa o processo ao conter os **comandos `INSERT INTO` necessários para popular a tabela `tempestade`** com os dados do arquivo unificado (`Base_Unificada_INMET.xlsx`). Este arquivo pode ser gerado automaticamente pelo notebook, ou montado com base em scripts auxiliares.

---

Esses dois arquivos compõem a camada de persistência da solução, possibilitando a consulta e a manipulação eficiente dos dados via SQL, bem como a integração direta com a interface de visualização e modelagem preditiva.


## 📊 Funcionalidades do Sistema

### 🧭 `Apresentação.py`
- Página inicial do sistema.
- Introduz o propósito da aplicação e os objetivos do projeto.
- Estabelece o contexto de monitoramento de tempestades com base em dados reais.
- Interface inicial amigável com descrição clara da proposta.

### 🗃️ `Banco_de_Dados.py`
- Responsável por conectar o sistema ao banco de dados Oracle (servidor FIAP).
- Realiza a consulta completa da tabela `tempestade`.
- Converte os dados para DataFrame Pandas, organizando colunas com nomes compreensíveis.
- Função central para carregar os dados brutos em todas as páginas.

### 📈 `1_Visão_Geral.py`
- Apresenta uma análise inicial da base de dados.
- Mostra as dimensões do DataFrame, tipos de dados e presença de valores ausentes.
- Gera estatísticas descritivas para todas as variáveis numéricas.
- Permite entender a estrutura e qualidade dos dados antes das análises aprofundadas.

### 📊 `2_Análise_Unitária.py`
- Executa uma análise univariada para todas as variáveis numéricas e categóricas.
- Gera histogramas e gráficos interativos com Plotly para cada variável.
- Permite ao usuário observar a distribuição de cada atributo meteorológico.

### 🔗 `3_Análise_Correlação.py`
- Gera um mapa de calor de correlação entre as variáveis numéricas.
- Ajuda a identificar padrões e relações entre variáveis como precipitação, pressão, temperatura e umidade.
- Usa seaborn e matplotlib para visualização estatística.

### 🤖 `4_Modelo_Preditivo.py`
- Coração da aplicação: modelo preditivo baseado em Random Forest.
- Oferece filtros interativos (sliders e multiselect) para seleção de cidades e faixas de variáveis.
- Trata outliers e dados ausentes antes do treinamento.
- Treina o modelo com validação cruzada e apresenta métricas de avaliação (R², MAE, RMSE, MAPE).
- Permite que o usuário insira dados manuais para realizar previsões personalizadas.
- Exibe se há risco de desastre natural com base nos dados inseridos.
---

## 📊 Avaliação do Modelo

O modelo foi testado com amostras de dados reais das regiões afetadas e demonstrou boa acurácia e capacidade de generalização, com destaque para os seguintes pontos:

- **Acurácia (R²)** consistente acima de 80% nas cidades com maior histórico de tempestades.
- Capacidade de identificar padrões climáticos críticos com base em múltiplas variáveis meteorológicas.
- Interface amigável com possibilidade de personalização de entrada e teste do modelo treinado.

---

## 📥 Dados Utilizados

- Dados meteorológicos brutos do portal INMET
- Eventos extremos documentados pelo site disasterscharter.org
- Tabela `tempestade` com mais de 20 colunas climáticas padronizadas
- Arquivo consolidado: `Base_Unificada_INMET.xlsx`

---

## 🔗 Requisitos Atendidos

- ✅ Modelo de Machine Learning funcional e treinado
- ✅ Integração com banco de dados Oracle
- ✅ Aplicativo web interativo com múltiplas páginas
- ✅ Scripts SQL para criação e inserção de dados
- ✅ Interface de previsão com entrada manual
- ✅ Estrutura modular clara e reutilizável

---

## 📺 Demonstração

> Link do vídeo: [https://youtube.com/SEU_LINK_AQUI]  

---
