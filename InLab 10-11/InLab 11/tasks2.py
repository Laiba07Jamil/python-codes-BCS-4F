import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan',
                     'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)

df['vehicle_type'] = df['vehicle_type'].map({
    'SUV': 0,
    'Sedan': 1,
    'Truck': 2,
    'Hatchback': 3
})

X = df.drop('vehicle_serial_no', axis=1)

kmeans1 = KMeans(n_clusters=3, random_state=42)
labels1 = kmeans1.fit_predict(X)

X_scaled = X.copy()

scaler = StandardScaler()

cols_to_scale = ['mileage', 'fuel_efficiency', 'maintenance_cost']

X_scaled[cols_to_scale] = scaler.fit_transform(X_scaled[cols_to_scale])

kmeans2 = KMeans(n_clusters=3, random_state=42)
labels2 = kmeans2.fit_predict(X_scaled)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.scatter(X['mileage'], X['maintenance_cost'], c=labels1, cmap='rainbow')
plt.title("Without Scaling")
plt.xlabel("Mileage")
plt.ylabel("Maintenance Cost")

plt.subplot(1,2,2)
plt.scatter(X_scaled['mileage'], X_scaled['maintenance_cost'], c=labels2, cmap='rainbow')
plt.title("With Scaling")
plt.xlabel("Scaled Mileage")
plt.ylabel("Scaled Maintenance Cost")

plt.show()

print("\nWithout Scaling Centroids:\n", kmeans1.cluster_centers_)
print("\nWith Scaling Centroids:\n", kmeans2.cluster_centers_)