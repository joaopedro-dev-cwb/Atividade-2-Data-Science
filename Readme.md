#  Projeto de Clusterização: Análise de Insuficiência Cardíaca

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
##  Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivos](#objetivos)
- [Dataset](#dataset)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Pipeline de Execução](#pipeline-de-execução)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Resultados](#resultados)
- [Como Usar](#como-usar)
- [Contribuindo](#contribuindo)

---

##  Sobre o Projeto

Este projeto de **Data Science** utiliza técnicas de **aprendizado não supervisionado** para identificar perfis distintos de pacientes com insuficiência cardíaca. Através do algoritmo **K-Means**, agrupamos pacientes com características clínicas semelhantes, possibilitando:

-  Identificação de padrões em dados médicos
-  Descoberta de subgrupos de pacientes com perfis similares
-  Classificação automática de novos pacientes
-  Insights para tomada de decisão clínica

---

##  Objetivos

1.  **Normalizar dados clínicos** para garantir que todas as features tenham a mesma escala
2.  **Determinar o número ótimo de clusters** usando o Método do Cotovelo (Elbow Method)
3.  **Treinar modelo de clusterização** com K-Means
4.  **Descrever características** de cada cluster identificado
5.  **Classificar novos pacientes** em clusters existentes

---

##  Dataset

**Nome:** Heart Failure Clinical Records Dataset  
**Fonte:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+failure+clinical+records)  
**Registros:** 299 pacientes  
**Features:** 12 características clínicas

### Features Utilizadas:

| Feature | Descrição | Tipo |
|---------|-----------|------|
| `age` | Idade do paciente | Numérica |
| `anaemia` | Presença de anemia (0/1) | Binária |
| `creatinine_phosphokinase` | Nível de CPK no sangue (mcg/L) | Numérica |
| `diabetes` | Presença de diabetes (0/1) | Binária |
| `ejection_fraction` | Porcentagem de sangue que sai do coração a cada contração | Numérica |
| `high_blood_pressure` | Presença de hipertensão (0/1) | Binária |
| `platelets` | Contagem de plaquetas (kiloplatelets/mL) | Numérica |
| `serum_creatinine` | Nível de creatinina sérica (mg/dL) | Numérica |
| `serum_sodium` | Nível de sódio sérico (mEq/L) | Numérica |
| `sex` | Sexo do paciente (0=F, 1=M) | Binária |
| `smoking` | Paciente fumante (0/1) | Binária |
| `time` | Período de acompanhamento (dias) | Numérica |

> **Nota:** A coluna `DEATH_EVENT` (target) é removida para análise não supervisionada.

---

##  Tecnologias Utilizadas

- **Python 3.8+**
- **scikit-learn** - Algoritmos de ML e normalização
- **pandas** - Manipulação de dados
- **numpy** - Operações numéricas
- **matplotlib** - Visualização de dados
- **scipy** - Cálculos científicos

---

##  Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/joaopedro-dev-cwb/Atividade-2-Data-Science.git
cd Atividade-2-Data-Science
```

2. **Instale as dependências:**
```bash
pip install scikit-learn pandas numpy matplotlib scipy
```

Ou usando requirements.txt (se disponível):
```bash
pip install -r requirements.txt
```

---

##  Pipeline de Execução

Os scripts devem ser executados **na ordem sequencial** para garantir o funcionamento correto do pipeline:

### 1️. **Normalização dos Dados**
```bash
python normalizar.py
```

**O que faz:**
-  Lê o dataset bruto (`heart_failure_clinical_records_dataset.csv`)
-  Remove a coluna alvo (`DEATH_EVENT`)
-  Aplica normalização **MinMaxScaler** (escala 0-1)
-  Salva o modelo de normalização e dados processados

**Arquivos gerados:**
- `modelo_normalizador_heart.model` - Modelo de normalização para uso futuro
- `dados_preprocessados_heart.csv` - Dados normalizados

---

### 2️. **Clusterização e Determinação do K Ótimo**
```bash
python clusterizar.py
```

**O que faz:**
-  Carrega os dados pré-processados
-  Testa clusters de K=2 até K=50
-  Aplica o **Método do Cotovelo** para encontrar K ótimo
-  Treina o modelo KMeans com o K determinado
-  Salva o modelo treinado e visualização

**Arquivos gerados:**
- `cluster_heart.model` - Modelo KMeans treinado
- `distorcoes_heart.jpg` - Gráfico do Método do Cotovelo

**Saída esperada:**
```
Número ótimo de clustes: 20
```

---

### 3️. **Descrição dos Clusters**
```bash
python descrever_centroides_simplificado.py
```

**O que faz:**
-  Carrega os modelos salvos
-  Reverte a normalização dos centroides
-  Exibe características médias de cada cluster
-  Permite interpretação dos grupos identificados

**Saída:** Tabela com características de todos os 20 clusters

---

### 4️. **Classificação de Novo Paciente**
```bash
python processar_paciente_desconhecido.py
```

**O que faz:**
-  Define dados de um paciente exemplo
-  Normaliza os dados do novo paciente
-  Classifica o paciente em um cluster
-  Exibe o cluster atribuído e suas características

**Saída esperada:**
```
===== DADOS DO PACIENTE =====
age: 50.0
anaemia: 0
...

O paciente pertence ao CLUSTER 17

===== DESCRIÇÃO DO CLUSTER =====
age: 60.0
anaemia: 0.06
...
```

---

##  Estrutura do Projeto

```
Atividade-2-Data-Science/
│
├── 📄 heart_failure_clinical_records_dataset.csv  # Dataset original
│
├──  normalizar.py                               # Script 1: Normalização
├──  clusterizar.py                              # Script 2: Clusterização
├──  descrever_centroides_simplificado.py        # Script 3: Análise clusters
├──  processar_paciente_desconhecido.py          # Script 4: Classificação
│
├──  modelo_normalizador_heart.model             # Modelo de normalização (gerado)
├──  cluster_heart.model                         # Modelo KMeans (gerado)
├──  dados_preprocessados_heart.csv              # Dados normalizados (gerado)
├──  distorcoes_heart.jpg                        # Gráfico do cotovelo (gerado)
│
└──  Readme.md                                   # Documentação
```

---

##  Resultados

### Número Ótimo de Clusters
Através do **Método do Cotovelo**, foi determinado que **K = 20** é o número ótimo de clusters para este dataset, equilibrando:
-  Boa separação entre grupos
-  Interpretabilidade dos clusters
-  Variância explicada

### Insights dos Clusters
Os 20 clusters identificados representam diferentes perfis de pacientes, considerando:
-  Características demográficas (idade, sexo)
-  Condições pré-existentes (diabetes, anemia, hipertensão)
-  Marcadores laboratoriais (creatinina, sódio, plaquetas)
-  Função cardíaca (fração de ejeção)
-  Tempo de acompanhamento

---

##  Como Usar

### Classificar um Novo Paciente

Edite o dicionário em `processar_paciente_desconhecido.py`:

```python
paciente = {
    'age': 50.0,                      # Idade em anos
    'anaemia': 0,                     # 0=Não, 1=Sim
    'creatinine_phosphokinase': 7800, # mcg/L
    'diabetes': 0,                    # 0=Não, 1=Sim
    'ejection_fraction': 38,          # Porcentagem
    'high_blood_pressure': 1,         # 0=Não, 1=Sim
    'platelets': 263000.0,            # kiloplatelets/mL
    'serum_creatinine': 1.1,          # mg/dL
    'serum_sodium': 136,              # mEq/L
    'sex': 1,                         # 0=Feminino, 1=Masculino
    'smoking': 1,                     # 0=Não, 1=Sim
    'time': 10                        # Dias de acompanhamento
}
```

Execute o script:
```bash
python processar_paciente_desconhecido.py
```

---

##  Autor

**João Pedro dos Santos**  
GitHub: [@joaopedro-dev-cwb](https://github.com/joaopedro-dev-cwb)

---

##  Referências

- [Scikit-learn K-Means Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [Heart Failure Dataset - UCI](https://archive.ics.uci.edu/ml/datasets/Heart+failure+clinical+records)
- [Elbow Method for Optimal K](https://en.wikipedia.org/wiki/Elbow_method_(clustering))

