import matplotlib.pyplot as plt
import numpy as np
p= [2,4,8,16,24]

t_N_2000=[1.4485, 0.9934, 0.6422, 0.5857, 0.5871]
t_N_4000=[6.1682, 3.0465, 2.2287, 1.3701, 1.1308]
t_N_8000=[25.6961, 12.0100, 8.0772, 4.8119, 3.2655]
t_N_16000=[97.3506, 51.1366, 28.1262, 20.3178, 11.3774]
t_N_24000=[236.7852, 112.3368, 72.3130, 38.8428, 30.0642]

ts_N_2000 = 2.7169 #4.7113
ts_N_4000 = 11.0412 #19.1000
ts_N_8000 = 43.545 #75.3277
ts_N_16000 = 176.1509 #304.7207
ts_N_24000 = 392.956 #679.7685



speedup_N_2000 = [ts_N_2000 / t for t in t_N_2000]
speedup_N_4000 = [ts_N_4000 / t for t in t_N_4000]
speedup_N_8000 = [ts_N_8000 / t for t in t_N_8000]
speedup_N_16000 = [ts_N_16000 / t for t in t_N_16000]
speedup_N_24000 = [ts_N_24000 / t for t in t_N_24000]

# Calcular eficiencia para cada dataset
efficiency_N_2000 = [speedup_N_2000[i] / p[i] for i in range(len(p))]
efficiency_N_4000 = [speedup_N_4000[i] / p[i] for i in range(len(p))]
efficiency_N_8000 = [speedup_N_8000[i] / p[i] for i in range(len(p))]
efficiency_N_16000 = [speedup_N_16000[i] / p[i] for i in range(len(p))]
efficiency_N_24000 = [speedup_N_24000[i] / p[i] for i in range(len(p))]

plt.figure(figsize=(10, 6))
plt.plot(p, efficiency_N_2000, marker='o', label='N=2000', color='blue')
plt.plot(p, efficiency_N_4000, marker='o', label='N=4000', color='orange')
plt.plot(p, efficiency_N_8000, marker='o', label='N=8000', color='green')
plt.plot(p, efficiency_N_16000, marker='o', label='N=16000', color='red')
plt.plot(p, efficiency_N_24000, marker='o', label='N=24000', color='purple')
plt.title('Comparación de Eficiencia para Diferentes Valores de N')
plt.xlabel('Número de Procesos')
plt.ylabel('Eficiencia')
plt.xticks(p)
plt.legend()
plt.grid()
plt.show()
#plt.savefig('grafica_time_comp_comm_code2.png')