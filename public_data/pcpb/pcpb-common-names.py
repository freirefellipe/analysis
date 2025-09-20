# ESSE CÓDIGO COMPARA DOIS DOCUMENTOS CSV PARA VER NOMES EM COMUM.  É PRECISO DIGITAR O NOME DE DOIS DOCUMENTOS COM A TERMINAÇÃO .CSV

import csv

print('ESSE CÓDIGO COMPARA DOIS DOCUMENTOS CSV PARA VER NOMES EM COMUM.  É PRECISO DIGITAR O NOME DE DOIS DOCUMENTOS COM A TERMINAÇÃO .CSV')

a = input('nome do primeiro documento csv a comparar: ')
b = input('nome do segundo documento csv a comparar: ')

with open (file=a, mode='r', encoding='utf8') as local_ipc:
    file_ipc = csv.reader(local_ipc, delimiter=';')
    next(file_ipc)
    candidatos_ipc = [elmnt[1] for elmnt in file_ipc]

    with open (file=b, mode='r', encoding='utf8') as local_epc:
      file_epc = csv.reader(local_epc, delimiter=';')
      next(file_epc)
      candidatos_epc = [lmnt[1] for lmnt in file_epc]

common_candidates = list(set(candidatos_epc) & set(candidatos_ipc))

for candidate in common_candidates:
    print(candidate)

for common_candidate in common_candidates:
print(common_candidate)
