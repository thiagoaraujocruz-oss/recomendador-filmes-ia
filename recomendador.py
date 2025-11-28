import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Base de dados simples de filmes (vocês podem alterar os nomes depois)
filmes = {
    "Vingadores: Ultimato": "heróis lutando para salvar o universo, ação, ficção científica",
    "Homem-Aranha": "super-herói adolescente, ação, aventura",
    "Interestelar": "espaço, viagem no tempo, ficção científica, drama",
    "A Culpa é das Estrelas": "romance, drama, história emocionante",
    "O Rei Leão": "animação, aventura, animais, clássico",
    "Carros": "animação, corrida, carros",
}

# Vetorização do texto
vectorizer = TfidfVectorizer()
vetores = vectorizer.fit_transform(filmes.values())

def recomendar_filme(filme_usuario):
    if filme_usuario not in filmes:
        return "Filme não encontrado na base."

    # Similaridade
    idx = list(filmes.keys()).index(filme_usuario)
    similaridade = cosine_similarity(vetores[idx], vetores).flatten()

    # Ordenar por similaridade (exceto o próprio filme)
    indices_ordenados = np.argsort(similaridade)[::-1][1:4]

    recomendados = [list(filmes.keys())[i] for i in indices_ordenados]
    return recomendados

# Teste
if _name_ == "_main_":
    entrada = "Homem-Aranha"
    print("Filmes recomendados para:", entrada)
    print(recomendar_filme(entrada))
