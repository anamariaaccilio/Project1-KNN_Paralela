import matplotlib.pyplot as plt
import numpy as np
p= [2,4,8,16,32]
t_comm=[0.0572, 0.1347, 0.4988, 0.3095, 0.4682]
t_comp=[6.1107, 2.9116, 1.7297, 1.0603, 0.6620]

plt.figure(figsize=(10, 6))
plt.plot(p, t_comp, marker='o', label='tiempo computacion', color='blue')
plt.plot(p, t_comm, marker='o', label='tiempo comunicacion', color='orange')
plt.title('Tiempo de Computación vs Tiempo de Comunicación del KNN Paralelo 2')
plt.xlabel('Número de Procesos')
plt.ylabel('Tiempo (segundos)')
plt.xticks(p)
plt.yticks(np.arange(1, 12, 1))  # Mostrar de 1 a 11 en eje Y
plt.legend()
plt.grid()
plt.show()
#plt.savefig('grafica_time_comp_comm_code2.png')