import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os


output_dir = "../Graficos"
os.makedirs(output_dir, exist_ok=True)

# Datos experimentales
p = np.array([2, 4, 8, 16, 32])
T_real = np.array([7.7620, 8.5444, 11.6762, 12.0023, 14.8331])


n = 3200
m = 800


def T_teorico(p, a1, a2, a3):
    return a1 * (n * m / p) + a2 * np.log2(p) + a3 * p

# Ajuste de parámetros
param_opt, _ = curve_fit(T_teorico, p, T_real, p0=[0.0001, 1, 0.001])
a1_opt, a2_opt, a3_opt = param_opt
T_fit = T_teorico(p, a1_opt, a2_opt, a3_opt)


plt.figure(figsize=(8, 5))
plt.plot(p, T_real, marker='o', label='Tiempo Real', color='blue')
plt.plot(p, T_fit, marker='s', linestyle='--', label='Teórico (Normalizado)', color='violet')
plt.xlabel("Número de Procesos")
plt.ylabel("Tiempo de Ejecución (s)")
plt.title("Ajuste con Factores Individuales: Tiempo Real vs. Teórico")
plt.grid(True)
plt.legend()
plt.xticks(p)
plt.tight_layout()

filename = os.path.join(output_dir, "tiempo_teórico_vs_real.png")
plt.savefig(filename)

