#in princpiu un bubble sort putin mai destept la turtles si date aproape sortate

def cocktail_sort(arr):
    n = len(arr)
    start, end = 0, n - 1
    swapped = True

    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        end -= 1

        if not swapped:
            break

        swapped = False
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        start += 1

    return arr


