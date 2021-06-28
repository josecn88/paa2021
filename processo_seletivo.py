#!/usr/bin/python3
"""
Olá Professor Diego!
Infelizmente para o caso do trabalho, todas as implementações de algorítmo de sort que encontrei
estouram o tempo de processamento no run.codes. A única que executou dentro do intervalo de
tempo proposto foi o sort do próprio Python.
"""
MIN_MERGE = 32

def processoSeletivo():
    try:
        n = int(input())
    except:
        return 1

    for i in range(1,n+1):
        aux = input().split()
        K = int(aux[0])
        C = int(aux[1])
        nota = [float(x) for x in aux[2:]]
        #quickSort(nota, 0, len(nota)-1)
        #mergeSort(nota)
        #qsort(nota)
        #quickSort2(nota)
        nota.sort()
        #timSort(nota)
        #shellSort(nota,len(nota))
        print(format(nota[C-K],'.2f'))

def particao(vetor, inicial, final):
    i = inicial-1           # indice do menor elemento
    pivo = vetor[final]     # pivo
  
    for j in range(inicial, final):
        # Se o elemwnto atual é menor ou igual ao pivô
        if vetor[j] <= pivo:
            # indice do menor elemento ++
            i = i+1
            #troca posicao
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i+1], vetor[final] = vetor[final], vetor[i+1]
    return (i+1)
  
def quickSort(vetor, inicial, final):
    if len(vetor) == 1:
        return vetor
    if inicial < final:
        # pi é o indice da particao. Vetor[p] esta na posicao correta
        pi = particao(vetor, inicial, final)
        # Recursivamente ordenar os elementos antes e depois de 'pi'
        quickSort(vetor, inicial, pi-1)
        quickSort(vetor, pi+1, final)
      
def mergeSort(vetor):
    if len(vetor)>1:
        meio = len(vetor)//2
        esquerda = vetor[:meio]
        direita = vetor[meio:]

        mergeSort(esquerda)
        mergeSort(direita)

        i=0
        j=0
        k=0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k]=esquerda[i]
                i=i+1
            else:
                vetor[k]=direita[j]
                j=j+1
            k=k+1

        while i < len(esquerda):
            vetor[k]=esquerda[i]
            i=i+1
            k=k+1

        while j < len(direita):
            vetor[k]=direita[j]
            j=j+1
            k=k+1

def qsort(inlist):
    if inlist == []: 
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater

def quickSort2(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort2(less)
        more = quickSort2(more)
        return less + pivotList + more


 
def calcMinRun(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.
 
    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r
 
 
# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
 
 
# Merge function merges the sorted runs
def merge(arr, l, m, r):
     
    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
 
    i, j, k = 0, 0, l
     
    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
 
        else:
            arr[k] = right[j]
            j += 1
 
        k += 1
 
    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
 
    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
 
 
# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)

#Algoritmo usado nos métodos sorted() e sort() in Python
# https://www.geeksforgeeks.org/timsort/

def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
     
    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
 
    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:
         
        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
 
            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)
 
        size = 2 * size


def shellSort(inp, n):
 
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = inp[i]
            j = i
            while j >= h and inp[j - h] > t:
                inp[j] = inp[j - h]
                j -= h
 
            inp[j] = t
        h = h // 2

if __name__ == "__main__":
    processoSeletivo()