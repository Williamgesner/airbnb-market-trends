# 📊 Explorando tendências do mercado do Airbnb em Nova York  

**👤 LinkedIn:** [William Gesner](https://www.linkedin.com/in/william-gesner/)  

---
## 📝 Descrição  
Este projeto consistiu em **explorar e manipular dados do Airbnb na cidade de Nova York**, utilizando arquivos em diferentes formatos (`.csv`, `.xlsx`, `.tsv`).  
O foco foi **importar, limpar e combinar os datasets** para gerar insights sobre preços, tipos de acomodações e datas de avaliações.  

Esse tipo de atividade é diretamente relacionado ao trabalho de um **Engenheiro de Dados**, pois envolve integração de múltiplas fontes, padronização e preparação de dados para análises futuras.  

## 🎯 Objetivo  
O objetivo principal foi aplicar técnicas de **ETL (Extract, Transform, Load)** em dados reais do Airbnb para responder perguntas de negócio relevantes para uma startup imobiliária:  
- Qual foi a **primeira e a última data de avaliação** entre os anúncios?  
- Quantos anúncios correspondem a **quartos privativos**?  
- Qual é o **preço médio** dos anúncios?  
- Consolidar os resultados em um **único DataFrame** chamado `review_dates`, com as colunas:  
  - `first_reviewed`  
  - `last_reviewed`  
  - `nb_private_rooms`  
  - `avg_price`  

## 🔎 Análise  
Durante o projeto, foram trabalhados pontos essenciais de Engenharia de Dados:  
- **Importação de múltiplos formatos de arquivos** (`CSV`, `TSV`, `Excel`).  
- **Padronização de colunas** para permitir integração correta entre datasets distintos.  
- **Limpeza de dados**, como tratamento de datas e consistência de tipos de variáveis.  
- **Cálculo de estatísticas descritivas** (contagem, média arredondada).  
- **Criação de um DataFrame consolidado** com variáveis de interesse para stakeholders.  

O maior aprendizado foi perceber como a combinação de dados de fontes heterogêneas gera uma visão integrada, algo essencial para análises estratégicas em empresas.  

## 🛠️ Ferramentas Utilizadas  
- **Python** 🐍  
- **Pandas** para manipulação, integração e análise dos dados  
- **VSCode** como ambiente de desenvolvimento  
- **CSV, Excel e TSV** como formatos de entrada  
- **Markdown** para documentação de projetos no GitHub.  

## 🧩 Tarefas realizadas  
- Leitura de três datasets: `airbnb_price.csv`, `airbnb_room_type.xlsx`, `airbnb_last_review.tsv`.  
- Padronização de colunas e integração dos dados em um único DataFrame.  
- Identificação das datas de avaliações mais antigas e recentes.  
- Contagem de anúncios classificados como **quartos privativos**.  
- Cálculo do **preço médio dos anúncios**.  
- Criação do DataFrame final `review_dates` consolidando os insights obtidos.  

## ✅ Conclusão  
O projeto resultou em um **DataFrame consolidado com informações estratégicas sobre o mercado do Airbnb em Nova York**, respondendo perguntas-chave de negócio para uma startup imobiliária.  
Além de ajudar na consolidação e no domínio em Python e Pandas, ele demonstrou a importância da **integração de múltiplas fontes de dados**, habilidade essencial para qualquer **Engenheiro de Dados**.  

👉 Este projeto está diretamente conectado à minha transição de carreira, mostrando na prática como aplicar **boas práticas de coleta, transformação e análise de dados** para gerar valor em cenários do mundo real.
