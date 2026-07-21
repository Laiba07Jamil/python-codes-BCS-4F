import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("Mall_Customers.csv")

print("First 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

num_col = df.select_dtypes(include=['int64','float64']).columns
cat_col = df.select_dtypes(include=['object']).columns

for i in num_col :
    df[i] = df[i].fillna(df[i].mean())

for col in cat_col:
    df[col] = df[col].fillna(df[col].mode()[0])

Label = LabelEncoder()
for col in cat_col:
    df[col] = Label.fit_transform(df[col])
    
X = df.drop(columns=["Gender", "CustomerID"])
y = df["Gender"]

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = DecisionTreeClassifier(criterion = 'gini',max_depth = 5,random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n===== DECISION TREE RESULTS =====")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

print("==Training Accuracy==")
test1 = model.score(X_train, y_train)
testacc = test1 * 100
print(testacc)

print("===Testing Accuracy===")
test = accuracy_score(y_test , y_pred)
teactacc = test * 100
print(teactacc)

"""1. Import libraries
2. Load dataset
3. Check head(), columns(), null values
4. Handle missing values
5. Encode categorical columns
6. Define x and y
7. Train-test split
8. Scaling (if needed)
9. Create model
10. fit()
11. predict()
12. metrics"""