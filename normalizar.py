from sklearn import preprocessing
from pickle import dump
import pandas as pd

dados = pd.read_csv('heart_failure_clinical_records_dataset.csv')

target_col = 'DEATH_EVENT'
dados = dados.drop(columns=[target_col])

feature_cols = dados.columns.tolist()

normalizador = preprocessing.MinMaxScaler()
modelo_normalizador = normalizador.fit(dados)

dump(modelo_normalizador, open('modelo_normalizador_heart.model', 'wb'))

dados_normalizados = modelo_normalizador.transform(dados)

dados_finais = pd.DataFrame(data=dados_normalizados, columns=feature_cols)

dados_finais.to_csv('dados_preprocessados_heart.csv', index=False)