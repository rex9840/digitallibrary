import numpy as np


class KMEANS:
    def __init__(self, n_clusters=3, max_iter=100,random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None
        self.inertia = None
        self.random_state = random_state

    def fit(self, df):
        if self.random_state is not None:
            np.random.seed(self.random_state)
        # Initialize centroids randomly
        self.centroids = df[np.random.choice(df.shape[0], self.n_clusters, replace=False)]

        for _ in range(self.max_iter):
            # Assign each data point to the nearest centroid
            labels = self._assign_clusters(df)

            # Update centroids based on the mean of data points in each cluster
            new_centroids = self._update_centroids(df, labels)

            # Check convergence
            if np.all(np.abs(new_centroids - self.centroids)):
                break

            self.centroids = new_centroids

        # Calculate inertia
        self.inertia = self._calculate_inertia(df, labels)

        return labels

    def _assign_clusters(self, df):
        distances = np.sqrt(((df - self.centroids[:, np.newaxis])**2).sum(axis=2)) #np.newaxis -> dimentional conversion of the centroid where each indivisual centroid is the list containing the centroid values
        return np.argmin(distances, axis=0) # minimum value of flattned array along the columns of the given dimentionalality along the columns


    def _update_centroids(self, df, labels):
        new_centroids = np.zeros_like(self.centroids)
        for i in range(self.n_clusters):
            cluster_points = df[labels == i]
            if len(cluster_points) > 0:
                new_centroids[i] = np.mean(cluster_points, axis=0)
            else:
                new_centroids[i] = self.centroids[i]
        return new_centroids

    def _calculate_inertia(self, df, labels):
        inertia = 0
        for i, centroid in enumerate(self.centroids):
            inertia += np.sum((df[labels == i] - centroid) ** 2)
        return inertia
