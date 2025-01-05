import matplotlib.pyplot as plt

def draw_quadtree_and_clusters(ax, points_normalized, labels, centroids, k=4):
    colors = ['red', 'blue', 'green', 'orange']
    for label in range(k):
        cluster_points = points_normalized[labels == label]
        ax.scatter(cluster_points[:, 0], cluster_points[:, 1], s=10, color=colors[label], label=f'Cluster {label}')
        ax.scatter(*centroids[label], color=colors[label], edgecolor='black', s=100, marker='X')  # Centroids
    ax.legend()

def predict_and_update(ax, new_point, points_min, points_max, kmeans, colors):
    # Normalize the input point
    new_point_normalized = (new_point - points_min) / (points_max - points_min)
    prediction = kmeans.predict([new_point_normalized])[0]
    ax.scatter(*new_point_normalized, color=colors[prediction], edgecolor='black', s=150, marker='o', label=f'New Point')
    plt.draw()
    plt.pause(0.1)
