from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

frases =  [
      "Estou feliz hoje!",  "Que dias maravilhoso!",  "Ganhei um prêmio, estou animado",
      "Amo estar com minha família", "Hoje o dia está incrível", "A vida é maravilhosa",
      "Estou radiante de felicidade", "Que notícia incrível, estou muito empolgado",
      "Felicidade é estar cercado por pessoas que amo!", "Consegui p emprego dos sonhos!",
      "O dia esta lindo, um sol maravilhoso!", "Recebi uma surpresa, estou animado",

      "Isso me deixa muito triste", "Estou deprimido e sem ânimo",  "Nada mais faz sentido, estou desanimado",
      "Estou chorando de tristeza", "Sinto um vazio enorme dentro de mim",  "Não tenho energia para fazer nada",
      "Meu dia foi horrível, estou exausto", "Estou me sentindo completamente sozinho",
      "Não consigo parar de chorar, estou muito triste", "Perdi alg muito importante para mim",
      "Hoje foi um dos piores dias da minha vida", "A tristeza está me consumindo"
]

rotulos = [1] * 12 + [0] * 12  #12 frases

vectorizer = CountVectorizer(ngram_range=(1, 2))

X = vectorizer.fit_transform(frases).toarray()

print("Palavras", vectorizer.get_feature_names_out())

x_train, x_test, y_train, y_test = train_test_split(X, rotulos, test_size=0.3, random_state=42)

EmotionIA = SVC(kernel='linear')

#Treinando Modelo
EmotionIA.fit(x_train, y_train)

y_pred_svm =  EmotionIA.predict(x_test)

acuracia_svm = accuracy_score(y_test, y_pred_svm)

print(f"Acurácia Modelo SVM : {acuracia_svm:.2f}")