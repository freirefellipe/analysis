# ESSE CÓDIGO EXTRAI DE UMA TEXTO NÚMEROS DE TELEFONE POR MEIO DE REGEX E CONCATENA (COLLAPSE) ELEMENTOS DE UMA LISTA PARA JUNTAR TODOS OS NÚMEROS DE UM TELEFONE POR MEIO DO MÉTODO JOIN.

import csv
import re


with open (file='ebac.txt', mode='r', encoding='utf8') as fp: # carrego o documento
	ebac =  fp.readlines()
	contato = {}

contato['whatsapp'] = list(filter(lambda ogni: 'WhatsApp' in ogni, ebac)) # acha a linha com a informação desejada
contato['whatsapp'] = re.findall(r'\d+', contato['whatsapp'][0]) # pega somente a informação (nesse caso, números)
contato['whatsapp'] = ''.join(contato['whatsapp']) # junta os números em forma de str

contato['telefone'] = list(filter(lambda ogni: 'Telefone' in ogni, ebac))
contato['telefone'] = re.findall(r'\d+', contato['telefone'][0])
contato['telefone'] = ''.join(contato['telefone'])

contato_keys = iter(contato) # para poder acessar somente a chave do dicionário posteriormente com next()

with open(file='contato_ebac.csv', mode='w', encoding='utf8') as fp: # escrevo as informações, separando adequadamente, em arquivo csv
	contato_ebac = csv.writer(fp, delimiter=';') # cria o documento ainda sem conteúdo, informando qual será o delimitador
	contato_ebac.writerows([['tipo','número']] + [[next(contato_keys), contato['whatsapp']]] + [[next(contato_keys), contato['telefone']]]) # escreve a linha. Dá para escrever várias no mesmo comaondo, ou de uma em uma com writerows()

