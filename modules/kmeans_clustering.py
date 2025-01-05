from sklearn.cluster import KMeans

def apply_kmeans_clustering(points_normalized, k=4):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(points_normalized)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    return labels, centroids,kmeans
