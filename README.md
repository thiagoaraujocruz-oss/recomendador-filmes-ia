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
