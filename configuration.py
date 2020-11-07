import attributes as att
import results
import algorithms as clustering
import time
import logging


class Configuration:

    def kmeans(self, x, df):
        for nc in att.NUMBER_CLUSTERS:
            for mi in att.MAX_ITERATIONS:
                for nr in att.NUMBER_INIT:
                    configuration, alg = clustering.kmeans(nc, nr, mi)
                    if results.path_exists(configuration) is False:
                        self.execute_clustering(alg, configuration, df, x)

    def agglomerative(self, x, df):
        for nc in att.NUMBER_CLUSTERS:
            for affinity in att.METRIC:
                for linkage in att.LINKAGE:
                    if linkage != "ward" and affinity != "euclidean":
                        configuration, alg = clustering.agglomerative(nc, affinity, linkage)
                    if results.path_exists(configuration) is False:
                        self.execute_clustering(alg, configuration, df, x)

    def affinity_propagation(self, x, df):
        for mi in att.MAX_ITERATIONS:
            for nr in att.NUMBER_INIT:
                configuration, alg = clustering.affinity_propagation(nr, mi, att.DAMPING)
                if results.path_exists(configuration) is False:
                    self.execute_clustering(alg, configuration, df, x)

    def gaussian_mixture(self, x, df):
        for nc in att.NUMBER_CLUSTERS:
            for mi in att.MAX_ITERATIONS:
                for nr in att.NUMBER_INIT:
                    configuration, alg = clustering.gaussian_mixture(nc, nr, mi)
                    if results.path_exists(configuration) is False:
                        self.execute_clustering(alg, configuration, df, x)

    def spectral(self, x, df):
        for affinity in att.AFFINITY_SPECTRAL:
            for labels in att.ASSIGN_LABELS:
                for n_neighbors in att.NUMBER_NEIGHBORS:
                    for number_init in att.NUMBER_INIT:
                        configuration, alg = clustering.spectral_clustering(affinity, labels, number_init, n_neighbors)
                        if results.path_exists(configuration) is False:
                            self.execute_clustering(alg, configuration, df, x)

    def dbscan(self, x, df):
        for metric in att.METRIC:
            for eps in att.EPS:
                for min_samples in att.MIN_SAMPLES:
                    configuration, alg = clustering.dbscan(metric, eps, min_samples)
                    if results.path_exists(configuration) is False:
                        self.execute_clustering(alg, configuration, df, x)

    def save(self, configuration, alg, y, df, time):
        results.save_clustering_results(df, alg, y, configuration, time)

    def execute_clustering(self, alg, configuration, df, x):
        y, execution_time = self.fit_predict(alg, x, configuration)
        self.save(configuration, alg, y, df, execution_time)

    def fit_predict(self, alg, x, configuration):
        path = "output/" + "/".join(configuration)
        try:
            start_time = time.time()
            logging.info("Running configuration '" + path + "'")
            print("Running configuration " + path + "'")
            y = alg.fit_predict(x)
            logging.info("Execution of configuration '" + path + "'has ended")
            print("Execution of configuration '" + path + "' has ended")
            end_time = time.time()
            total_time = end_time - start_time
        except:
            logging.error('Error running ' + alg)
        return y, total_time

