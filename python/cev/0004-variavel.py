a = input('Digite alguma coisa: ')

print('O tipo primitivo desse valor é' ,type(a))


if a.isnumeric() == True:
	print('O que você digitou é número.')
	
elif a.isalpha() == True:
	print('O que você digitou é texto.')
	
elif a.isalnum() == True:
	print('O que você digitou é alfamumérico.')

elif a.isupper() == True:
	print('O texto está todo em maiúsculo.')

elif a.islower() == True:
	print('O texto está todo em minúsculo.')
	
elif a.istitle() == True:
	print('As palavras começam com letra maiúscula.')

else:
	print('É qualque outra coisa; só não é número, nem texto.')
