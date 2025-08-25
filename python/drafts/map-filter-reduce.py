### MAP

print('-') # ESEMPIO 1

numeros = [2,3,4]
numeros_quadrados = map(lambda numero:numero**2, numeros) # o método map precisa ter a informação da função a ser realizada e da coleção que vai ser utilizada respectivamente.

print(list(numeros_quadrados)) # foi usado aqui o método lista porque "os dados retornados ainda estão brutos", segundo o professor.

print('-')  # ESEMPIO 2

emails = ['freirefellipe@gmail.com','freirefellipe@outlook.com','lipeoliv@mail.com']

extrai_nome_usuario = lambda email: email.split(sep='@')[0]

nomes_usuario = list(map(extrai_nome_usuario, emails)) # nesse caso, para efeito de ilustração, a função lambda ganhou nome com uma variável. Mas, em geral, a função lambda vai dentro da map para que continue 'anônima', sendo mais prático.

print(nomes_usuario)

print('-')  # ESEMPIO 3 (mesmo do esempio 2, mas sem criar variável para o lambda)

emails = ['freirefellipe@gmail.com','freirefellipe@outlook.com','lipeoliv@mail.com']

extrai_nomes_usuario = list(map(lambda email: email.split(sep='@')[0], emails))

print(extrai_nomes_usuario)


### FILTER

emails_list = ['freirefellipe@gmail.com', 'lipefreioliv@gmail.com', 'freirefellipe@outlook.com', 'lipeoliv@mail.com']

# 1st way to go:

emails_gmail_1 = []

for email in emails_list:
    if '@gmail' in email:
        emails_gmail_1.append(email)

# 2nd, BEST, way to go, by not creating variable for the lambda function:

emails_gmail_2 = list(filter(lambda email: '@gmail' in email, emails_list)) # impressindível colocar em list(), senão vai retornar somente uma mensagem de espaço alocado na memória.


'-------------------------------'

print(emails_gmail_2)


### REDUCE


print('-') # ESEMPIO 1

elenco = [5, 3, 4]

from functools import reduce # reduce não é nativo do python. Precisa importar.

ridurre = reduce(lambda x, y: x*y, elenco)

print(ridurre)

print('-') # ESEMPIO 2

from random import random #

spazio_campionario = [int(100*random()) for _ in range(0, 10)] # cria uma variável de lista e, dentro, usa o 'random' para mandar sortear um número dentro de um intervalo cem vezes usando o 'for .. in range'.

print(spazio_campionario)

from functools import reduce #

def confrontando_due_valori(a: int, b: int) -> int:
    return a if a > b else b

ridurre = reduce(confrontando_due_valori, spazio_campionario)
print(ridurre)

print('-') # ESEMPIO 3

from random import random

espaco_amostral = [int(100*random()) for _ in range(0,10)]

print(espaco_amostral)

from functools import reduce

maior_valor_amostral = reduce(lambda a, b: a if a > b else b, espaco_amostral)
menor_valor_amostral = reduce(lambda a, b: a if a < b else b, espaco_amostral)

print(f'O maior valor amostral é {maior_valor_amostral}, e o menor valor amostral é {menor_valor_amostral}.')


