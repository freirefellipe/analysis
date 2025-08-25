# solução do exercício 1.1

import requests

URL = 'https://www.imdb.com/robots.txt'

try:
  robots = requests.get(url=URL)

except HTTPError as exc:
  print(exc)

else:
  robots_text = robots.text

import re

print(True) if re.findall('top' or 'chart', robots_text, re.IGNORECASE) else print(False)

# a) Utilize o pacote requests para fazer o download da página na variável conteudo

import requests
from requests.exceptions import HTTPError

conteudo = requests.get('https://www.imdb.com/chart/top/').text

with open(file='imdb.html', mode='w', encoding='utf8') as fp:
  pagina = fp.write(conteudo)


# b) Utilize o pacote beautifulsoup4 para carregar o HTML da variavel conteudo na variavel pagina

from bs4 import BeautifulSoup

pagina = BeautifulSoup(open('imdb.html', mode='r'), 'html.parser') # É possível baixar direto de uma variável digitando BeautifulSoup(variaveldesejada, 'html.parser')


# c) Utilize o código abaixo para iterar nas linhas e colunas da tabela e preencher a variavel conteudo_extraido

# c) Utilize o código abaixo para iterar nas linhas e colunas da tabela e preencher a variavel conteudo_extraido

conteudo_extraido = []

tabela = pagina.find('table', {'class': 'chart'})

for linha in tabela.find_all('tr'):
  textos_coluna = list()  

  for coluna in linha.find_all('td'):
    texto_coluna = coluna.get_text().strip().split('\n')
    textos_coluna += texto_coluna
  conteudo_extraido.append(textos_coluna)

conteudo_extraido.pop(0)
conteudo_extraido = list(map(lambda i : [i[1].replace('.', ''),i[2].strip(),i[3].replace('(', '').replace(')', ''),i[4]], conteudo_extraido))

print(conteudo_extraido)

# d) Escreva o arquivo imdb.csv com o conteudo da variavel conteudo_extraido

import csv

with open(file='imdb.csv', mode='w', encoding='utf8') as imdb_csv:
  imdb = csv.writer(imdb_csv, delimiter=';')
  imdb.writerows([['Ranking','Título','Ano','Nota']])
  imdb.writerows(map(lambda a : [a[0], a[1], a[2], a[3]], conteudo_extraido))

print('sucesso.')

