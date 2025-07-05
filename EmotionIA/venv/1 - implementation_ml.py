import joblib

EmotionIa  = joblib.load("emotionIA_rf.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

sentence = ["I am sad my job"]

x = vectorizer.transform(sentence).toarray()

prediction = EmotionIa.predict(x)

print("Prediction:", "happy" if prediction[0] == 1 else "sad")