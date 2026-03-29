
#bubble sort - algoritmul naiv

def bubble_sort(arr):

    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - 1 - i): # mereu ultimul e pe pozitia corecta 

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #swap

                swapped = True

        if not swapped:
            break
    return arr


if __name__ == "__main__":

    print(
        bubble_sort([2,3,4,1,0,7,5])
        )
