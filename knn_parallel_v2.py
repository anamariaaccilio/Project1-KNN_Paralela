from sklearn.model_selection import train_test_split
from collections import Counter
from mpi4py import MPI
import pandas as pd
import numpy as np

# ---------- Inicializar MPI ----------
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

tComp = 0
tComm = 0

# ---------- Funciones ----------
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def knn_predict(test_point, X_train, y_train, k):
    distances = [euclidean_distance(test_point, x) for x in X_train]
    k_indices = np.argsort(distances)[:k]
    k_labels = [y_train[i] for i in k_indices]
    most_common = Counter(k_labels).most_common(1)
    return most_common[0][0]

# ---------- Proceso 0 carga los datos ----------
if rank == 0:
    N = 2000  # Tamaño del conjunto de datos
    train_df = pd.read_csv("data/train.csv")
    train_df = train_df.head(N)

    y = train_df.iloc[:, 0].values
    X = train_df.iloc[:, 1:].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    k = 3
    start_time = MPI.Wtime()

else:
    X_train = None
    y_train = None
    X_test = None
    y_test = None
    k = None

# ---------- Difundir conjunto de entrenamiento y parámetro ----------
tComm0 = MPI.Wtime()
X_train = comm.bcast(X_train if rank == 0 else None, root=0)
y_train = comm.bcast(y_train if rank == 0 else None, root=0)
k = comm.bcast(k, root=0)

# ---------- Repartir test entre procesos ----------
X_test_local = comm.scatter(np.array_split(X_test, size) if rank == 0 else None, root=0)
y_test_local = comm.scatter(np.array_split(y_test, size) if rank == 0 else None, root=0)
tCommF = MPI.Wtime()
tComm += tCommF - tComm0

# ---------- Predicción local ----------
tComp0 = MPI.Wtime()
y_pred_local = [knn_predict(x, X_train, y_train, k) for x in X_test_local]
tCompF = MPI.Wtime()
tComp += tCompF - tComp0

# ---------- Reunir resultados ----------
tComm0 = MPI.Wtime()
y_pred_all = comm.gather(y_pred_local, root=0)
y_test_all = comm.gather(y_test_local, root=0)
tCommF = MPI.Wtime()
tComm += tCommF - tComm0

# ---------- Evaluación final ----------
if rank == 0:
    tComp0 = MPI.Wtime()
    y_pred = [item for sublist in y_pred_all for item in sublist]
    y_test = [item for sublist in y_test_all for item in sublist]
    tCompF = MPI.Wtime()
    tComp += tCompF - tComp0
    accuracy = np.mean(np.array(y_pred) == np.array(y_test))
    end_time = MPI.Wtime()

    print("\n--- Results (Test Data Distributed Strategy) ---")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Execution time: {end_time - start_time:.4f} sec")
    print(f"Computation time: {tComp:.4f} sec")
    print(f"Communication time: {tComm:.4f} sec")
    print(f"Training samples: {len(X_train)}")
    print(f"Test samples: {len(X_test)}")
