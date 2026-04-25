import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


df = pd.read_csv("students.csv")

print(df.head())

X = df[['GPA', 'study_hours', 'attendance_rate']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []

for k in range(2, 7):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(2,7), wcss, marker='o')
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

plt.figure(figsize=(8,6))

plt.scatter(df['study_hours'], df['GPA'],
            c=df['cluster'], cmap='rainbow')

plt.title("Student Clusters (K-Means)")
plt.xlabel("Study Hours")
plt.ylabel("GPA")
plt.show()

print("\nFinal Students with Clusters:")
print(df[['student_id', 'GPA', 'study_hours', 'attendance_rate', 'cluster']])