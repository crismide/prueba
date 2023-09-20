import numpy as np
import pandas as pd
import sklearn.cluster as sc

data = pd.read_csv("iris_clusters.csv", delimiter=";") #pandas package

linkage_method = "complete"

clustering = sc.AgglomerativeClustering(linkage=linkage_method).fit(data)
unique, counts = np.unique(clustering.labels_, return_counts=True)
cluster_counts = dict(zip(unique, counts))

for cluster, count in cluster_counts.items():
    print(f"Cluster {cluster}: {count} records")