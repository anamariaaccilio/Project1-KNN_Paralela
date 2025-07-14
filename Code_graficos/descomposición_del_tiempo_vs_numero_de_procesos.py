import numpy as np
import matplotlib.pyplot as plt
import os


output_dir = "../Graficos"
os.makedirs(output_dir, exist_ok=True)

# Datos reales
p = np.array([2, 4, 8, 16, 32])
T_comp = np.array([0.0572, 0.1347, 0.4988, 0.3095, 0.4682]) 
T_comm = np.array([6.1107, 2.9116, 1.7297, 1.0603, 0.6620])

  
T_total = T_comp + T_comm


plt.figure(figsize=(8, 5))
plt.plot(p, T_total, marker='o', label='Tiempo Total', color='green')
plt.plot(p, T_comp, marker='s', label='Tiempo de Cómputo', color='blue')
plt.plot(p, T_comm, marker='^', label='Tiempo de Comunicación', color='orange')


opt_idx = np.argmin(T_total)
plt.axvline(x=p[opt_idx], color='gray', linestyle='--', label=f'p óptimo ≈ {p[opt_idx]}')

plt.xlabel("Número de Procesos")
plt.ylabel("Tiempo (s)")
plt.title("Descomposición del Tiempo vs Número de Procesos")
plt.legend()
plt.grid(True)
plt.xticks(p)
plt.tight_layout()


plt.savefig(os.path.join(output_dir, "tiempo_total_vs_computo_y_comunicacion.png"))
plt.show()
