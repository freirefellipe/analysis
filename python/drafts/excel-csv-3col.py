# ESSE CÓDIGO EXTRAI TRÊS COLUNAS DE UM DOCUMENTO EXCELL E CRIA UM DOCUMENTO CSV COM ELAS

from openpyxl import load_workbook
import csv

# wget --show-progress --continue credito.xlsx https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/dataset/credito.xlsx')

doc_input = str(input('Insira o nome do documento. >'))

planilhas = load_workbook(filename=doc_input)
planilha = planilhas.active

header = next(planilha.values)

identidade = header.index('id')
sexo = header.index('sexo')
idade = header.index('idade')
default = header.index('default')
estado_civil = header.index('estado_civil')

id_sex_age = list([dado[identidade], dado[sexo], dado[idade]] for dado in planilha.values if dado[default] == 1 and dado[estado_civil] == 'solteiro') # se quiser remover elementos duplicados com set(), em vez de fazer os elementos com [] faz com ();

with open(file='credito.csv', mode='w', encoding='utf8') as doc:
 	doc_csv = csv.writer(doc, delimiter=';')
 	doc_csv.writerows([['id', 'sexo', 'idade']])
 	doc_csv.writerows(map(lambda elem : [elem[0], elem[1], elem[2]], id_sex_age))

print('sucesso.')

