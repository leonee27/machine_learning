## This code uses library

import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

from sklearn.metrics import pairwise_distances_argmin

from sklearn.datasets.samples_generator import make_blobs

X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
plt.scatter(X[:, 0], X[:, 1])
#plt.show(block=False)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)


plt.scatter(X[:, 0], X[:, 1],c=y_kmeans)

centers = kmeans.cluster_centers_
plt.scatter(centers[:,0], centers[:,1],c='black')
plt.show()

print(y_kmeans)

print(['a', 'b', 'c'] + [1, 2, 3])