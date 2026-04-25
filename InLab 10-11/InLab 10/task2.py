import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("spam_dataset.csv")

print("Dataset Preview:")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nLabel Counts:")
print(df['label'].value_counts())

vectorizer = TfidfVectorizer(stop_words='english')

X = vectorizer.fit_transform(df['text'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n====================")
print("MODEL PERFORMANCE")
print("====================")

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

def predict_spam(text):
    text_vec = vectorizer.transform([text])
    pred = model.predict(text_vec)[0]
    
    return "Spam" if pred == 1 else "Not Spam"

print("\n====================")
print("SAMPLE PREDICTIONS")
print("====================")

print(predict_spam("Win a free iPhone now click link"))
print(predict_spam("Are we meeting tomorrow for lunch?"))
print(predict_spam("Urgent! Your bank account is suspended"))