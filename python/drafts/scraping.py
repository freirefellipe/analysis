import requests
from bs4 import BeautifulSoup

pagina = BeautifulSoup(open('lotr.html', mode='r'), 'html.parser') # carrega a página. dentro dos parênteses: documento, modo, parse

filmes_li = pagina.find_all('li') # explora pela informação desejada com find_all na página. Faz lista com as informações dentro da lista

filmes_lista = []

for filme_li in filmes_li:
	filmes = filme_li.get_text().split(sep=':') # retirar o texto do meio das tags
	ano = filmes[0]
	titulo = filmes[1] + ':' + filmes[2]
	filmes_lista.append({'Ano': ano ,'Título': titulo}) 

print(filmes_lista)

########################

import requests
from bs4 import BeautifulSoup

from crawl_website import crawl_website


URL2 = 'https://en.wikipedia.org/wiki/Web_crawler' # declarar o website
contenido = crawl_website(url=URL2) # buscar na net e converter o site em uma variável com o craw_website

with open(file='wiki.html', mode='w', encoding='utf8') as fp: # grava em um documento local o conteúdo da página.
	fp.write(contenido)
	pagina = BeautifulSoup(open('wiki.html', mode='r'), 'html.parser') # ler o conteúdo do documento html
	pagina_texto = pagina.get_text() # remover as tags da página com get_text


import re


incidencias = len(re.findall('crawler', pagina_texto, re.IGNORECASE)) # buscar fraseado desejado. Maior feature: re.IGNORECASE
print(incidencias)
 
