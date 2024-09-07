# Synthetic Clustering Project

## Project Overview
This project demonstrates the use of clustering algorithms, specifically **K-means** and **HDBSCAN**, on synthetic datasets such as **stretched ellipsoids** and **concatenated half-moons**. These datasets are designed to test the algorithms' ability to handle complex structures, noise, and clusters of varying shapes and densities. The project includes visualizations of the clustering results, comparisons to the ground truth, and evaluation using silhouette scores.

## Datasets
The project works with two synthetic datasets:
- **Stretched Ellipsoids**: A dataset with clusters shaped like ellipsoids, often used to test clustering algorithms on stretched structures.
- **Concatenated Half-Moons**: A non-linear dataset with two interleaving half-moons that challenge traditional clustering methods like K-means.

## Clustering Algorithms
- **K-means**: A centroid-based clustering algorithm that partitions the data into a predefined number of clusters (K).
- **HDBSCAN** (Hierarchical Density-Based Spatial Clustering of Applications with Noise): A density-based clustering algorithm that can handle clusters of varying shapes, densities, and noise, making it more flexible than K-means for complex datasets.
