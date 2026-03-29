#cam cel mai ok ptr uz generic in complexitatea O(n^2), e folosit intern si de timsort ul din python sub un threshold de cam 

def insertion_sort(arr):


    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr  