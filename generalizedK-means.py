import random
import math

data = [
    [1.0, 1.5, 0.8, 1.2],
    [1.2, 1.7, 0.9, 1.1],
    [1.1, 1.4, 0.7, 1.3],
    [1.3, 1.6, 0.85, 1.15],
    [4.0, 4.5, 3.8, 4.2],
    [4.2, 4.7, 3.9, 4.1],
    [4.1, 4.4, 3.7, 4.3],
    [4.3, 4.6, 3.85, 4.15],
    [2.0, 2.2, 1.8, 2.1],
    [2.1, 2.3, 1.9, 2.0],
    [4.5, 4.8, 4.0, 4.4],
    [4.4, 4.9, 3.95, 4.35]
]

def euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def calculate_mean(points):
    if not points:
        return None
    n_features = len(points[0])
    mean_point = []
    for i in range(n_features):
        mean_point.append(sum(point[i] for point in points) / len(points))
    return mean_point

def k_means(data, k, max_iters=100, seed=42):
    random.seed(seed)
    
    centroids = random.sample(data, k)
    
    print(f"K-Means Clustering with k={k}")
    print(f"Dataset: {len(data)} samples, {len(data[0])} features")
    print(f"Initial centroids:")
    for i, centroid in enumerate(centroids):
        print(f"  Centroid {i}: {[f'{x:.3f}' for x in centroid]}")
    
    for iteration in range(max_iters):
        cluster_assignments = []
        
        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            closest_cluster = distances.index(min(distances))
            cluster_assignments.append(closest_cluster)
        
        new_centroids = []
        for j in range(k):
            cluster_points = [data[i] for i in range(len(data)) if cluster_assignments[i] == j]
            if cluster_points:
                new_centroid = calculate_mean(cluster_points)
            else:
                new_centroid = centroids[j]
            new_centroids.append(new_centroid)
        
        converged = True
        for i in range(k):
            for j in range(len(centroids[i])):
                if abs(centroids[i][j] - new_centroids[i][j]) > 1e-6:
                    converged = False
                    break
            if not converged:
                break
        
        if converged:
            print(f"\nConverged at iteration {iteration + 1}")
            break
        
        centroids = new_centroids
        
        if iteration % 10 == 0:
            print(f"Iteration {iteration + 1}: Centroids updated")
    
    return cluster_assignments, centroids

cluster_assignments, centroids = k_means(data, k=3)

print("\nFinal cluster assignments:")
for idx, cluster in enumerate(cluster_assignments):
    print(f"Sample {idx:2d}: Cluster {cluster}")

print("\nFinal centroid positions:")
for i, centroid in enumerate(centroids):
    print(f"Centroid {i}: {[f'{x:.4f}' for x in centroid]}")

wcss = 0
for j in range(3):
    cluster_points = [data[i] for i in range(len(data)) if cluster_assignments[i] == j]
    for point in cluster_points:
        wcss += sum((point[k] - centroids[j][k]) ** 2 for k in range(len(point)))

print(f"\nWithin-Cluster Sum of Squares (WCSS): {wcss:.4f}")

print("\nCluster Details:")
for j in range(3):
    cluster_points = [data[i] for i in range(len(data)) if cluster_assignments[i] == j]
    print(f"Cluster {j}: {len(cluster_points)} points")
    for i in range(len(data)):
        if cluster_assignments[i] == j:
            print(f"  Sample {i}: {[f'{x:.3f}' for x in data[i]]}")

print("\nVisualization (First two features):")
print("Sample | Feature1 | Feature2 | Cluster")
print("-" * 40)
for i in range(len(data)):
    print(f"{i:6d} | {data[i][0]:8.3f} | {data[i][1]:8.3f} | {cluster_assignments[i]:7d}")