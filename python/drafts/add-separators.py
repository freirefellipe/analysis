list_ = []	

with open (file='lista-escr-pcpb-t3-alem.csv', mode='r', encoding='utf8') as fp:
	with open(file='list-escr-pcpb-t3-on-separated.csv', mode='a', encoding='utf8') as roll_call:
		
		csv = fp.readline()

		while csv:
			csv = list(csv)
			csv[8] = ';'
			if csv[-5] == '1': 
				csv[-6] = ';'
				csv[-12] = ';'
			else:
				csv[-5] = ';'
				csv[-11] = ';'
			csv = ''.join(csv)
			roll_call.write(csv)
			csv = fp.readline()

print('Um documento .csv foi criado.')


# procedimento: era um bloco de texto com informações diferentes, porém juntas em uma só string. Para fazer a separação, nesse caso de linhas curtas, foi feito um comando de leitura de linha por linha do documento de texto. Cada linha lida ia sendo transformada em lista, sendo cada caractere da string um elemento da lista, para que, facilmente, fossem substituidos os elementos desejados por ';'. Por fim, cada linha ia, por sua vez, sendo salva em um novo documento, até sua conclusão.
