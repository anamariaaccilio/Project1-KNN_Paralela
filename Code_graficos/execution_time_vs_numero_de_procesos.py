import matplotlib.pyplot as plt
import os


output_dir = "../Graficos"
os.makedirs(output_dir, exist_ok=True)


procesos = [2, 4, 8, 16, 32]
tiempos = [7.7620, 8.5444, 11.6762, 12.0023, 14.8331]


info_experimento = "k = 3, N = 4000, test_size = 20%"

plt.figure(figsize=(8,5))
plt.plot(procesos, tiempos, marker='o', linestyle='-', color='blue', label='Tiempo de ejecución')
plt.xlabel("Número de Procesos")
plt.ylabel("Tiempo de Ejecución (segundos)")
plt.title("Tiempo de Ejecución vs Número de Procesos")
plt.grid(True)
plt.xticks(procesos)

plt.legend([f"Tiempo de ejecución\n{info_experimento}"], loc='upper left')

plt.tight_layout()


plt.savefig(f"{output_dir}/execution_time_vs_procesos_k3_N4000.png")
plt.show()

