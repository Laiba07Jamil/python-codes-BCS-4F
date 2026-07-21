import numpy as num
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,f1_Score,r2_Score,accuracy_Score , precision , recall_score

df = pd.read_csv("Mall_Customers.csv")
x = df.copy()
y = df.pop("target")
print(df.head())

num_cols = df.select_dtypes(include=['int64','float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

cat_columns = df.select_dtypes(include=['object']).columns

for col in cat_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

Label = LabelEncoder()
for i in cat_columns:
    df[i] = Label.fit_transform(df[i])

x = df.drop(columns= ['Spending Score (1-100)' , 'CustomerID'])
y = df['Spending Score (1-100)']

x_train ,x_test, y_train ,y_test =  train_test_split(x,y, test_size=0.3 , random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

mse = mean_squared_error(y_test , y_predict)
r2 = r2_Score(y_test , y_predict)
f1 = f1_Score(y_test , y_predict)
print("Mean Squared Error:", mse)
print("R-squared Score:", r2)
print("F1 Score:", f1)

