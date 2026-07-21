import numpy as num
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Mall_Customers.csv")
df.head()
x = df.iloc[: , [3,4]].values
print(df.columns)

print(df.isnull().sum())  #check  for null values in the dataset

df["Genre"].fillna(df['Genre'].mode()[0] , inplace = True) #fill null vales for words data
df["Age"].fillna(df["Age"].mean() , inplace= True) #fill null values for numeric data

label = LabelEncoder()
df["Genre"] = label.fit_transform(df["Genre"]) # convert words to numeric data using LabelEncoder
df["Genre"] = df["Genre"].map({"Male" : 1 , "Female" : 0}) #convert words to numeric data using mapping

wcss_list = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i , init = 'k-means++' , random_state = 42)
    kmeans.fit(x)
    wcss_list.append(kmeans.inertia_)

plt.plot(range(1,11),wcss_list)
plt.title("The Elbow Method")
plt.xlabel("Number of clusters")
plt.ylabel("WCSS")
plt.show()

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

kmeans = KMeans(n_clusters=3,init='k-means++',random_state=42)
y_predict = kmeans.fit_predict(x_scaled)

plt.scatter(x_scaled[y_predict == 0 , 0] , x_scaled[y_predict == 0, 1] , s = 100 , c ='blue' , label = 'Cluster 1')
plt.scatter(x_scaled[y_predict == 1 , 0] , x_scaled[y_predict == 1, 1] , s = 100 , c ='green' , label = 'Cluster 2')
plt.scatter(x_scaled[y_predict == 2 , 0] , x_scaled[y_predict == 2, 1] , s = 100 , c ='red' , label = 'Cluster 3')
plt.scatter(x_scaled[y_predict == 3 , 0] , x_scaled[y_predict == 3, 1] , s = 100 , c ='black' , label = 'Cluster 4')
plt.scatter(kmeans.cluster_centers_[: , 0] , kmeans.cluster_centers_[: , 1] , s = 300 , c = 'yellow' , label = ' Centroids')

plt.title("Customers of Mall")
plt.xlabel("Annunal income")
plt.ylabel("Spending score")
plt.show()

plt.bar(df["Age"] , df["CustomerID"])
plt.title("Bar chart")
plt.xlabel("Ages")
plt.ylabel("CustomerID")
plt.show()

plt.pie(df["Age"].head(5) , labels=df["CustomerID"].head(5) , autopct="%1.1f%%")
plt.title("Pie chart")
plt.show()

import numpy as np

x = np.arange(4)

sales1 = [10,20,15,25]
sales2 = [12,18,10,22]

plt.bar(x-0.2, sales1, width=0.4, color='blue', label='2024')
plt.bar(x+0.2, sales2, width=0.4, color='green', label='2025')

plt.xticks(x, ['A','B','C','D'])
plt.legend()
plt.show()

plt.hist(df["Age"])
plt.title("Histogram")
plt.show()

plt.boxplot(df["Age"])
plt.show()