# ESSE CÓDIGO EXTRAI DUAS COLUNAS DE UMA PLANILHA DE EXCEL, REMOVE DUPLICATAS, CRIA UM DICIONÁRIO COM AS DUAS COLUNAS E INTERPRETA COM JSON

from openpyxl import load_workbook
import csv


planilhas = load_workbook(filename='credito.xlsx')
planilha = planilhas.active

header = next(planilha.values)

escolaridade = header.index('escolaridade')
tipo_cartao = header.index('tipo_cartao')


duas_colunas = list((dado[escolaridade], dado[tipo_cartao]) for dado in planilha.values)
duas_colunas = set(duas_colunas)
duas_colunas = list(duas_colunas)

credito = {}
credito['escolaridade'] = list(ogni[0] for ogni in duas_colunas if ogni[0] != 'escolaridade')
credito['tipo_cartao'] = list(ogni[1] for ogni in duas_colunas if ogni[1] != 'tipo_cartao')

credito['escolaridade'] = set(credito['escolaridade'])
credito['tipo_cartao'] = set(credito['tipo_cartao'])

credito['escolaridade'] = list(credito['escolaridade'])
credito['tipo_cartao'] = list(credito['tipo_cartao'])

print(credito)


import json


credito_json = json.dumps(credito, indent=4) # cria variável para receber o código json dumps, tendo, dentro dos parênteses, o dicionário alvo e o número desejado da indentação separados por vírgula.

print(credito_json)
