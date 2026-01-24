try:
	num_1 = int(input('Insira um número: '))
	num_2 = int(input('insira outro número: '))

	print(f'A soma de {num_1} e {num_2} é', num_1 + num_2)
	
except ValueError:
	print(f'Eu já imaginava que você ia querer inserir letra...')
	print(f'É pra inserir número, lesado!')
