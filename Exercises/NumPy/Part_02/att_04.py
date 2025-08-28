import numpy as np
import random

size_x = random.randint(1, 4)  # Evita tamanho 0
size_y = random.randint(1, 4)

mtz = np.random.randint(0, 10, (size_x, size_y)) 

print("Matriz original:")
print(mtz)

total_elements = mtz.shape[0] * mtz.shape[1]
print(f"Total de elementos: {total_elements}")

if total_elements % 2 == 0:
    print("Pode ser transformada em um array unidimensional com número PAR de elementos.")
else:
    print("Pode ser transformada em um array unidimensional com número ÍMPAR de elementos.")