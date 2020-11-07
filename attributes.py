PATH = 'input/info_by_classes/number_refactorings_by_class.csv'

#columns to be considered by the algorithm
COLUMNS = ['EM', 'ES', 'MMT', 'MMS', 'PDT', 'PDS', 'PUT', 'PUS', 'IM']

#names to appear optional
COLUMNS_FORMATTED = {'EM': 'Extract Method',
                   'ES':'Extract SuperClass',
                   'MMT':'Move Method - Target',
                   'MMS':'Move Method - Source',
                   'PDT':'Push Down Method - Target',
                   'PDS':'Push Down Method - Source',
                   'PUT':'Pull Up Method - Target',
                   'PUS':'Pull Up Method - Source',
                   'IM':'Inline Method'}
SPARSE_DATA = True
THREADS = 5

#common attributes
NUMBER_CLUSTERS = [2]
ALGORITHMS = ["kmeans", "agglomerative",
              "gaussian_mixture","spectral", "dbscan", "affinity_propagation"]
MAX_ITERATIONS = [100, 200]
NUMBER_INIT = [5, 10]

#agglomerative and DBSCAN attribute
METRIC = ["euclidean","manhattan", "l1", "l2", "cosine"]

#DBSCAN attributes
EPS=[5]
MIN_SAMPLES = [10]
#EPS = [5, 10, 20, 30, 40, 50, 100]
#MIN_SAMPLES = [10, 50, 100, 200, 300, 400, 500, 1000]

#agglomerative attribute
LINKAGE = ["ward", "complete", "average", "single"]

#affinity propagation attribute
DAMPING = 0.5

#spectral clustering attributes
AFFINITY_SPECTRAL = ["nearest_neighbors", "precomputed", "rbf"]
ASSIGN_LABELS = ["kmeans", "discretize"]
NUMBER_NEIGHBORS = [10]
#NUMBER_NEIGHBORS = [2, 5, 7, 10, 20, 30, 40, 50]