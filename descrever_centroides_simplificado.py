from pickle import load
import pandas as pd
import numpy as np

clusters = load(open('cluster_heart.model', 'rb'))
normalizador_num = load(open('modelo_normalizador_heart.model', 'rb'))

colunas_features = [
    'age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
    'ejection_fraction', 'high_blood_pressure', 'platelets',
    'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time'
]

df = pd.DataFrame(clusters.cluster_centers_, columns=colunas_features)

df[colunas_features] = normalizador_num.inverse_transform(df[colunas_features])

pd.set_option('display.max_columns', None)
print("\n===== CENTROIDES (reconstruídos) =====\n")
print(df.round(3))

print("\n===== DESCRIÇÃO LEGÍVEL POR CLUSTER =====\n")
for i, linha in df.iterrows():
    print(f"--- Cluster {i} ---")
    print({k: round(linha[k], 2) for k in colunas_features})
    print()