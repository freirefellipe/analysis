# É possível ir à página de um site e extrair dele a tabela desejada para transformá-la em dataframe, tudo com o pandas. 
# fonte: https://www.youtube.com/shorts/xlXO41SuG3E

import pandas

URL = 'https://pt.wikipedia.org/wiki/Lista_das_maiores_empresas_do_Brasil'

empresas_wiki_page = pandas.read_html(URL)

#empresas_geral = pandas.DataFrame(empresas_wiki_page[0])

print(empresas_wiki_page[0])


