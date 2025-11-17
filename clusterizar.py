from sklearn import preprocessing
from pickle import dump
import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

dados = pd.read_csv('dados_preprocessados_heart.csv', sep = ',')

distorcoes = []
K = range(2, 50)
for i in K:
    cluster_model = KMeans(n_clusters=i, random_state=42, n_init=10).fit(dados)
    distorcoes.append(
        sum(
            np.min(
                cdist(dados,
                      cluster_model.cluster_centers_,
                      'euclidean'), axis=1)/dados.shape[0]
            )
        )

fig, ax = plt.subplots()
ax.plot(K, distorcoes)
ax.set(xlabel='n Clusters', ylabel='Distorcoes')
ax.grid()
plt.savefig('distorcoes_heart.jpg')

x0 = K[0]
y0 = distorcoes[0]
xn = K[-1]
yn = distorcoes[-1]
distancias = []
for i in range(len(distorcoes)):
    x = K[i]
    y = distorcoes[i]
    numerador = abs(
        (yn-y0)*x - (xn-x0)*y + xn*y0 - yn*x0
    )
    denominador = math.sqrt(
        (yn-y0)**2 + (xn-x0)**2
    )
    distancias.append(numerador/denominador)
    
numero_clusters_otimo = K[
                            distancias.index(
                                np.max(distancias)
                                )
                        ]
print('Número ótimo de clustes:', numero_clusters_otimo)

cluster_model_final = KMeans(n_clusters=numero_clusters_otimo, random_state=42, n_init=10).fit(dados)
dump(cluster_model_final, open('cluster_heart.model', 'wb'))