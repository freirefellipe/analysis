import requests
from requests.exceptions import HTTPError


def crawl_website(url: str) -> str:

	try:
		resposta = requests.get(url)
		resposta.raise_for_status()
	except HTTPError as exc:
		print(exc)
	else:
		conteudo = resposta.text

	return conteudo

