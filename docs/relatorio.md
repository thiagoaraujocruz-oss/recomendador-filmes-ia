## Etapa 3  - Definição do Problema e da IA/ML 

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

## Etapa 4 Dados, Desenvolvimento e Treino/Teste

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

Para poder replicar tudo, o repositório inclui:
	•	requirements.txt com todas as dependências
	•	Scripts organizados em src/
	•	Dados padronizados em data/
	•	Modelo salvo em models/
	•	Notebook ou script completo para rodar o pipeline

  ## Etapa 5 








































