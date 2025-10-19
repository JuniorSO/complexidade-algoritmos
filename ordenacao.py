import time
import random
import matplotlib.pyplot as plt

# Algoritmo de ordenação bubble sort O(n^2)
def bubble_sort(list, list_length):
    for i in range(list_length):
        swapped = False
        for j in range(list_length - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        if not swapped:
            break

    return list

# Algoritmo de ordenação selection sort O(n^2)
def selection_sort(list, list_length):
    for i in range(list_length - 1):
        min_index = i
        for j in range(i + 1, list_length):
            if list[j] < list[min_index]:
                min_index = j
        if list[i] != list[min_index]:
            list[i], list[min_index] = list[min_index], list[i]

    return list

# Algoritmo de ordenação insertion sort O(n^2)
def insertion_sort(list, list_length):
    for i in range(1, list_length):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

    return list

# Algoritmo de ordenação merge sort O(n log n)
def merge_sort(list):
    list_length = len(list)
    if list_length <= 1:
        return list
    
    middle = list_length // 2
    left = list[:middle]
    right = list[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    left_length = len(left)
    right_length = len(right)

    while i < left_length and j < right_length:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < left_length:
        result.append(left[i])
        i += 1

    while j < right_length:
        result.append(right[j])
        j += 1

    return result

# Causa o erro RecursionError: maximum recursion depth exceeded
# para 2048 elementos, mesmo depois de aumentar o limite de recursão
# para 2000.
# def quick_sort(list):
#     list_length = len(list)
#     if list_length <= 1:
#         return list
    
#     pivot = list[-1]
#     smaller = [elem for elem in list[:-1] if elem <= pivot]
#     bigger = [elem for elem in list[:-1] if elem > pivot]

#     return quick_sort(smaller) + [pivot] + quick_sort(bigger)

# Solução iterativa de Quick Sort:
# Algoritmo de ordenação quick sort O(n log n)
def quick_sort(list, start, end):
    size = end - start + 1
    stack = [0] * (size)

    top = -1

    top += 1
    stack[top] = start
    top += 1
    stack[top] = end

    while top >= 0:
        end = stack[top]
        top -= 1
        start = stack[top]
        top -= 1

        pivot = partition(list, start, end)

        if pivot - 1 > start:
            top += 1
            stack[top] = start
            top += 1
            stack[top] = pivot - 1
        if pivot + 1 < end:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = end

def partition(list, start, end):
    i = (start - 1)
    x = list[end]

    for j in range(start, end):
        if list[j] <= x:
            i += 1
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[end] = list[end], list[i + 1]
    return (i + 1)

sorts = ['bubble', 'selection', 'insertion', 'merge', 'quick']
n_qtd_list = []
time_taken_bubble = []
time_taken_selection = []
time_taken_insertion = []
time_taken_merge = []
time_taken_quick = []

seed = 2
quantity = 17 # Atenção com esse valor, diminuir para máquinas com menos RAM, impacta na precisão do resultado final
for i in range(quantity): # Populando a lista 'n_qtd_list' com conjuntos de valores
    n_qtd_list.append(seed)
    seed *= 2
print('[*]Lista n populada.')

random_list = []
previous_n_qtd = 1
for n_qtd in n_qtd_list: # Utilizando 'n_qtd' para definir quantos elementos existirão em cada lista
    time_list_start = time.time()
    random_list.extend(range(previous_n_qtd, n_qtd + 1)) # Incrementando a lista
    previous_n_qtd = n_qtd + 1
    random.shuffle(random_list) # Embaralhando os elementos dentro da lista
    time_list_end = time.time()
    time_list_tooked = time_list_end - time_list_start
    print(f'[*]Tempo de Gerar Lista Aleatória para {n_qtd} Elementos: {time_list_tooked:.5f} segundos')

    for sort in sorts:
        match sort:
            case 'bubble':
                time_start_bubble = time.time()
                bubble_sort(random_list, n_qtd)
                time_end_bubble = time.time()
                time_tooked_bubble = time_end_bubble - time_start_bubble
                time_taken_bubble.append(time_tooked_bubble)
                print(f'[*]Tempo de Ordenação (BubbleSort) para {n_qtd} Elementos: {time_tooked_bubble:.5f} segundos')
                random.shuffle(random_list) # Embaralhando os elementos dentro da lista para garantir que as outras ordenações funcionem como esperado

            case 'selection':
                time_start_selection = time.time()
                selection_sort(random_list, n_qtd)
                time_end_selection = time.time()
                time_tooked_selection = time_end_selection - time_start_selection
                time_taken_selection.append(time_tooked_selection)
                print(f'[>]Tempo de Ordenação (SelectionSort) para {n_qtd} Elementos: {time_tooked_selection:.5f} segundos')
                random.shuffle(random_list)

            case 'insertion':
                time_start_insertion = time.time()
                insertion_sort(random_list, n_qtd)
                time_end_insertion = time.time()
                time_tooked_insertion = time_end_insertion - time_start_insertion
                time_taken_insertion.append(time_tooked_insertion)
                print(f'[!]Tempo de Ordenação (InsertionSort) para {n_qtd} Elementos: {time_tooked_insertion:.5f} segundos')
                random.shuffle(random_list)

            case 'merge':
                time_start_merge = time.time()
                merge_sort(random_list)
                time_end_merge = time.time()
                time_tooked_merge = time_end_merge - time_start_merge
                time_taken_merge.append(time_tooked_merge)
                print(f'[#]Tempo de Ordenação (MergeSort) para {n_qtd} Elementos: {time_tooked_merge:.5f} segundos')
                random.shuffle(random_list)

            case 'quick':
                time_start_quick = time.time()
                quick_sort(random_list, 0, n_qtd - 1)
                time_end_quick = time.time()
                time_tooked_quick = time_end_quick - time_start_quick
                time_taken_quick.append(time_tooked_quick)
                print(f'[?]Tempo de Ordenação (QuickSort) para {n_qtd} Elementos: {time_tooked_quick:.5f} segundos')
                random.shuffle(random_list)

# Criando gráfico para visualizar os tempos
fig, ax = plt.subplots()
ax.plot(n_qtd_list[:len(time_taken_bubble)], time_taken_bubble, label='Bubble Sort O(n^2)')
ax.plot(n_qtd_list[:len(time_taken_selection)], time_taken_selection, label='Selection Sort O(n^2)')
ax.plot(n_qtd_list[:len(time_taken_insertion)], time_taken_insertion, label='Insertion Sort O(n^2)')
ax.plot(n_qtd_list[:len(time_taken_merge)], time_taken_merge, label='Merge Sort O(n log n)')
ax.plot(n_qtd_list[:len(time_taken_quick)], time_taken_quick, label='Quick Sort (iterativo) O(n log n)')
ax.set_ylabel("Tempo (Segundos)")
ax.set_xlabel("Número de Elementos")
ax.set_title("Ordenação")
ax.legend()

plt.show()