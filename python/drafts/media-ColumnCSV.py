from functools import reduce

import modules.ColumnCSV


coluna_limpa = map(lambda dado: dado.replace('R$',''), modules.ColumnCSV.coluna) # pegar a lista com os valores em reais e remover cifras dos valores;
coluna_integer = map(lambda dado: int(dado), coluna_limpa) # transformar os elementos em integer;
coluna_media = reduce(lambda dado_1, dado_2: dado_1 + dado_2, coluna_integer) / len(modules.ColumnCSV.coluna) # calcular a média;

print(coluna_media)
