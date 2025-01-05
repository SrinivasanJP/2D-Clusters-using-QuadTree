import matplotlib.pyplot as plt
from modules.data_preprocessing import load_and_normalize_data
from modules.kmeans_clustering import apply_kmeans_clustering
from modules.quadtree import Quadtree
from modules.visualization import draw_quadtree_and_clusters, predict_and_update
import warnings
warnings.filterwarnings("ignore")
import numpy as np

# Load and normalize data
data_file = './data/Mall_Customers.csv'  # Replace with the correct path
points, points_normalized, points_min, points_max = load_and_normalize_data(data_file)

# Apply KMeans clustering
k = 4  # Number of clusters
labels, centroids, kmeans = apply_kmeans_clustering(points_normalized, k)

# Create the quadtree
quadtree = Quadtree([0, 0, 1, 1], max_depth=4)
for point in points_normalized:
    quadtree.insert(point)

# Initialize the figure
fig, ax = plt.subplots(figsize=(8, 8))
plt.ion()  # Turn on interactive mode

# Draw quadtree grid
quadtree.draw(ax)

# Draw clusters and centroids
draw_quadtree_and_clusters(ax, points_normalized, labels, centroids, k)

# Dynamic plotting function for new points
colors = ['red', 'blue', 'green', 'orange']
print("Enter new points for prediction (comma-separated, e.g., '50,50'). Type 'exit' to quit.")
while True:
    try:
        user_input = input("Predict cluster [Annual Income, Spending Score]: ").strip()
        if user_input.lower() == 'exit':
            break
        new_point = np.array(list(map(float, user_input.split(','))))
        if len(new_point) != 2:
            print("Please enter exactly two values (x, y).")
            continue
        predict_and_update(ax, new_point, points_min, points_max, kmeans, colors)
    except Exception as e:
        print(f"Error: {e}. Please try again.")

plt.ioff()  # Turn off interactive mode
plt.show()
