# data-pipeline-logistics
# 🚨 Data Pipeline Logístico: Auditoria e Limpeza Automatizada (Operação Cajamar)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Cleaning-purple.svg)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen.svg)

## 📌 Contexto do Projeto

Em operações logísticas de grande escala, o volume de dados gerado a cada turno é massivo. No entanto, bases alimentadas de forma descentralizada frequentemente sofrem com "dados sujos": bips duplicados, erros manuais de digitação, registros com tempos zerados e anomalias de sistema. 

Este projeto consiste em um **Data Pipeline 100% Automatizado** desenvolvido em Python que consome uma base histórica de **+105 mil linhas** diretamente do Google Sheets. O sistema atua em duas frentes: realiza um diagnóstico completo de qualidade dos dados (Data Auditing) e aplica regras de negócio rígidas para higienização e padronização, gerando um arquivo limpo e otimizado pronto para consumo em ferramentas de Business Intelligence (Power BI/Looker Studio).

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python:** Linguagem base para a construção do pipeline.
* **Pandas:** Manipulação de dados, agrupamento, filtros dinâmicos e exportação.
* **NumPy:** Suporte matemático para vetorização e identificação de anomalias numéricas.
* **Google Sheets Cloud Integration:** Integração via URL para consumo de dados em tempo real sem dependência de download manual de arquivos.

---

## ⚙️ Arquitetura do Pipeline (Como Funciona)

### 1. Módulo de Auditoria (Data Quality Assessment)
Antes de qualquer alteração, o script faz uma varredura completa na base bruta e exibe no terminal alertas de inconsistência baseados em regras de negócio:
* Identificação de linhas 100% duplicadas.
* Mapeamento de campos nulos (`NaN`) em colunas críticas de produtividade.
* Detecção de erros de digitação e caixa (ex: padronização de setores operacionais como `DV` e `RESSUBIDO`).
* Filtro de "Bips Bizarrros" (quantidades de peças negativas ou outliers extremos do sistema como `99999`).
* Erros de cronômetro (registros de produtividade com tempo igual ou menor que 0 segundos).

### 2. Módulo de Tratamento (ETL - Extract, Transform, Load)
Caso anomalias sejam encontradas, o pipeline inicia o processo de higienização automatizada:
* **Deduplicação:** Eliminação imediata de registros duplicados.
* **Tratamento de Nulos:** Remoção de linhas com ausência de IDs ou métricas essenciais.
* **Padronização de Strings:** Aplicação de `.str.upper()` e `.str.strip()` para eliminar espaçamentos invisíveis e padronizar caracteres.
* **Correction de Sintaxe:** Substituição ativa de desvios padrão da operação (ex: convertendo `RESUBIDO` para `RESSUBIDO`).
* **Filtro de Outliers:** Expulsão de falsos positivos numéricos no tempo e nas peças processadas.

---

## 📊 Resultados Obtidos

Ao executar o script, a base de dados passa pelo seguinte fluxo visível no console:

* **Entrada:** Base bruta consumida via nuvem contendo mais de **105.000 registros**.
* **Processamento:** Identificação em milissegundos de todas as quebras de padrão e anomalias de tempo/contagem.
* **Saída:** Geração automatizada do arquivo `dados_limpos_meli.csv`, estruturado em formato ideal para modelagem de dados (Star Schema) e livre de ruídos.

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:
```bash
git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
