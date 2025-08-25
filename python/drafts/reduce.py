print('-') ## ESEMPIO 1

elenco = [5, 3, 4]

from functools import reduce # reduce não é nativo do python. Precisa importar.

ridurre = reduce(lambda x, y: x*y, elenco)

print(ridurre)

print('-') ## ESEMPIO 2

from random import random #

spazio_campionario = [int(100*random()) for _ in range(0, 10)] # cria uma variável de lista e, dentro, usa o 'random' para mandar sortear um número dentro de um intervalo cem vezes usando o 'for .. in range'.

print(spazio_campionario)

from functools import reduce #

def confrontando_due_valori(a: int, b: int) -> int:
    return a if a > b else b

ridurre = reduce(confrontando_due_valori, spazio_campionario)
print(ridurre)

print('-') ## ESEMPIO 3

from random import random

espaco_amostral = [int(100*random()) for _ in range(0,10)]

print(espaco_amostral)

from functools import reduce

maior_valor_amostral = reduce(lambda a, b: a if a > b else b, espaco_amostral)
menor_valor_amostral = reduce(lambda a, b: a if a < b else b, espaco_amostral)

print(f'O maior valor amostral é {maior_valor_amostral}, e o menor valor amostral é {menor_valor_amostral}.')

