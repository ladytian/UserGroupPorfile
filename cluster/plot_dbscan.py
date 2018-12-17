# -*- coding: utf-8 -*-
__author__ = 'tianjiwei'

import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE


# #############################################################################
# Generate sample data
centers = [[1, 1], [-0.4, -0.6], [1, -1], [1.5, 2.5], [2.5, 0.9], [3, -1.5], [3.5, 4.9], [2.9, 3.3]]
X, labels_true = make_blobs(n_samples=200, centers=centers, cluster_std=0.4, random_state=0)

X = StandardScaler().fit_transform(X)

# #############################################################################
# Compute DBSCAN
db = DBSCAN(eps=0.37, min_samples=13).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)
cluster_0 = list(labels).count(0)
cluster_1 = list(labels).count(1)
cluster_2 = list(labels).count(2)
cluster_3 = list(labels).count(3)
cluster_4 = list(labels).count(4)
cluster_5 = list(labels).count(5)
cluster_6 = list(labels).count(6)

print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of cluster_0: %d' % cluster_0)
print('Estimated number of cluster_1: %d' % cluster_1)
print('Estimated number of cluster_2: %d' % cluster_2)
print('Estimated number of cluster_3: %d' % cluster_3)
print('Estimated number of cluster_4: %d' % cluster_4)
print('Estimated number of cluster_5: %d' % cluster_5)
print('Estimated number of cluster_6: %d' % cluster_6)
print('Estimated number of noise points: %d' % n_noise_)

# print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
# print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
# print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
# print("Adjusted Rand Index: %0.3f"
#       % metrics.adjusted_rand_score(labels_true, labels))
# print("Adjusted Mutual Information: %0.3f"
#       % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels, sample_size=200) )
# print(metrics.silhouette_samples(X, labels) )
# #############################################################################
# Plot result
import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=10)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=5)

plt.title('Number of clusters: %d\nSilhouette Coefficient: 0.723' % n_clusters_)
plt.show()
