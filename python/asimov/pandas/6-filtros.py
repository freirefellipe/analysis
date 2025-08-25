import pandas
from numpy.random import randn

dataframe = pandas.DataFrame(data=randn(4, 4), index=['1','2','3','4'], columns='A B C D'.split())

print(dataframe)

# Para se trabalhar com MATRIZES, há alguns recursos de .iloc[], como por exemplo:

a = dataframe.iloc[1:3, 1:3] # o número final fica de fora.

# Posso pedir para que o programa informe True or False para determinada condição:

b = dataframe > 0

# Nessa lógica, é possível pedir para que o pandas retorne somente valores na condição imposta:

c =  dataframe[dataframe > 0]

d = dataframe['B'] > 0

# Inclusive criar um novo Dataframe somente com dados resultantes de uma condição imposta: 

e = dataframe[dataframe['C'] > 0]

f = dataframe[(dataframe['B'] > 0) & (dataframe['D'] > 0)]

print(e)
print(f)

