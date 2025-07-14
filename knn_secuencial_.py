import pandas as pd
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
import time
import matplotlib.pyplot as plt

N = 4000  # Tamaño del conjunto de datos

# -----------------------------
# Cargar y preparar los datos
# -----------------------------
train_df = pd.read_csv("data/train.csv")
# train_df = pd.read_csv("C:/Users/HP/Desktop/UTEC/Ciclo_IX/CParalela/proyecto/data/train.csv")

# -----------------------------
# Definición del modelo KNN
# -----------------------------
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def knn_predict(test_point, X_train, y_train, k):
    # Calcula la distancia del punto de prueba (test_point) a todos los puntos de entrenamiento (X_train).
    distances = [euclidean_distance(test_point, x) for x in X_train]

    # Ordena los índices según menor distancia.
    k_indices = np.argsort(distances)[:k]

    # Selecciona las k etiquetas más cercanas (k_labels).
    k_labels = [y_train[i] for i in k_indices]
  
    # Usa Counter para contar las clases más comunes entre esos k
    most_common = Counter(k_labels).most_common(1)
    return most_common[0][0] # Devuelve la clase más frecuente como predicción.

# train_df = pd.read_csv("C:/Users/HP/Desktop/UTEC/Ciclo_IX/CParalela/proyecto/data/train.csv")
train_df = train_df.head(N)

y = train_df.iloc[:, 0].values
X = train_df.iloc[:, 1:].values

# División en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Ejecutar predicción
# -----------------------------
k = 3
start_time = time.time()
y_pred = [knn_predict(x, X_train, y_train, k) for x in X_test]
accuracy = np.mean(y_pred == y_test)
end_time = time.time()

print(f"Accuracy: {accuracy:.4f}")
print(f"Execution time (sequential): {end_time - start_time:.4f} sec")