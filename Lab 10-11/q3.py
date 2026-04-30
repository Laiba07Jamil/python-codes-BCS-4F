import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("marketing_campaign.csv", sep='\t')

print(df.head())
print(df.shape)

features = [
    'Income',
    'MntWines',
    'MntFruits',
    'MntMeatProducts',
    'MntFishProducts',
    'MntSweetProducts',
    'MntGoldProds'
]

df = df[features]

df = df.fillna(df.median())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

inertia = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure()
plt.plot(range(2, 11), inertia, marker='o')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

df['Cluster'] = clusters

plt.figure()
plt.scatter(df['Income'], df['MntWines'], c=df['Cluster'])
plt.xlabel("Income")
plt.ylabel("Wine Spending")
plt.title("Customer Segmentation")
plt.show()

print(df.head())
print("\nCluster Counts:\n", df['Cluster'].value_counts())