import sys
import resource
import random
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

def quicksort_hoare(vetor, lo, hi):
    if lo < hi:
        p = partition_hoare(vetor, lo, hi)
        quicksort_hoare(vetor, lo, p - 1)
        quicksort_hoare(vetor, p + 1, hi)
def partition_hoare(vetor, lo, hi) :
    
    pivot = vetor[lo]

    i = lo
    j = hi

    while True:

        while vetor[i] < pivot :
            i += 1

        while vetor[j] > pivot :
            j-= 1
        
        if i >= j :
            return j

        vetor[i], vetor[j] = vetor[j], vetor[i]

vet = list(range(5))
random.shuffle(vet)
print(vet)
quicksort_hoare(vet, 0, 4)
print(vet)