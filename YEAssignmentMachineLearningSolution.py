from sklearn import preprocessing
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

data = pd.read_csv('cereal.csv', index_col=0)
# data_scaled =  preprocessing.scale(data)
# data_scaled = pd.Dataframe(data_scaled)

kmeans = KMeans(n_clusters = 4, random_state=0)
clusters = kmeans.fit_predict(data)

print(clusters)
