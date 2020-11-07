from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import pandas as pd
from scipy.sparse import csr_matrix
import configuration as conf
import attributes as att
import filter as f

df = pd.read_csv(att.FILE)
df = df[att.COLUMNS]
df = f.filter(df, att.MAX_POINTS[0])

#convert
#if att.SPARSE_DATA:
#    X = csr_matrix(df)
#else:
X = df.values
    
model = KMeans()
visualizer = KElbowVisualizer(
        model, k=(2,15), metric='calinski_harabasz', timings=False)
visualizer.fit(X)
visualizer.show()