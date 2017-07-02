import random
import sys
import time

arq = open("tempo.txt","w")


def quicksort_hoare(vetor, lo, hi):
    if lo < hi:
        p = partition_hoare(vetor, lo, hi)
        quicksort_hoare(vetor, lo, p - 1)
        quicksort_hoare(vetor, p + 1, hi)
def partition_hoare(vetor, lo, hi) :
    
    pivot = vetor[int((lo+hi)/2)]
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


tamanho = [100, 500, 1000, 5000, 30000, 80000, 100000, 150000, 200000]
i = 0

l = list(range(tamanho[8]))

#CRESCENTE
inicial = time.time()
quicksort_hoare(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write(" TEMPO PARA ")
arq.write("200k\n")
inicial = time.time()
quicksort_hoare(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write(" TEMPO PARA ")
arq.write("200k\n")
inicial = time.time()
quicksort_hoare(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write(" TEMPO PARA ")
arq.write("200k\n")

#DECRESCENTE
l.reverse()
inicial = time.time()
quicksort_hoare(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write(" TEMPO PARA ")
arq.write("200k\n")
inicial = time.time()
quicksort_hoare(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write(" TEMPO PARA ")
arq.write("200k\n")
inicial = time.time()
quicksort_hoare(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write(" TEMPO PARA ")
arq.write("200k\n")

#ALEATORIO
random.shuffle(l)
inicial = time.time()
quicksort_hoare(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write(" TEMPO PARA ")
arq.write("200k\n")
random.shuffle(l)
inicial = time.time()
quicksort_hoare(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write(" TEMPO PARA ")
arq.write("200k\n")
random.shuffle(l)
inicial = time.time()
quicksort_hoare(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write(" TEMPO PARA ")
arq.write("200k\n")
