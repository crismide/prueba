import pandas as pd
import sklearn.cluster as sc
import sklearn.metrics as sm

data = pd.read_csv("iris_clusters.csv", delimiter=";") #pandas package

for n_clusters in range(2,11):
    print(f"Clustering with n_clusters = {n_clusters}")
    k_means = sc.KMeans(n_clusters=n_clusters,n_init=10)
    k_means.fit(data)
    cluster_labels = k_means.labels_

    cluster_data = data[['pl', 'pw', 'sl', 'sw']]
    davies_index = sm.davies_bouldin_score(cluster_data,cluster_labels)

    print(f"The Davies Bouldin score is {davies_index}")