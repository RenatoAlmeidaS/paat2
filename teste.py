import random
import time
import sys
import resource

resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

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
lomuto = []
hoare = []

def tempo(func, vetor, boolim):
	retorno = 0
	for i in range(3):
		if (boolim == "true"):
			print("vai gerar aleatorio")
			random.shuffle(vetor)
			print("gerou aleatorio")
		inicial = time.time()
		func(list(vetor), 0, len(vetor)-1)
		final = time.time()
		retorno += ((final - inicial)/3)
	return retorno

def rodar(entrada,boolim):
	
	lomuto.append( tempo( quicksort_lomuto, list(entrada), boolim ) )
	print ("TERMINOU lomuto")
	hoare.append( tempo( quicksort_hoare, list(entrada), boolim ) )
	print ("TERMINOU hoare")


def dicionario ():
	lomutoC = {}
	lomutoD = {}
	lomutoA = {}
	hoareC = {}
	hoareD = {}
	hoareA = {}
	i = 0
	while i < len(lomuto):
		if i%3==0: 
			lomutoC[tamanho[int(i/3)]] = lomuto[i]
		if i%3==1: 
			lomutoD[tamanho[int(i/3)]] = lomuto[i]
		if i%3==2: 
			lomutoA[tamanho[int(i/3)]] = lomuto[i]
		i += 1
	i = 0
	while i < len(hoare):
		if i%3==0: 
			hoareC[tamanho[int(i/3)]] = hoare[i]
		if i%3==1: 
			hoareD[tamanho[int(i/3)]] = hoare[i]
		if i%3==2: 
			hoareA[tamanho[int(i/3)]] = hoare[i]
		i += 1	
	print (lomutoC)
	print (lomutoD)
	print (lomutoA)
	print (hoareC)
	print (hoareD)
	print (hoareA)

for i in tamanho:
	entrada = list(range(i))
	print ("--------RODAR ORDEM CRESCENTE PARA " + str(i))
	rodar(list(entrada),"false")
	print ("--------TERMINOU ORDEM CRESCENTE PARA " +str(i))
	entrada.reverse()
	rodar(list(entrada),"false")
	print ("--------TERMINOU ORDEM DECRESCENTE PARA " +str(i))
	rodar(list(entrada),"true")
	print ("--------TERMINOU ALEATORIO PARA " +str(i))
dicionario()