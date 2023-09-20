# Plot k-distances
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import sklearn.preprocessing as sp
import scipy.stats as stats

def k_distances(X, n):
    if type(X) is pd.DataFrame:
        X = X.values
    k = 0
    if n is None:
        k = X.shape[1] + 2
        print(f"The k used is {k}")
    else:
        k = n + 1
    dist_func = lambda x, y: math.sqrt(np.sum(np.power(x - y, np.repeat(2, x.size))))
    Distances = pd.DataFrame({
        "i": [i // 10 for i in range(0, len(X) * len(X))],
        "j": [i % 10 for i in range(0, len(X) * len(X))],
        "d": [dist_func(x, y) for x in X for y in X]
    })
    
    # Iterate through groups and calculate k-distances
    k_distances_list = []
    for group_name, group_data in Distances.groupby(by="i"):        
        # Check if k is within bounds for this group
        if k < len(group_data):
            k_distances_group = group_data["d"].iloc[k]
            k_distances_list.append(k_distances_group)
    
    return np.sort(k_distances_list)

data = pd.read_csv("iris_clusters.csv", delimiter=";") #pandas package
z_scores = stats.zscore(data)
threshold = 5  # You can adjust this threshold based on your data and requirements
outlier_indices = (z_scores > threshold).any(axis=1) | (z_scores < -threshold).any(axis=1)
data = data[~outlier_indices]
data = sp.normalize(data)

d = k_distances(
    data, None
)

plt.plot(d)
plt.ylabel("k-distances")
plt.grid(True)
plt.show()