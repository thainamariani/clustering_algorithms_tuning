from multiprocessing.pool import Pool
import pandas as pd
from scipy.sparse import csr_matrix
import configuration as conf
import attributes as att
import filter as f
import logging
from itertools import repeat

def call_function(function):
    function(x, df)
    logging.basicConfig(level=logging.INFO, filename="log.txt")
    path = "output/" + "/".join(configuration)
#read file and select columns
df = pd.read_csv(att.PATH)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
df = df[att.COLUMNS]

#check if data is sparse
if att.SPARSE_DATA:
    x = csr_matrix(df)
else:
    x = df.values

#make a list of algorithms
functions = []
for algorithm in att.ALGORITHMS:
    functions.append(getattr(conf.Configuration(), algorithm))

#execute each configuration
with Pool(processes=att.THREADS) as p:
    p.starmap(call_function, zip(functions))