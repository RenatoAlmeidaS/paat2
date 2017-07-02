import random


arq = open("a.txt","w")

tamanho = [100, 500, 1000, 5000, 30000, 80000, 100000, 150000, 200000]
i = 0
texto = ""

def escreve(batata):
	a = str(l)
	arq.write(a)
	arq.write("\n")


while (i<len(tamanho)):
	l = list(range(tamanho[i]))
	escreve(l)
	l.reverse()
	escreve(l)
	j = 0
	while (j<3):
		random.shuffle(l)
		escreve(l)
		j += 1
	i += 1
arq.close()