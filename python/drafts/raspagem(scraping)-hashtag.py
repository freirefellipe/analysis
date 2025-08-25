import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'} # vai em código-fonte > network > clica em qualquer dos links e vai na última informação 'user-agent'

URL = 'https://www.google.com/search?channel=fs&client=ubuntu-sn&q=cota%C3%A7%C3%A3o+d%C3%B3lar'

requests_text = requests.get(URL, headers=header).text # mostra o codigo-fonte da página html, O headers='' é para que o site entregue mais informações baseadas no navegador, não somente no python. Com isso é possível digitar dois argumentos futuramente no método .find();

page_bs4 = BeautifulSoup(requests_text, 'html.parser') # entrega o mesmo resultado que o requests.get().text, mas o bs4 tem mais funcionalidades.

organize_page = page_bs4.prettify() # prettify() deixa o html formatado com layout original.

print(page_bs4.find_all('input')[4]) # escolhe a Tag que quer ver em seu total de resultados. Pode colocar índice para exibir somente um deles.

dolar_quotation_tagged = page_bs4.find('span', class_='DFlfde SwHCTb') # mostra o conteúdo dentro da Tag escolhida. class_ com underscore para diferenciar da palavra reservada do python;

dolar_get_text = round(float(dolar_quotation_tagged.get_text().replace(',','.')),2)
print(dolar_get_text)

dolar_quotation = round(float(dolar_quotation_tagged['data-value']), 2)
print(dolar_quotation)

