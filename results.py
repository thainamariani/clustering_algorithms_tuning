import matplotlib.pyplot as plt
import seaborn as sns
import attributes as att
import os
import sklearn.metrics as measures
import numpy as np
import logging


def path_exists(configuration):
    path = "output/" + "/".join(configuration)
    try:
        os.makedirs(path)
    except IOError:
        logging.info("Configuration " + path + " already exists.")
        print("Configuration " + path + " already exists.")
        return True
    return False

def save_clustering_results(df, alg, y, configuration, time):
    path = "output/" + "/".join(configuration)
    create_info_file(alg, df, path, time, y)
    create_label_file(path, y)


def create_label_file(path, y):
    f = open(path + "/" + "labels.txt", "w")
    write_label_information(f, y)
    f.close()


def create_info_file(alg, df, path, time, y):
    f = open(path + "/" + "info.txt", "w")
    write_time_information(f, time)
    write_cluster_information(alg, f, y)
    write_centroids_information(alg, f)
    write_metrics_information(df, f, y)
    write_params_information(alg, f)
    f.close()


def write_label_information(f, y):
    j=0
    for i in y:
        j = j + 1
        f.write(str(i) + "\n")


def write_time_information(f, time):
    f.write("Time: " + str(time) + "\n\n")


def write_params_information(alg, f):
    f.write("\n\n" + str(alg.get_params()))


def write_metrics_information(df, f, y):
    f.write("\nMetrics:\n")
    f.write("Davies Bouldin Score: " + str(measures.davies_bouldin_score(df, y)))
    f.write("\nSilhouette Coefficient: " + str(measures.silhouette_score(df, y)))
    #f.write("\nCalinski-Harabasz Index: " + str(measures.calinski_harabaz_score(df, y)))


def write_centroids_information(alg, f):
    if "cluster_centers_" in dir(alg):
        f.write("\nCentroids:\n")
        cluster = -1
        for i in alg.cluster_centers_:
            cluster = cluster + 1
            f.write("Cluster " + str(cluster) + ": " + str(i) + "\n")


def write_cluster_information(alg, f, y):
    if "n_clusters" in dir(alg):
        number_clusters = alg.n_clusters
    elif "n_components" in dir(alg):
        number_clusters = alg.n_components
    elif "core_sample_indices_" in dir(alg):
        number_clusters = len(alg.core_sample_indices_)
    else:
        number_clusters = len(alg.cluster_centers_indices_)
    f.write("Number of clusters: " + str(number_clusters) + "\n")
    for i in range(number_clusters):
        f.write("Cluster " + str(i) + ": " + str(np.count_nonzero(y == i)) + " instances \n")

