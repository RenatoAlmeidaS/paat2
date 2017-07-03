import random
import sys
import time
import resource

resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

arq = open("tempo lomuto.txt","w")


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


tamanho = [100, 500, 1000, 5000, 30000, 80000, 100000, 150000, 200000]
i = 0




#100
l = list(range(tamanho[0]))
arq.write("\n\nPARA 100 C D A\n")
#CRESCENTE
arq.write("CRESCENTE\n")
inicial = time.time()
quicksort_lomuto(l,0,99)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,99)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,99)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#DECRESCENTE
arq.write("DESCENDENTE\n")
l.reverse()
inicial = time.time()
quicksort_lomuto(l,0,99)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,99)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,99)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#ALEATORIO
arq.write("ALEATORIO\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,99)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,99)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,99)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#500
l = list(range(tamanho[1]))
arq.write("\n\nPARA 500 C D A\n")
#CRESCENTE
arq.write("CRESCENTE\n")
inicial = time.time()
quicksort_lomuto(l,0,499)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,499)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,499)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#DECRESCENTE
arq.write("DESCENDENTE\n")
l.reverse()
inicial = time.time()
quicksort_lomuto(l,0,499)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,499)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,499)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#ALEATORIO
arq.write("ALEATORIO\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,499)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,499)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,499)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#1000
l = list(range(tamanho[2]))
arq.write("\n\nPARA 1000 C D A\n")
#CRESCENTE
arq.write("CRESCENTE\n")
inicial = time.time()
quicksort_lomuto(l,0,999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#DECRESCENTE
arq.write("DESCENDENTE\n")
l.reverse()
inicial = time.time()
quicksort_lomuto(l,0,999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#ALEATORIO
arq.write("ALEATORIO\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#5000
l = list(range(tamanho[3]))
arq.write("\n\nPARA 5000 C D A\n")
#CRESCENTE
arq.write("CRESCENTE\n")
inicial = time.time()
quicksort_lomuto(l,0,4999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,4999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,4999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#DECRESCENTE
arq.write("DESCENDENTE\n")
l.reverse()
inicial = time.time()
quicksort_lomuto(l,0,4999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,4999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,4999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#ALEATORIO
arq.write("ALEATORIO\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,4999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,4999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,4999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#30k
l = list(range(tamanho[4]))
arq.write("\n\nPARA 30k C D A\n")
#CRESCENTE
arq.write("CRESCENTE\n")
inicial = time.time()
quicksort_lomuto(l,0,29999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,29999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,29999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#DECRESCENTE
arq.write("DESCENDENTE\n")
l.reverse()
inicial = time.time()
quicksort_lomuto(l,0,29999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,29999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,29999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#ALEATORIO
arq.write("ALEATORIO\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,29999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,29999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,29999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#80k
l = list(range(tamanho[5]))
arq.write("\n\nPARA 80k C D A\n")
#CRESCENTE
arq.write("CRESCENTE\n")
inicial = time.time()
quicksort_lomuto(l,0,79999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,79999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,79999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#DECRESCENTE
arq.write("DESCENDENTE\n")
l.reverse()
inicial = time.time()
quicksort_lomuto(l,0,79999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,79999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,79999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#ALEATORIO
arq.write("ALEATORIO\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,79999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,79999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,79999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#100k
l = list(range(tamanho[6]))
arq.write("\n\nPARA 100k C D A\n")
#CRESCENTE
arq.write("CRESCENTE\n")
inicial = time.time()
quicksort_lomuto(l,0,99999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,99999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,99999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#DECRESCENTE
arq.write("DESCENDENTE\n")
l.reverse()
inicial = time.time()
quicksort_lomuto(l,0,99999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,99999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,99999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#ALEATORIO
arq.write("ALEATORIO\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,99999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,99999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,99999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#150k
l = list(range(tamanho[7]))
arq.write("\n\nPARA 150k C D A\n")
#CRESCENTE
arq.write("CRESCENTE\n")
inicial = time.time()
quicksort_lomuto(l,0,149999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,149999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,149999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#DECRESCENTE
arq.write("DESCENDENTE\n")
l.reverse()
inicial = time.time()
quicksort_lomuto(l,0,149999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,149999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,149999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#ALEATORIO
arq.write("ALEATORIO\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,149999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,149999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,149999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")


#200000
l = list(range(tamanho[8]))
arq.write("\n\nPARA 200k C D A\n")
#CRESCENTE
arq.write("CRESCENTE\n")
inicial = time.time()
quicksort_lomuto(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#DECRESCENTE
arq.write("DECRESCENTE\n")
l.reverse()
inicial = time.time()
quicksort_lomuto(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
inicial = time.time()
quicksort_lomuto(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

#ALEATORIO
arq.write("ALEATORIO\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")
random.shuffle(l)
inicial = time.time()
quicksort_lomuto(l,0,199999)
final = time.time()
tempo = str(final-inicial)
arq.write(tempo)
arq.write("\n")

arq.close()