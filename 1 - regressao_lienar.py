from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

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

Y = [1, 1 ,0 ,0, 1, 0, 1, 0, 1, 0, 1, 0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(frases).toarray()

print("Palavras", vectorizer.get_feature_names_out())
print(X)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

EmotionIA = LogisticRegression()

#Treinando Modelo
EmotionIA.fit(x_train, y_train)

y_pred =  EmotionIA.predict(x_test)

acurity = accuracy_score(y_test, y_pred)

print("Acurácia Modelo", acurity)