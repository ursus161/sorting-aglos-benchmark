def heap_sort(arr):
    n = len(arr)

    def heap_repair(parent, limit):

        while True:
            left = 2 * parent + 1
            right = 2 * parent + 2

            # gasim cel mai mare dintre parinte, left, right
            largest = parent #am init asa ca nu mai copiez nimic in largest 
            if left <= limit and arr[left] > arr[largest]:
                largest = left
            if right <= limit and arr[right] > arr[largest]:
                largest = right

            # daca parintele e deja cel mai mare, gata, asta e si scopu functiei
            if largest == parent:
                break

            arr[parent], arr[largest] = arr[largest], arr[parent] 
            parent = largest  # continua in jos



    # construieste max-heap, luam pe fiecare parinte pana ajungem la cel mai "tare" parinte adica radacina
    last_parent = n // 2 - 1 #asta e ultimu nod care are frunze
    for i in range(last_parent, -1, -1):
        heap_repair(i, n - 1)

    # extrage maximul repetat
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]  # maximul merge la sfarsit
        heap_repair(0, end - 1)                # repara heap-ul ramas
    
    return arr

if __name__ == "__main__":
    print(
        heap_sort(
            [8,4,2,5,7,3,1,6,7]
        )
     )

