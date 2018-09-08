from sklearn.metrics import pairwise_distances_argmin

def find_clusters(X, n_cluters, rseed = 2):
    rng = np.random.RadomState(rseed)
    i = rng.permutation(X.shape[0])[:n_cluters]
    centers = X[i]

    while True:
        # 2a. Assign labels based on closest center
        labels = pairwise_distances_argmin(X,centers)

        # 2b. Find new centers from means of points
        new_centers = np.array([X[labels==i].mean(0) for i in range(n_clusters)])

        # 2c. Check for convergence
