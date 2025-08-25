################## EXTRAINDO COLUNA DE ARUIVO .CSV COM FUNÇÃO

def extrai_coluna (nome_arquivo: str, numero_coluna: int):

  coluna_extraida = []
  
  with open(file=nome_arquivo, mode='r', encoding='utf8') as dados:
    linha = dados.readline() # lê o cabeçalho
    #linha = dados.readline() # lê a primeira linha   
    while linha:
      coluna = linha.split(sep=',') # quebra a string nas virgulas e salva os resultados em uma lista
      coluna_desejada = coluna[numero_coluna - 1] # seleciona o segundo elemento da lista
      coluna_extraida.append(coluna_desejada) # salva o valor na lista de valor_venda
      linha = dados.readline() # lê uma nova linha, se a linha não existir, salva o valor None
  return coluna_extraida

coluna_arquivo = extrai_coluna(nome_arquivo='./dados.csv', numero_coluna=1)
print(coluna_arquivo)

######################## EXTRAINDO NOME E SOBRENOME DE UM NOME COMPLETO POR MEIO DE FUNÇÕES.

nome_completo = 'Fellipe Freire Oliveira'

def nome_proprio(i):

  nome_proprio = nome_completo.split(sep=' ')[0]
  return nome_proprio

def sobrenome(i):
  
  nome_meio = nome_completo.split(sep=' ')[1]
  nome_ultimo = nome_completo.split(sep=' ')[2]
  sobrenome = nome_meio + ' ' + nome_ultimo
  return sobrenome

print(nome_proprio(nome_completo))    
print(sobrenome(nome_completo))


######################## TRANSFERINDO DADOS DE ARQUIVO .CSV PARA DICIONÁRIOS DENTRO DE LISTAS, INDEXANDO COLUNAS 


dati = [] # crio uma lista para colocar os dados desejados

with open (file='dados.csv', mode='r', encoding='utf8') as arquivo: # chamo o arquivo a ser lido

    header = arquivo.readline().split(sep=',') # transformo o cabeçalho em uma variável

    riga = arquivo.readline() # leio a próxima linha com dados importantes

    while riga: # crio um loop para repetir a criação de dicionários e inclusão na variável inicial

       collona_dati = riga.split(sep=',') # separar o texto em dados

       riga_dizio = {} # criar um dicionário vazio

# incluir os dados provindos do texto no dicionário, relacionando chave (o cabeçalho de antes) e valor (os elementos provindos do texto) corretamente

       riga_dizio[header[0]] = collona_dati[0]

       riga_dizio[header[1]] = collona_dati[1]

       riga_dizio[header[2]] = collona_dati[2]

       riga_dizio[header[3]] = collona_dati[3]

       dati.append(riga_dizio) # adicionar o dicionário na lista do início

       riga = arquivo.readline() # ler a próxima linha

for dato in dati:
    print(dato['coluna_1'])

print(dati[0]['coluna_1'])


######################## EXTRAINDO TEXTO DE TAGS DE HTML


from bs4 import BeautifulSoup

with open(file='texto.txt', mode='r', encoding='utf8') as fp:
    texto = fp.read()
    texto = BeautifulSoup(open('texto.txt', mode='r'), 'html.parser')
    h1 = texto.find('h1')
    h1_text = h1.get_text()

print(h1_text)


######################### EXECUTANDO COMANDOS NO TERMINAL COM PYTHON

import os

os.system('aqui vai o comando em python') # apesar de funcionar, tá depricated. Importar o 'subprocess' ao invés.

import subprocess

subprocess
