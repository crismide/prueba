import numpy as np
import pandas as pd
import sklearn.cluster as sc
import sklearn.preprocessing as sp
import scipy.stats as stats

data = pd.read_csv("iris_clusters.csv", delimiter=";") #pandas package

z_scores = stats.zscore(data)
threshold = 5  # You can adjust this threshold based on your data and requirements
outlier_indices = (z_scores > threshold).any(axis=1) | (z_scores < -threshold).any(axis=1)
data = data[~outlier_indices]
data = sp.normalize(data)

eps = 100000000000

clustering = sc.DBSCAN(eps=eps, min_samples=5).fit(data)
unique, counts = np.unique(clustering.labels_, return_counts=True)
cluster_counts = dict(zip(unique, counts))
num_cluster=0
for cluster, count in cluster_counts.items():
    num_cluster+=1
print(f"Number of clusters -> {num_cluster}")
        