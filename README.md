


Recomendador de Filmes por Similaridade

Este projeto é uma IA simples que recomenda filmes semelhantes com base na descrição de cada um, utilizando TF-IDF e similaridade do cosseno.

Como funciona
	•	Cada filme possui uma descrição.
	•	A IA transforma essas descrições em vetores numéricos.
	•	Em seguida, mede a similaridade com o filme escolhido pelo usuário.
	•	Retorna os filmes mais parecidos.

Tecnologias usadas
	•	Python
	•	Scikit-Learn


## Etapa 3 - Definição do Problema e da IA/ML 

Problema a Resolver / Contexto da Aplicação

Com o aumento da quantidade de produtos, conteúdos e opções disponíveis online, muitos usuários têm dificuldade para encontrar aquilo que realmente atenda às suas preferências. Isso gera perda de tempo, frustração e, muitas vezes, escolhas ruins. O problema que o projeto busca resolver é exatamente essa “dor”: como ajudar um usuário a descobrir itens relevantes sem precisar navegar por milhares de opções manualmente.

A solução proposta é um sistema recomendador, capaz de sugerir itens similares com base nas escolhas ou interesses do usuário. O objetivo de “funcionar” significa que as recomendações apresentadas sejam coerentes, relevantes e úteis para o usuário final — isto é, que de fato ajudem na tomada de decisão.

⸻

Tipo de IA/ML Escolhido e Por Que É Adequado

A técnica escolhida foi um Sistema de Recomendação baseado em similaridade (Content-Based Filtering) utilizando medidas matemáticas (como similaridade de cosseno) para encontrar itens semelhantes entre si. Esse método é adequado porque:
	•	Não exige grandes quantidades de usuários ou de avaliações, funcionando mesmo com poucos dados.
	•	Permite recomendar itens parecidos com base nas características do item selecionado.
	•	É simples, eficiente e atende ao objetivo principal do projeto: fornecer recomendações rápidas e diretas.

Além disso, sistemas de recomendação são uma aplicação clássica de IA/ML, presentes em plataformas como Netflix, Spotify e Amazon, mostrando sua relevância e utilidade prática.


Etapa 4 — Dados, Desenvolvimento e Treino/Teste
1) Dados Utilizados

Para este projeto foi utilizada uma base de filmes contendo título, descrição e gêneros.
As descrições textuais são essenciais para que o modelo calcule a similaridade entre os filmes.

Exemplo de estrutura do arquivo filmes.csv:
| Coluna      | Tipo   | Descrição                    |   |
| ----------- | ------ | ---------------------------- | - |
| movie_id    | int    | Identificador único do filme |   |
| title       | string | Título do filme              |   |
| description | string | Sinopse/descrição do filme   |   |
| genres      | string | Gêneros separados por `      | ` |

2) Pré-processamento

As etapas de preparação dos dados incluíram:

Remoção de nulos nas descrições

Limpeza básica do texto

Extração de features com TF-IDF

Separação em treino e teste com divisão 80/20:

train_test_split(..., test_size=0.2, random_state=42)

3) Modelo de IA Implementado

Foi utilizado um sistema de recomendação baseado em conteúdo (Content-Based Filtering):

Cada filme tem sua descrição convertida em um vetor TF-IDF

As similaridades são calculadas usando cosseno

O sistema recomenda os filmes mais próximos ao escolhido pelo usuário

Esse tipo de modelo é adequado por ser simples, eficiente e não depender de avaliações de usuários.

4) Treino e Teste

O processo de treino consistiu em:

Ajustar o TF-IDF a partir dos dados de treino

Gerar os vetores dos filmes

Calcular a matriz de similaridade

Para medir desempenho, foi usada a métrica Precision@K, que verifica se o modelo é capaz de sugerir corretamente filmes semelhantes dentro do top-K retornado.

Os arquivos gerados foram salvos na pasta models/.

5) Reprodutibilidade

O projeto inclui:

requirements.txt com todas as dependências

Scripts organizados em src/

Artefatos salvos na pasta models/

Código estruturado para sempre usar random_state=42, garantindo resultados reproduzíveis
Com isso, qualquer pessoa pode baixar o repositório e rodar:
pip install -r requirements.txt
python src/preprocess.py
python src/recomendador.py

---

 Versão Resumida / README Formatado 
Recomendador de Filmes por Similaridade
Equipe

Nome Sobrenome — RA: 0000000
Nome Sobrenome — RA: 0000000
Turma: X | Curso: Y | Período: Noturno | Ano: 2025

Problema

Com a enorme quantidade de filmes disponíveis em plataformas digitais, os usuários têm dificuldade em encontrar opções que realmente combinem com seus gostos. Esse projeto resolve esse problema oferecendo um sistema recomendador baseado em similaridade, capaz de sugerir filmes parecidos com base na descrição de um título escolhido.

Abordagem de IA

O sistema utiliza Content-Based Filtering, transformando descrições de filmes em vetores numéricos com TF-IDF e calculando a similaridade usando cosseno.

Essa técnica é adequada pois:

Funciona mesmo com poucos dados

Não depende de avaliações

Retorna recomendações relevantes rapidamente

Métrica principal: Precision@K

Dados
Coluna	Tipo	Descrição
movie_id	int	ID único do filme
title	string	Título
description	string	Sinopse
genres	string	Gêneros separados por “,”
Pré-processamento

Remoção de nulos

Limpeza de texto

TF-IDF

Treino/teste 80/20 (random_state=42)

Como reproduzir
1. Clonar o repositório
git clone https://github.com/usuario/nome-do-projeto.git
cd nome-do-projeto

2. Criar ambiente virtual

Windows

python -m venv .venv
.venv\Scripts\activate


Linux/macOS

python3 -m venv .venv
source .venv/bin/activate

3. Instalar dependências
pip install -r requirements.txt

4. Pré-processar os dados
python src/preprocess.py

5. Rodar o recomendador
python src/recomendador.py

6. Executar o programa principal
python src/main.py --seed 42

Resultados

Métrica usada: Precision@K
(Substitua pelos resultados reais depois.)

Estrutura do Projeto
├── data/
│   ├── filmes.csv
│   └── processed/
├── models/
│   ├── tfidf_vectorizer.pkl
│   └── similarity_matrix.npy
├── src/
│   ├── preprocess.py
│   ├── recomendador.py
│   └── main.py
├── reports/
│   └── figures/
├── notebooks/
│   └── exploracao.ipynb
├── requirements.txt
└── README.md


