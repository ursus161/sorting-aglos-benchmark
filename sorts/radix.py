#fapt ce mi se pare cel mai interesant la radix sort, desi in functie de nr cifre degenereaza, daca iau baza 256 pot la orice int32 sa am doar 4 iteratii
#daca ar fi sa lucrez pe un sistem cu RAM putin, ceva low level, asta ar fi ultima sortare pe care as alege-o, ptr ca am O(n+b) complex spatiala
#complexitate O(d * (n+b)) unde d si b sunt nr de cif si baza timp

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n          # O(n) extra memorie
    count = [0] * 10          # 10 bucket-uri, una per cifra, adica inca O(10) extra memorie de unde avem O(n+b)

    # numara aparitiile fiecarei cifre
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # prefix sum
    # count[d] devine "cate elemente au cifra <= d"
    for i in range(1, 10):
        count[i] += count[i - 1]

    #plaseaza elementele in output
    # parcurgem invers pentru stabilitate
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]

    # copiaza inapoi
    arr[:] = output

    
def radix_sort(arr):
    if not arr:
        return

    negatives = [-x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]

    if positives:
        max_val = max(positives)
        exp = 1
        while max_val // exp > 0:
            counting_sort_by_digit(positives, exp)
            exp *= 10

    if negatives:
        max_val = max(negatives)
        exp = 1
        while max_val // exp > 0:
            counting_sort_by_digit(negatives, exp)
            exp *= 10

    # negativele: sortate crescator ca valori absolute
    # le inversam si le facem negative inapoi
    result = [-x for x in reversed(negatives)] + positives
    arr[:] = result

    return arr

if __name__ == "__main__":
    print(radix_sort(
        [329, -355, 436, -457, 657, 720, 83]
    ))