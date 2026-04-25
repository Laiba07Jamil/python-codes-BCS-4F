import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Mall_Customers.csv")

print(df.head())

df = df.drop("CustomerID", axis=1)

df["Genre"] = df["Genre"].map({"Male": 0, "Female": 1})
X = df.values

kmeans1 = KMeans(n_clusters=5, init='k-means++', random_state=42)
labels1 = kmeans1.fit_predict(X)

df_scaled = df.copy()

scaler = StandardScaler()

cols_to_scale = ["Annual Income (k$)", "Spending Score (1-100)"]
df_scaled[cols_to_scale] = scaler.fit_transform(df_scaled[cols_to_scale])

X_scaled = df_scaled.values

kmeans2 = KMeans(n_clusters=5, init='k-means++', random_state=42)
labels2 = kmeans2.fit_predict(X_scaled)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.scatter(X[:, 2], X[:, 3], c=labels1, cmap='rainbow')
plt.title("Without Scaling")

plt.subplot(1,2,2)
plt.scatter(X_scaled[:, 2], X_scaled[:, 3], c=labels2, cmap='rainbow')
plt.title("With Scaling")

plt.show()

print("\nCentroids (Without Scaling):")
print(kmeans1.cluster_centers_)

print("\nCentroids (With Scaling):")
print(kmeans2.cluster_centers_)