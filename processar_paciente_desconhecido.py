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

# Paciente exemplo (valores baseados na base)
paciente = {
    'age': 50.0,
    'anaemia': 0,
    'creatinine_phosphokinase': 7800,
    'diabetes': 0,
    'ejection_fraction': 38,
    'high_blood_pressure': 1,
    'platelets': 263000.0,
    'serum_creatinine': 1.1,
    'serum_sodium': 136,
    'sex': 1,
    'smoking': 1,
    'time': 10
}

df_paciente = pd.DataFrame([paciente])

df_paciente = df_paciente[colunas_features]

df_paciente_normalizado = normalizador_num.transform(df_paciente)

cluster_predito = clusters.predict(df_paciente_normalizado)[0]

print("\n===== DADOS DO PACIENTE =====")
for k, v in paciente.items():
    print(f"{k}: {v}")

print(f"\n O paciente pertence ao CLUSTER {cluster_predito}\n")

# Carregar e reverter centroides para descrição
df_centroides = pd.DataFrame(clusters.cluster_centers_, columns=colunas_features)
df_centroides_revertidos = normalizador_num.inverse_transform(df_centroides)
df_final = pd.DataFrame(df_centroides_revertidos, columns=colunas_features)

print("===== DESCRIÇÃO DO CLUSTER =====")
print(df_final.loc[cluster_predito].round(2).to_string())