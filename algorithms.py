from numpy.core.defchararray import lower
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import AffinityPropagation
from sklearn.mixture import GaussianMixture
from sklearn.cluster import SpectralClustering
from sklearn.cluster import DBSCAN


def kmeans(number_clusters, number_init, max_iterations):
    kmeans = KMeans(n_clusters=number_clusters, n_init=number_init, max_iter=max_iterations)
    configuration = [str(lower(kmeans.__class__.__qualname__)), str(kmeans.n_clusters), str(kmeans.n_init)]
    return configuration, kmeans


def agglomerative(number_clusters, affinity, linkage):
    ac = AgglomerativeClustering(n_clusters=number_clusters, affinity=affinity, linkage=linkage)
    configuration = [str(lower(ac.__class__.__qualname__)), str(ac.n_clusters), str(ac.affinity), str(ac.linkage)]
    return configuration, ac


def affinity_propagation(number_init, max_iterations, damping):
    ap = AffinityPropagation(max_iter=max_iterations, convergence_iter=number_init, damping=damping)
    configuration = [str(lower(ap.__class__.__qualname__)), str(ap.convergence_iter)]
    return configuration, ap


def gaussian_mixture(number_clusters, number_init, max_iterations):
    gm = GaussianMixture(n_components=number_clusters, random_state=0, n_init=number_init, max_iter=max_iterations)

    configuration = [str(lower(gm.__class__.__qualname__)), str(gm.n_components), str(gm.n_init)]
    return configuration, gm


def spectral_clustering(affinity, assign_labels, number_init, number_neighbors):
    sc = SpectralClustering(affinity=affinity, assign_labels=assign_labels, n_init=number_init, n_neighbors=number_neighbors)
    configuration = [str(lower(sc.__class__.__qualname__)), str(sc.n_init),  str(sc.affinity), str(sc.assign_labels), str(sc.n_neighbors)]
    return configuration, sc


def dbscan(metric, eps, min_samples):
    dbscan = DBSCAN(metric=metric, eps=eps, min_samples=min_samples)
    configuration = [str(lower(dbscan.__class__.__qualname__)), str(dbscan.metric), str(dbscan.min_samples), str(dbscan.eps)]
    return configuration, dbscan

