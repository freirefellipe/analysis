import requests
from requests.exceptions import HTTPError


def crawl_website(url: str) -> str:

	try:
		resposta = requests.get(URL)
		resposta.raise_for_status()
	except HTTPError as exc:
		print(exc)
	else:
		conteudo = resposta.text

	print(conteudo)


URL = str(input('URL: '))

conteudo = crawl_website(url=URL)
