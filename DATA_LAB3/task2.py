import numpy as np
import pandas as pd
import sklearn.cluster as sc
import sklearn.preprocessing as sp
import matplotlib.pyplot as plt
import scipy.stats as stats

data = pd.read_csv("iris_clusters.csv", delimiter=";") #pandas package

## PREPROCESSING
data = sp.normalize(data)
z_scores = stats.zscore(data)
threshold = 5  # You can adjust this threshold based on your data and requirements
outlier_indices = (z_scores > threshold).any(axis=1) | (z_scores < -threshold).any(axis=1)
data = data[~outlier_indices]


## CLUSTERING 

k_means = sc.KMeans(n_clusters=3,n_init=10)
k_means.fit(data)

cluster_labels = k_means.labels_
unique, counts = np.unique(cluster_labels, return_counts=True)
cluster_counts = dict(zip(unique, counts))
for cluster, count in cluster_counts.items():
    print(f"Cluster {cluster}: {count} records")