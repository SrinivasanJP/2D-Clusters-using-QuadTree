import pandas as pd
import numpy as np

def load_and_normalize_data(file_path):
    data = pd.read_csv(file_path)
    points = data[['Annual Income (k$)', 'Spending Score (1-100)']].values

    # Normalize the data to range [0, 1]
    points_min = points.min(axis=0)
    points_max = points.max(axis=0)
    points_normalized = (points - points_min) / (points_max - points_min)
    
    return points, points_normalized, points_min, points_max
