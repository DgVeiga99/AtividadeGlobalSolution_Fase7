# Atividade Global Solution - Fase 7

##  🎯 Tema

Com a intensificação das mudanças climáticas, o Brasil tem testemunhado um crescimento acentuado na frequência e severidade de eventos meteorológicos extremos, como tempestades, enchentes e deslizamentos. Tragédias em cidades como Petrópolis (RJ), Recife (PE), São Sebastião (SP) e em diversas regiões do Vale do Itajaí (SC) evidenciam o impacto direto desses fenômenos: centenas de mortos, milhões em prejuízos e milhares de pessoas desabrigadas.

Diante desse cenário, este projeto propõe o desenvolvimento de um **modelo preditivo de tempestades no Brasil utilizando machine learning**, com o objetivo de fornecer alertas antecipados baseados em dados históricos reais do INMET (Instituto Nacional de Meteorologia). A escolha do tema é justificada pela urgência de soluções tecnológicas que auxiliem na prevenção de catástrofes naturais.

A proposta se concretiza por meio de um sistema completo, que envolve o processamento de dados meteorológicos, integração com banco de dados Oracle, modelagem preditiva com Random Forest, e interface em Streamlit. Futuramente, o sistema poderá ser expandido para incluir sensores físicos via ESP32 e serviços de notificação por nuvem (AWS SES/SNS), tornando-o um instrumento acessível para apoio a decisões em tempo real.

---

## 📅 Dados Utilizados

* Dados climáticos do INMET (históricos regionais);
* Registros de desastres naturais do site disasterscharter.org;
* Estrutura padronizada com 20+ colunas meteorológicas;
* Base consolidada: `Base_Unificada_INMET.xlsx`.

---

## 📟 Etapas e Lógica da Solução

* 📅 **Aquisição de Dados**: Coleta de séries temporais do INMET, correlacionadas com registros históricos de desastres documentados visualmente (Imagem 1).
* 🧹 **Limpeza e Unificação**: Criação do notebook `DiegoVeiga_RM560658_Fase7_GlobalSolution.ipynb`, responsável por consolidar os dados em uma única base estruturada (`Base_Unificada_INMET`).
* 📈 **Banco de Dados**: Modelagem e criação da tabela `tempestade` com `CriaçãoTabela.sql`, e inserção automatizada dos dados processados via `InserçãoDados.sql`.
* 🌐 **Interface Web**: Implementação de uma aplicação interativa em Streamlit com navegação por páginas modulares.
* 🤖 **Machine Learning**: Treinamento e avaliação de um modelo Random Forest com métricas confiáveis, além de interface para previsões manuais baseadas em parâmetros selecionáveis.

---

## 🧹 Processamento e Estrutura de Dados

### 📌 `DiegoVeiga_RM560658_Fase7_GlobalSolution.ipynb`

Este notebook é responsável pela **automação do processo de unificação e saneamento de dados meteorológicos** do INMET. As escolhas metodológicas visam garantir a qualidade dos dados utilizados no modelo preditivo:

* Leitura e integração de múltiplos arquivos `.CSV`/`.XLSX` por cidade e faixa temporal;
* Padronização de colunas e conversão de tipos (data/hora para ISO);
* Exclusão de duplicatas e tratamento de valores ausentes com critérios estatísticos;
* Inclusão da coluna `desastre_natural` com base em cruzamentos com fontes históricas de desastres;
* Exportação para o arquivo `Base_Unificada_INMET.xlsx`, base central de alimentação da aplicação.

Essa estrutura reforça a consistência, confiabilidade e reprodutibilidade dos dados utilizados.

### 📈 Arquivos SQL

#### 🧱 `CriaçãoTabela.sql`

O script define a estrutura da tabela `tempestade` no banco Oracle, projetada para armazenar todas as variáveis necessárias à análise preditiva:

* Campos meteorológicos (precipitação, pressão, radiação, temperatura, umidade, vento);
* Identificação temporal (data, hora UTC);
* Localização (cidade);
* Variável alvo (`desastre_natural`) para aprendizado supervisionado.

A escolha dos tipos (`VARCHAR2`, `FLOAT`, `DATE`) garante compatibilidade e desempenho no banco de dados FIAP.

#### 📄 `InserçãoDados.sql`

Script auxiliar que realiza a **inserção automatizada dos registros** processados. Pode ser gerado via notebook ou scripts adicionais. Foi utilizado para simular a inserção de dados via ESP32, que estaria em um local estratégico para a captura dos daodos.

---

## 📊 Funcionalidades do Sistema

### 🧝 `Apresentação.py`

* Página de boas-vindas e descrição geral do sistema;
* Explica o propósito do projeto e o contexto dos desastres analisados.

### 📃 `Banco_de_Dados.py`

* Gerencia a conexão com o banco Oracle;
* Realiza consulta SQL e converte os dados em DataFrame para uso em todas as páginas.

### 📈 `1_Visão_Geral.py`

* Exibe informações básicas do dataset: dimensões, tipos, valores nulos;
* Gera estatísticas descritivas de forma automatizada.

### 📊 `2_Análise_Unitária.py`

* Visualiza a distribuição individual das variáveis climáticas e categóricas;
* Usa gráficos interativos (Plotly) para melhor compreensão dos dados.

### 🔗 `3_Análise_Correlação.py`

* Apresenta um mapa de calor com a correlação entre as variáveis numéricas;
* Suporte visual para entender as inter-relações entre os fatores climáticos.

### 🤖 `4_Modelo_Preditivo.py`

* Interface central do modelo de machine learning;
* Permite filtragem por cidade e faixa de variáveis;
* Realiza pré-processamento e treinamento com Random Forest;
* Apresenta métricas (R², MAE, RMSE, MAPE) e realiza previsões customizadas.

---

## 📊 Avaliação do Modelo

O modelo Random Forest demonstrou desempenho consistente ao ser testado com registros reais de diferentes regiões. Os principais destaques incluem:

* **Acurácia (R²)** superior a 80% nas localidades com maior número de registros;
* Capacidade de identificar padrões relevantes entre variáveis meteorológicas e ocorrência de desastres;
* Interface de previsão robusta e personalizável.

A escolha do Random Forest foi motivada pela sua robustez a outliers, baixo risco de overfitting e excelente desempenho com dados tabulares heterogêneos.

---

## 🔌 Integração com ESP32 e Simulação no Wokwi

Como prova de conceito para futuras implementações físicas do sistema, foi desenvolvido um protótipo funcional na plataforma **[Wokwi](https://wokwi.com/projects/433061603613628417)**, que simula o uso de sensores ambientais conectados ao **ESP32 DevKit V4**.

### ⚙️ Componentes Utilizados

A simulação contempla os seguintes dispositivos eletrônicos:

- 🧠 **ESP32 DevKit V4** – Microcontrolador responsável pela aquisição e transmissão dos dados;
- 🌡️ **Sensor DHT22** – Mede temperatura e umidade relativa do ar;
- 🔆 **Potenciômetro** – Simula a intensidade de radiação solar para calibração dos valores analógicos;
- 🔌 **Protoboard virtual** – Para facilitar as conexões dos componentes;
- 🔋 Fontes de alimentação e conexões com GND e 5V devidamente configuradas.

### 🧾 Bibliotecas Utilizadas

As seguintes bibliotecas foram integradas no ambiente de simulação Wokwi:

- `DHT sensor library for ESPx`
- `DHT sensor library`

Essas bibliotecas garantem a correta leitura dos dados de temperatura e umidade do sensor DHT22.

### 📑 Funcionalidades do Código

O código desenvolvido na IDE do Wokwi (`sketch.ino`) realiza:

1. **Inicialização da comunicação serial e dos sensores**;
2. **Leitura periódica** dos valores de temperatura, umidade e radiação simulada (potenciômetro);
3. **Registro contínuo** dos dados no monitor serial para visualização em tempo real;
4. **Cálculo do ponto de orvalho**, com identificação dos valores máximos e mínimos.

### 🖼️ Diagrama de Ligações

A arquitetura física simulada foi documentada no arquivo `diagram.json`, contendo:

- Conexões entre pinos digitais/analógicos do ESP32 com os sensores;
- Alimentação correta dos componentes;
- Fiação representativa das ligações em protoboard.

Esse diagrama foi produzido diretamente pela interface do Wokwi, garantindo a fidelidade do circuito para futura replicação física.

---

## 📹 Demonstração

> Link do vídeo: \[[https://youtube.com/SEU\_LINK\_AQUI]((https://youtu.be/8uJGfc0_yOU))]

---
