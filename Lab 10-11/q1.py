import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from imblearn.over_sampling import SMOTE

df = pd.read_csv("creditcard.csv")

print("Original Shape:", df.shape)
print("\nOriginal Class Distribution:\n", df['Class'].value_counts())

df['Class'] = pd.to_numeric(df['Class'], errors='coerce')

df = df[df['Class'].notna()]

df['Class'] = df['Class'].astype(int)

df = df.fillna(df.mean(numeric_only=True))

print("\nAfter Cleaning:")
print("Shape:", df.shape)
print("NaN values:", df.isnull().sum().sum())
print("Class Distribution:\n", df['Class'].value_counts())

X = df.drop('Class', axis=1)
y = df['Class']

sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

print("\nAfter SMOTE:\n", pd.Series(y_res).value_counts())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_res)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_res, test_size=0.3, random_state=42, stratify=y_res
)


lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

def evaluate_model(name, y_test, y_pred):
    print(f"\n{name} Results:")
    print("-" * 35)
    print("Accuracy :", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall   :", recall_score(y_test, y_pred))
    print("F1 Score :", f1_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

evaluate_model("Logistic Regression", y_test, y_pred_lr)
evaluate_model("Random Forest", y_test, y_pred_rf)