import random

import libras_dicionario #importa módulo (arquivo) com vocabulário de libras em formato de listas

# sortear uma palavra de cada lista.
frase = f"{random.choice(libras_dicionario.verbo)}, {random.choice(libras_dicionario.substantivo)}, {random.choice(libras_dicionario.pronome)}, {random.choice(libras_dicionario.adjetivo)}, {random.choice(libras_dicionario.adverbio)}"

print(frase)
