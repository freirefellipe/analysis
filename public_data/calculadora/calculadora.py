from operacoes import soma, subtrai, multiplica, divide, potencia, raiz_quadrada, logaritmo

operacoes = ['soma', 'subtrai', 'multiplica', 'divide', 'potencia', 'raiz_quadrada', 'logaritmo']

def menu():

	print('0 - soma\n1 - subtrai\n2 - multiplica\n3 - divide\n4 - potencia\n5 - raiz quadrada\n6 - logaritmo\n')
	operacao_desejada = int(input('Operação desejada? > '))
	return operacao_desejada

def calculadora():

	opcao = menu()

	if opcao == 0: # soma

		a = int(input('Primeiro valor: '))
		b = int(input('Segundo valor: '))
		resultado = soma(a, b)
		print('O resultado da soma é', resultado)

	elif opcao == 1: # subtração

		a = int(input('Primeiro valor: '))
		a = int(input('Segudno valor: '))
		resultado = subtrai(a, b)
		print('O resultado da asubtração é', resultado)

	elif opcao == 2:

		a = int(input('Primeiro valor: '))
		b = int(input('Segundo valor: '))
		resultado = multiplica(a, b)
		print('O resultado da multiplicação é', resultado)

	elif opcao == 3:

		a = int(input('Primeiro valor: '))
		b = int(input('Segundo valor: '))
		resultado = divide(a, b)
		print('O resultado da divisão é', resultado)

	elif opcao == 4:

		a = int(input('Valor: '))
		resultado = potencia(a)
		print('A potência é', resultado)

	elif opcao == 5:

		a = int(input('Valor: '))
		resultado = raiz_quadrada(a)
		print('A raiz quadrada é', resultado)

	elif opcao == 6:

		a = int(input('Valor: '))
		resultado = logaritmo(a)
		print('O logaritmo é', resultado)

	else:
		print('Opção inválida.')

if __name__ == '__main__':

	calculadora()

	

