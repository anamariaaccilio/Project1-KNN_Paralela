import matplotlib.pyplot as plt
import numpy as np
p= [2,4,8,16,32]
t_comm=[0.0458, 0.9364, 0.8239, 0.6993, 0.5415]
t_comp=[10.1928, 5.2706, 2.5600, 1.3570, 0.8602]

plt.figure(figsize=(10, 6))
plt.plot(p, t_comp, marker='o', label='tiempo computacion', color='blue')
plt.plot(p, t_comm, marker='o', label='tiempo comunicacion', color='orange')
plt.title('Tiempo de Computación vs Tiempo de Comunicación del KNN Paralelo 1')
plt.xlabel('Número de Procesos')
plt.ylabel('Tiempo (segundos)')
plt.xticks(p)
plt.yticks(np.arange(1, 12, 1))  # Mostrar de 1 a 11 en eje Y
plt.legend()
plt.grid()
plt.show()
#plt.savefig('grafica_time_comp_comm_code1.png')