from sklearn.feature_extraction.text import CountVectorizer

frases =  [
      "Estou feliz hoje!",
      "Que dias maravilhoso!",
      "Isso me deixa muito triste",
      "Estou deprimido e sem ânimo",
      "Ganhei um prêmio, estou animado",
      "Nada mais faz sentido, estou desanimado",
      "Amo estar com minha família",
      "Estou chorando de tristeza",
      "Hoje o dia está incrível",
      "Sinto um vazio enorme dentro de mim",
      "A vida é maravilhosa",
      "Não tenho energia para fazer nada",
]

rotulos = [1, 1 ,0 ,0, 1, 0, 1, 0, 1, 0, 1, 0]

vectorizer = CountVectorizer()
vector = vectorizer.fit_transform(frases).toarray()

print("Palavras", vectorizer.get_feature_names_out())
print(vector)