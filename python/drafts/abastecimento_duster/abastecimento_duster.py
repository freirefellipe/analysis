
print('Controlador de abastecimento do Renault Duster.', '\n')


dicio_entrada = dict(
			data = str(input('Insira a data do abastecimento > ')),
			preco = float(input('Insira o preço do combustível > ')),
			km_total = int(input('Insira o total de km rodados > ')),
			km_parcial = float(input('Insira a parcial de km rodados > ')),
			litros = float(input('Insira a litragem > ')),
			kml = float(input('Insira a quilometragem por litro > ')),
			km_restante = int(input('Insira a quilometragem restante para o próximo abastecimento > ')),
			kmh_media = float(input('Insira a velocidade média do veículo > '))
		)

# for x in range(0, len(dicio_entrada), 1):
#	map(lambda i : dicio[x].append(dicio_entrada[x]), dicio_entrada)

import csv

with open (file='abastecimento_duster.csv', mode='a', encoding='utf8') as abastecimento_duster:

  abastecimento_duster_csv = csv.writer(abastecimento_duster, delimiter=';')
  abastecimento_duster_csv.writerows([[
	  				dicio_entrada['data'],
	  				dicio_entrada['preco'], 
	  				dicio_entrada['km_total'], 
	  				dicio_entrada['km_parcial'], 
	  				dicio_entrada['litros'], 
	  				dicio_entrada['kml'], 
	  				dicio_entrada['km_restante'], 
	  				dicio_entrada['kmh_media']
  				]])

print('Arquivo csv escrito com sucesso.', '\n')

## Caso queira criar um dicionário e adicionar as entradas neste.

#dicio = dict(
#		preco = [],
#		km_total = [],
#		km_parcial = [],
#		litros = [],
#		kml = [],
#		km_restante = [],
#		kmh_media = []		
#	)


#  dicio['preco'].append(dicio_entrada['preco'])
#  dicio['km_total'].append(dicio_entrada['km_total'])
#  dicio['km_parcial'].append(dicio_entrada['km_parcial'])
#  dicio['litros'].append(dicio_entrada['litros'])
#  dicio['kml'].append(dicio_entrada['kml'])
#  dicio['km_restante'].append(dicio_entrada['km_restante'])
#  dicio['kmh_media'].append(dicio_entrada['kmh_media'])


