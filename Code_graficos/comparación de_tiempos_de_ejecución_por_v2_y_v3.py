import matplotlib.pyplot as plt
import numpy as np
p= [2,4,8,16,32]
t_code_1=[10.8388, 6.2072, 3.3841, 2.0565, 1.4021]
t_code_2=[6.1682, 3.0465, 2.2287, 1.3701, 1.1308]

plt.figure(figsize=(10, 6))
plt.plot(p, t_code_1, marker='o', label='knn_parallel_opt', color='blue')
plt.plot(p, t_code_2, marker='o', label='knn_parallel_end', color='orange')
plt.title('Comparación de Tiempos de Ejecución')
plt.xlabel('Número de Procesos')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.xticks(p)
plt.legend()
plt.grid()
plt.show()
#plt.savefig('grafica_N_4000.png')