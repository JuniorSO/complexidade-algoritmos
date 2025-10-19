import time
import matplotlib.pyplot as plt
import random

# Algoritmo de busca linear O(n)
def linear_search(n, list, list_length):
    for i in range(list_length):
        if list[i] == n:
            return i
    
    return -1

# Algoritmo de busca binária O(log n)
def binary_search(n, list, start, end):
    if end >= start:
        middle = (end + start) // 2
        if list[middle] == n:
            return middle
        elif n > list[middle]:
            return binary_search(n, list, middle, end)
        else:
            return binary_search(n, list, start, middle)
    else:
        return -1

searchs = ['linear', 'binary']
n_qtd_list = []
time_taken_linear = []
time_taken_binary = []

seed = 2
quantity = 30 # Atenção com esse valor, diminuir para máquinas com menos RAM, impacta na precisão do resultado final
for i in range(quantity): # Populando a lista 'n_qtd_list' com conjuntos de valores
    n_qtd_list.append(seed)
    seed *= 2
print('[*]Lista n populada.')

ordered_list = []
previous_n_qtd = 1
for n_qtd in n_qtd_list: # Utilizando 'n_qtd' para definir quantos elementos existirão em cada lista
    time_list_start = time.time()
    ordered_list.extend(range(previous_n_qtd, n_qtd + 1)) # Incrementando a lista
    previous_n_qtd = n_qtd + 1
    time_list_end = time.time()
    time_list_tooked = time_list_end - time_list_start
    print(f'[*]Tempo de Gerar Lista Ordenada para {n_qtd} Elementos: {time_list_tooked:.5f} segundos')
    
    chosen_n = random.choice(ordered_list)
    for search in searchs:
        match search:
            case 'linear':
                time_start_linear = time.time()
                linear_search(chosen_n, ordered_list, n_qtd)
                time_end_linear = time.time()
                time_tooked_linear = time_end_linear - time_start_linear
                time_taken_linear.append(time_tooked_linear)
                print(f'[*]Tempo de Busca (Busca Linear) para {n_qtd} Elementos: {time_tooked_linear:.5f} segundos')

            case 'binary':
                time_start_binary = time.time()
                binary_search(chosen_n, ordered_list, 0, n_qtd)
                time_end_binary = time.time()
                time_tooked_binary = time_end_binary - time_start_binary
                time_taken_binary.append(time_tooked_binary)
                print(f'[*]Tempo de Busca (Busca Binária) para {n_qtd} Elementos: {time_tooked_binary:.5f} segundos')

# Criando gráfico para visualizar os tempos
fig, ax = plt.subplots()
ax.plot(n_qtd_list[:len(time_taken_linear)], time_taken_linear, label='Linear Search O(n)')
ax.plot(n_qtd_list[:len(time_taken_binary)], time_taken_binary, label='Binary Search O(log n)')
ax.set_ylabel("Tempo (Segundos)")
ax.set_xlabel("Número de Elementos")
ax.set_title("Busca")
ax.legend()

plt.show()