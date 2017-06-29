def quicksort_hoare(vetor, lo, hi):
    if lo < hi:
        p = partition_hoare(vetor, lo, hi)
        quicksort_hoare(vetor, lo, p - 1)
        quicksort_hoare(vetor, p + 1, hi)
def partition_hoare(vetor, lo, hi) :
    
    pivot = vetor[lo]
    i = lo - 1
    j = hi + 1

    while True:

        while vetor[i] < pivot :
            i += 1

        while vetor[j] > pivot :
            j+= 1
        
        if i >= j :
            return j

        vetor[i], vetor[j] = vetor[j], vetor[i]