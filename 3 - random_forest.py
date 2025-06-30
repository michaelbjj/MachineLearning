from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Expanding dataset with English sentences
sentences = [
    # HAPPY (1)
    "I am very happy today!", "What a wonderful day!", "I won a prize, I am excited!",
    "I love being with my family.", "Today is an amazing day!", "Life is wonderful!",
    "I am radiant with happiness!", "What an amazing news, I am thrilled!",
    "Happiness is being surrounded by people I love!", "I got the job of my dreams!",
    "The day is beautiful, a wonderful sun!", "I received an incredible surprise, I am excited!",
    "My heart is full of gratitude!", "The best feeling is being loved!",
    "There is nothing better than celebrating good achievements!", "I woke up full of hope today!",
    "I am extremely satisfied with everything in my life!", "Happiness lives inside me!",
    "Nothing can ruin this incredible day!", "It is wonderful to have amazing friends!",

    # SAD (0)
    "This makes me very sad.", "I am depressed and unmotivated.", "Nothing makes sense, I am discouraged.",
    "I am crying with sadness.", "I feel a huge emptiness inside me.", "I have no energy to do anything.",
    "My day was horrible, I am exhausted.", "I am feeling completely alone.",
    "I can't stop crying, I am very sad.", "I lost something very important to me.",
    "Today was one of the worst days of my life.", "Sadness is consuming me.",
    "Everything is going wrong, I see no way out.", "I feel trapped in an endless cycle.",
    "Each day seems harder than the other.", "I feel like I don't have the strength to continue.",
    "Emotional exhaustion is destroying me.", "Nothing I do seems to be enough.",
    "I am tired of everything, I just want to disappear.", "My heart is heavy with so much anguish."
]

labels = [1] * 20 + [0] * 20 

vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
X = vectorizer.fit_transform(sentences).toarray()

print("Vocabulary words", vectorizer.get_feature_names_out())

x_train, x_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

EmotionIA = RandomForestClassifier(n_estimators=100, random_state=42)
#Treinando Modelo
EmotionIA.fit(x_train, y_train)

y_pred_rf =  EmotionIA.predict(x_test)

acuracia_rf = accuracy_score(y_test, y_pred_rf)

print(f"Acurácia Modelo Random Forest : {acuracia_rf:.2f}")

joblib.dump(EmotionIA, 'emotionIA_rf.pkl')
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("Model Saved!")