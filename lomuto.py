def quicksort_lomuto(vetor, lo, hi):
    if lo < hi:
        p = partition_lomuto(vetor, lo, hi)
        quicksort_lomuto(vetor, lo, p - 1)
        quicksort_lomuto(vetor, p + 1, hi)
def partition_lomuto(vetor, lo, hi):
    pivot = vetor[hi]
    i = lo - 1
    j = lo
    while(j <= hi):
        if vetor[j] <= pivot:
            i += 1
            if(i <> j):
                vetor[i], vetor[j] = vetor[j], vetor[i]
        j += 1
    return i