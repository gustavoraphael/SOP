import random

#Gera um vetor (memória) com 100 espacos
memoria = [''] * 100

#popula o vetor(memoria) com o caractere x de forma aleatoria
print("M E M O R I A")
for i in range(len(memoria)):
    if (random.randint(0,11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ''
		
#Printa o vetor(memoria) na tela quebrando de 20 em 20 celulas
p = 0
for i in range(int(len(memoria)/20)):
    a = p
    p = p+20
    print(memoria[a:p])

def bestf(ltr,tmn):
	cont = 0
	a = 0
	aux = True

	for a in range(len(memoria)):
		if memoria[a] != '':
			cont = 0
		elif memoria[a] == '':
			cont = cont+1
			if cont == tmn:
				aux = False
				for c in range(tmn):
					memoria[a] = ltr
					a=a-1
				break
	if aux:
		print("Nao ha espaco para armzenar tal informacao")

	#Printa o vetor(memoria) na tela quebrando de 20 em 20 celulas
	p = 0
	for i in range(int(len(memoria)/20)):
		a = p
		p = p+20
		print(memoria[a:p])

#Rodando os programas
print("Buscando espaco para programa A")
bestf('a',4)
print("Buscando espaco para programa B")
bestf('b',3)
print("Buscando espaco para programa C")
bestf('c',2)
