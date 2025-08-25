def oddcount(lista):
	par = 0
	impar = 0

	for i in lista:
		if i % 2 == 0:
			print(f'{i} é número par.')
			par += 1
		else:
			print(f'{i} é número ímpar.')
			impar += 1

	print(f'A referida lista tem {par} números pares e {impar} números ímpares.')

def findeven(lista):

	for i in lista:
		if i % 2 == 0:
			print(f'Número par encontrado ({i}). Tarefa encerrada.')
			break
		else:
			continue


# esse programa conta a quantidade de números ímpares e pares em um lista com 'oddcount' ou escaneia uma lista pelo primeiro número para que aparecer com 'findeven'
# no código que desejar usar essas funções, é necessário importá-las com 'from buscador import <função_desejada>'

