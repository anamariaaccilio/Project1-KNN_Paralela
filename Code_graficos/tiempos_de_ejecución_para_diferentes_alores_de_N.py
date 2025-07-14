import matplotlib.pyplot as plt
import numpy as np
p= [2,4,8,16,32]

t_N_2000=[1.4485, 0.9934, 0.6422, 0.5857, 0.5871]
t_N_4000=[6.1682, 3.0465, 2.2287, 1.3701, 1.1308]
t_N_8000=[25.6961, 12.0100, 8.0772, 4.8119, 3.2655]
t_N_16000=[97.3506, 51.1366, 28.1262, 20.3178, 11.3774]
t_N_24000=[236.7852, 112.3368, 72.3130, 38.8428, 30.0642]

plt.figure(figsize=(10, 6))
plt.plot(p, t_N_2000, marker='o', label='N=2000', color='blue')
plt.plot(p, t_N_4000, marker='o', label='N=4000', color='orange')
plt.plot(p, t_N_8000, marker='o', label='N=8000', color='green')
plt.plot(p, t_N_16000, marker='o', label='N=16000', color='red')
plt.plot(p, t_N_24000, marker='o', label='N=24000', color='purple')
plt.title('Comparación de Tiempos de Ejecución para Diferentes Valores de N')
plt.xlabel('Número de Procesos')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.xticks(p)
plt.legend()
plt.grid()
plt.show()
#plt.savefig('grafica_time_comp_comm_code2.png')