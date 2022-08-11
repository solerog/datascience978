<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 22 - Unsupervised Learning

## Unsupervised algorithms

- Feature engineering (save time)
- Compress (save space)

It allows to **cluster data**.

## Principal Component Analysis (PCA)

Goal is to lower the dimensions. Finding the **best linear combination** of features.

Cancels all **multicolinearity**.

Like describing a line that defines all our data.
The PC contains information of all the columns.

The information **has to be scaled**.

### Limitations

Can't be used with **manifolds**.

We use PCA to deal with high-dimensional datasets.

- Better visualization of data
- Reduction of the effects of the curse of dimensionality.
- Reduction of fit size.

## Clustering

Find categories of unlabelled data.
Works with epochs.

1. Choose number of clusters `K`.
2. Initialize `K` centroids.
3. Compute mean square distance between data and centroids.
4. Assign each data point to the closest centroid (clustering).
5. Cumpute the mean of each cluster, which becomes a new centroid.

It is better to apply **PCA** before clustering.

### K-Means

#### Intertia

Loss functions of K-Means.
Sum of squared distance between observations and closest centroid.

We choose `K` such that the inertia is minimized.
