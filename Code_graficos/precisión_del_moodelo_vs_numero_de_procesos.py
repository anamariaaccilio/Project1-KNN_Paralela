import matplotlib.pyplot as plt
import os


ruta_salida = "../Graficos"
os.makedirs(ruta_salida, exist_ok=True)

# Parametros del experimento
k = 3
N = 4000
test_size = 20


procesos = [2, 4, 8, 16, 32]
accuracy = [0.9387, 0.9387, 0.9387, 0.9387, 0.9387] 


plt.figure(figsize=(8, 5))
plt.plot(procesos, accuracy, marker='o', linestyle='-', color='red', label='Accuracy')


info_experimento = f"k = {k}, N = {N}, test_size = {test_size}%"
plt.plot([], [], ' ', label=info_experimento)  

plt.xlabel("Número de Procesos")
plt.ylabel("Accuracy")
plt.title("Precisión del Modelo vs Número de Procesos")
plt.grid(True)
plt.xticks(procesos)
plt.ylim(0.93, 0.94)
plt.legend(["Accuracy", info_experimento], loc='best')


plt.savefig(os.path.join(ruta_salida, "accuracy_vs_procesos_k3_N4000.png"))
plt.close()

