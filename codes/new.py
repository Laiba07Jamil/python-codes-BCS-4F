import numpy as py
import pandas as pd
from sklearn.preprocessing import LabelEncoder , StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from matplotlib.pyplot import plot

df = pd.read_csv("Mall_Customers.csv")

print("First 5 rows of data set: " , df.head())
print("Shape of data set: " , df.shape)
print("Summary statistics: ",df.describe())
print("Data types: ",df.dtypes)


print("Missing values: ", df.isnull().sum())
cat_col = df.select_dtypes(include = ['object']).columns()
num_cols = df.select_dtypes(include = ['int64' , 'float64']).columns()

for col in cat_col:
    df[col].fillna(df[col].mode()[0] , inplace = True)

for col in num_cols:
    df[col].fillna(df[col].mean() , inplace = True)

df = df.dropna(subset=["CustomerID"]) #drop rows with null values
print("Missing values: ", df.isnull().sum())

df.drop(df[df["Quantity"] <= 0].index , inplace = True)
df.drop(df[df["UnitPrice"] <= 0].index , inplace = True)

df["Invoice"] = pd.to_datetime(df["Invoice"])
df["month"] = df["Invoice"].dt.month
df["Weeks"] = df["Invoice"].dt.weekday
df["Hours"] = df["Invoice"].dt.hour

df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

top_countries = df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False)

for cols in ["Quantity" , "UnitPrice"]:
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    before = df.shape[0]
    df = df[[df[cols] >= lower] , df[cols] <= upper]
    after = df.shape[0]

label = LabelEncoder()
for col in cat_col:
    df[col] = label.fit_transform(df[col])

x = df.groupby("CustomerID").agg(
    TotalSpend = ("TotalPrice" , "sum"),
    Totalquantity = ("Quantity" , "sum"),
    Frequncy = ("Invoice" , "nuniqu")
).reset_index()

x_train , x_test , y_train , y_test = train_test_split(x,test_size = 0.2,random_state = 42)
