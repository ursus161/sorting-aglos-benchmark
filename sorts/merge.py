#merge sort,  extrem de paralelizabil

def merge_sort(arr):
    if len(arr) <= 1:
        return

    #partea de divide
    mid = len(arr) // 2
    left = arr[:mid] 
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    # interclasare
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # ce a ramas
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

import ctypes
from multiprocessing import Semaphore, Array, Process

def merge_sort_parallel(arr, threshold=10_000):
    """split array in 2, sorteaza fiecare jumatate in proces separat,
    interclaseaza in procesul parinte.
 
    sub threshold cade pe secvential, nu merita overhead-ul.
    
    dupa teste ajunem si la concluzia ca pe date mici, chiar si cele in ordinul zecilor de mii , inca avem un overhead prea mare la fork() ptr un proces nou
    
    """
    n = len(arr)
 
    if n < threshold:
        merge_sort(arr)
        return
 
    shared = Array(ctypes.c_long, arr) # shared memory
    mid = n // 2
 
    sem_left = Semaphore(0)
    sem_right = Semaphore(0)
 
    p_left = Process(target=_worker, args=(shared, 0, mid, sem_left))
    p_right = Process(target=_worker, args=(shared, mid, n, sem_right))
 
    p_left.start()
    p_right.start()
 
    sem_left.acquire()
    sem_right.acquire()
 
    p_left.join()
    p_right.join()
 
    # interclasare
    left = list(shared[:mid])
    right = list(shared[mid:])
 
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
 
 
def _worker(shared, start, end, sem):
    chunk = list(shared[start:end])
    merge_sort(chunk)
    for i, val in enumerate(chunk):
        shared[start + i] = val
    sem.release()
 