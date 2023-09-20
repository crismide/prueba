import numpy as np
import pandas as pd
import sklearn.cluster as sc
import matplotlib.pyplot as plt

data = pd.read_csv("iris_clusters.csv", delimiter=";") #pandas package

k_means = sc.KMeans(n_clusters=3,n_init=10)
k_means.fit(data)

# Get the cluster labels assigned to each data point
cluster_labels = k_means.labels_

# Count the number of data points in each cluster
unique, counts = np.unique(cluster_labels, return_counts=True)

# Create a dictionary to store the cluster number as keys and the count as values
cluster_counts = dict(zip(unique, counts))

# Print the number of records in each cluster
for cluster, count in cluster_counts.items():
    print(f"Cluster {cluster}: {count} records")

plt.scatter(data["sw"], data["sl"], c=k_means.labels_, cmap='viridis')
plt.show()