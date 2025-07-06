import joblib
EmotionIa  = joblib.load("C:/Projetos/Projetos ItValley/venv/emotionIA_rf.pkl")
vectorizer = joblib.load("C:/Projetos/Projetos ItValley/venv/tfidf_vectorizer.pkl")

sentence = ["I am happy today"]

x = vectorizer.transform(sentence).toarray()

prediction = EmotionIa.predict(x)

print("Prediction:", "happy" if prediction[0] == 1 else "sad")