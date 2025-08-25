# conferir o arquivo robots.txt.

import requests

URL1 = 'https://github.com/robots.txt'

gh_robots = requests.get(URL1).text

print(gh_robots)

# ir na página de trends do Github e pegar seu conteúdo.

from bs4 import BeautifulSoup

URL2 = 'https://github.com/trending'

gh_html_raw = BeautifulSoup(URL2, 'html.parser')

# filtrar o desejado
# transformar em texto
# criar uma tabela completa em .csv com o cabeçalho: ranking; project; language; stars; stars_today; forks
