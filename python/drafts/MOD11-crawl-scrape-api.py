# WEB CRAWLING (https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods). Aqui se aprende a usar o método .get() do pacote requests.

import requests
from requests.exceptions import HTTPError

def crawl_website(url:str) -> str:

  try: # comando para ver se a página está lá
    resposta = requests.get(url)
    resposta.raise_for_status()
  
  except HTTPError as exc: # comando para caso a página não esteja lá
    print(exc)

  else: # caso esteja tudo bem, pegar o texto
    resposta_texto = resposta.text
    return resposta_texto

  # é possível resumir todas as linhas acima em uma só, fazendo: variavel = requests.get('url da página').text


# WEB SCRAPING . Aqui se usa o BeautifulSoup para remover as tags provindas da página html, e filtrar a página pela informação desejada mais específica

from bs4 import BeautifulSoup

conteudo_wiki = crawl_website(url='https://en.wikipedia.org/wiki/Main_Page')

with open (file='wiki.html', mode='w', encoding='utf8') as fp: # transformar o conteúdo em um documento local html
    wiki_local = fp.write(conteudo_wiki)

wiki_html = BeautifulSoup(open('wiki.html', mode='r'), 'html.parser') # pegar o documento local de volta para o python

 # incluir uma linha com .find_all() aqui ou .find(), sabendo que .find_all() é pra quando tem mais de uma incidência para ser encontrada.

wiki_clean = wiki_html.get_text() # para retirar as tags, usa-se o método .get_text()
print(wiki_clean)

import re

occur = re.findall('wikipedia', wiki_clean, re.IGNORECASE) # o re.findall() requer no mínimo dois argumentos: palavra buscada e variável a buscar palavra.

print(f'A palavra "wikipedia" apareceu {len(occur)} vezes') if occur else print(f'A pesquisa por "wikipedia" não retornou nenhum resultado.')


# WEB API. Faz o mesmo que web crawling, mas com mais facilidade, utilizando-se de API no formato JSON

import json

URL = 'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'

pagina = crawl_website(url=URL)

json.dumps(pagina, indent=2, ensure_ascii=False) # .dumps() requer no mínimo 1 argumento, o dp conteúdo a ser carregado na var do python. Indentação e ASCII (False/True para acentos) é opcional.

with open (file='taxa.json', mode='w', encoding='utf8') as fp:
    fp.write(pagina)

  # .load() - sem o S - carrega documento .json LOCAL de volta ao python em forma de dicionário. .loads() - com o S - faz a mesma coisa, mas dirieto do python, sem arquivo local.

taxa_json = json.load(open(file='taxa.json', mode='r')) 
print(taxa_json)

taxa = json.loads(pagina) 
cdi = float(taxa_json['taxa'].replace(',', '.'))
print(cdi)
