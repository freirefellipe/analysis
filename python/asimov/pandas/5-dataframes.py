import pandas
from numpy.random import randn # esse pacote forja tabelas de tamanho desejado e com dados aleatórios.

dataframe = pandas.DataFrame(data=randn(4, 5), index=['1','2','3','4'], columns='A B C D E'.split()) # no 'randn', deve-se determinar, nos parenteses, primeiro índice e depois coluna.

a = dataframe[['A']] # um colchete só retorna somente como series com seus respectivos detalhes. Dois colchetes retorna em formato de dataframe e mais colunas podem ser inclusas.

a1 = dataframe.A # outra forma de exibir uma coluna específica.

# É possível inserir novos dados nos dfs da seguinte forma:

b = dataframe['F'] = dataframe['B']

c = dataframe['F'] = dataframe['A'] + dataframe ['B']

# Para remover colunas:

del dataframe['F']

# Para colunas ou linhas, é possível utilizar o comando .drop(<coluna ou linha alvo>, axis=<0 pra linha, ou 1 pra coluna>)

d = dataframe.drop('1', axis=0)

# se quiser modificar o dataframe original, deve-se incluir o comando inplace=True dentro da função .drop()

# Caso queira retornar os valores de um índice (linha), deve-se usar o modo .loc['<nomedalinha>']. Uma transposição será feita, e o que era linha será exibido como uma coluna; ou, se colocando dois colchetes, será exibido em forma de dataframe novamente. Com dois colchetes é possível solicitar mais de uma linha. Após a vírgula, qualquer comando se referirá a uma coluna desejada.

e = dataframe.loc[['2', '3'], ['A']]

# Se quiser selecionar apenas um valor específico do dataframe, o .iloc[<num_da_linha>, <num_da_coluna>] faz o trabalho. 

f = dataframe.iloc[0, 0]

print(dataframe, '\n')

print(f'Retornando valores de 2 índices (linhas) de determinada coluna: \n {e}')
print(f'Utilizando o iloc() para pegar apenas um dado do dataframe: {f}')
