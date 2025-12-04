Recomendador de Filmes por Similaridade

Projeto Integrador 2025 – UNINOVE
⸻
Equipe
➤ NOME: THIAGO DE ARAUJO CRUZ — RA: 2224105685
➤ NOME: VICTOR RODRIGUES ROCHA DA CRUZ — RA: 2224104116

PROFESSOR:FELIPE SANTOS DE JESUS

Objetivo do Projeto

Criar uma IA capaz de recomendar filmes semelhantes com base na descrição de cada obra, utilizando TF-IDF e similaridade do cosseno

Tecnologias Utilizadas

Python
Scikit-Learn

Estrutura Inicial do Projeto

recomendador-filmes-ia/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── reports/
│   └── figures/
├── notebooks/
│   └── exploratory.ipynb
├── src/
├── requirements.txt
└── README.md

Como o Sistema Funciona (Resumo)
	•	Cada filme possui uma descrição.
	•	A IA transforma as descrições em vetores TF-IDF.
	•	Calcula a similaridade entre filmes usando cosseno.
	•	Retorna os filmes mais parecidos com o escolhido pelo usuário.

