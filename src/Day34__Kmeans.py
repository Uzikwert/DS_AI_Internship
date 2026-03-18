
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
# Synthetic data
X = np.random.rand(100, 2)

inertia = []
K_range = range(1, 11)

for k in K_range:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    inertia.append(model.inertia_)

print("K values tested: ", list(K_range))
print("Inertia values: ", [round(i, 2) for i in inertia])
plt.plot(inertia,marker='o')
plt.xlabel('K Value')
plt.ylabel('Inertia')
plt.show()
# Visualization Of K-Means CLustering
#a) Generate data
X, _ = make_blobs(n_samples=300, centers=4, random_state=42)

#b) Fit K-Means
kmeans = KMeans(n_clusters=4, random_state=42)
labels = kmeans.fit_predict(X)
plt.scatter(X[:,0],X[:,1], c=labels,cmap='viridis')

#c) Get Centroids
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X')

plt.title('K-Means Clustering')
plt.show()