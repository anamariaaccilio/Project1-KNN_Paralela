# from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from mpi4py import MPI
import numpy as np
from collections import Counter
import time
import pandas as pd

# ----- Función para vecinos locales -----
def compute_local_neighbors(X_test, X_train_local, y_train_local, k):
    local_neighbors = []
    for test_point in X_test:
        dists = [np.linalg.norm(test_point - x) for x in X_train_local] # calculo de distancias euclidianas
        idx = np.argsort(dists)[:k] # obtengo los indices de los k vecinos más cercanos
        neighbors = [(dists[i], y_train_local[i]) for i in idx] # creo una lista de tuplas (distancia, etiqueta)
        local_neighbors.append(neighbors) # añado los vecinos locales a la lista  
    return local_neighbors

# ----- Inicialización MPI -----
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# ----- Carga de datos solo en el proceso 0 -----
if rank == 0:
    # digits = load_digits()
    # X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
    N = 16000  # Tamaño del conjunto de datos
    train_df = pd.read_csv("data/train.csv")
    train_df = train_df.head(N)

    y = train_df.iloc[:, 0].values
    X = train_df.iloc[:, 1:].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    k = 3
    start_time = time.time()
    print(X_test.shape)
else:
    X_train = None
    y_train = None
    X_test = None
    y_test = None
    k = None

# ----- Broadcast X_test, y_test, k ----- es decir, se envían a todos los procesos
X_test = comm.bcast(X_test if rank == 0 else None, root=0)
y_test = comm.bcast(y_test if rank == 0 else None, root=0)
k = comm.bcast(k, root=0)

# ----- Scatter X_train, y_train ----- es decir se divide el train
X_train_local = comm.scatter(np.array_split(X_train, size) if rank == 0 else None, root=0)
y_train_local = comm.scatter(np.array_split(y_train, size) if rank == 0 else None, root=0)

# ----- Cada proceso calcula sus vecinos más cercanos locales -----
local_neighbors = compute_local_neighbors(X_test, X_train_local, y_train_local, k)

# ----- Enviar vecinos locales al proceso 0 -----
all_neighbors = comm.gather(local_neighbors, root=0)

'''
all_neighbors= [ [(0.5, 1), (0.8, 0), (1.2, 1)], proceso 0
                 [(0.3, 2), (0.9, 1), (1.0, 2)]] proceso 1
combined = [(0.5, 1), (0.8, 0), (1.2, 1),(0.3, 2), (0.9, 1), (1.0, 2) ]
'''
# ----- Proceso 0 aplica mayoría -----
if rank == 0:
    final_predictions = []

    for i in range(len(X_test)):
        # Reunir todos los vecinos de todos los procesos para este punto
        combined = []
        for proc_neighbors in all_neighbors:
            combined.extend(proc_neighbors[i])
        # Ordenar por distancia --> x[0] tiene la distancia y x[1] tiene la etiqueta
        combined.sort(key=lambda x: x[0])
        # Tomar los k más cercanos globales
        k_labels = [label for (_, label) in combined[:k]] 
        # Votar
        vote = Counter(k_labels).most_common(1)[0][0]
        final_predictions.append(vote)

    # Evaluar
    accuracy = np.mean(np.array(final_predictions) == np.array(y_test))
    end_time = time.time()

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Execution time (DAG-based KNN, {size} processes): {end_time - start_time:.4f} sec")
