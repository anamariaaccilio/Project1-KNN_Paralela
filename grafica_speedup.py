
import matplotlib.pyplot as plt
import numpy as np
#p= [2,4,8,16,32]
p= [2,4,8,10,12,16,20, 24, 28, 32]
#ts=18.7226
ts=11.0412
#t_code_2=[6.1682, 3.0465, 2.2287, 1.3701, 1.1308]
#t_code_2 = [5.6357, 2.9741, 2.1548, 2.128, 1.4814, 1.3925, 1.5371, 1.4586, 1.4908, 1.3469]
#t_code_2 =[5.9202	2.9599	1.6453	1.5938	1.3488	1.4151	1.0829	1.0261	1.2267	1.0119
#t_code_2 = [5.579, 2.8751, 1.5767, 1.431, 1.1938, 1.0362, 0.8484, 0.8154, 0.7223, 0.647]
t_code_2 = [5.6357, 2.9741, 2.1548, 2.128, 1.4814, 1.3925, 1.5371, 1.4586, 1.4908, 1.3469]

speedup = [ts / t for t in t_code_2]
print("Speedup values:", speedup)
plt.figure(figsize=(10, 6))
plt.plot(p, speedup, marker='o', label='Speedup knn_parallel_end', color='green')
plt.title('Speedup de knn_parallel_end para k=3')
plt.xlabel('Número de Procesos')
plt.ylabel('Speedup')
plt.xticks(p)
plt.legend()
plt.grid()
plt.show()