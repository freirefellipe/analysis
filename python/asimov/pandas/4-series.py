import pandas
import numpy

lis_filhos = ['thiago', 'fellipe', 'victor']

lis_pais = ['deraldo', 'fatima']

lis_eta = ['40','38','35']

lis_age = ['70','68']

dic = dict(
	thiago='40',
	fellipe='38',
	victor='35'
	)

dictionary = {
				'thiago':'40',
				'fellipe':'38',
				'victor':'35'
				}

ser = pandas.DataFrame(dictionary, index=None)

ser1 = pandas.Series(data=lis_eta,index=lis_filhos)

ser2 = pandas.Series(data=lis_age,index=lis_pais)

a = pandas.Series(lis_filhos) # comando que faz com que cada elemento da variável seja uma coluna (Serie) do dataframe.
b = pandas.Series(data=lis_eta, index=lis_filhos)

c = ser1[['thiago', 'victor']] #precisa duplicar os colchetes para poder solicitar mais de uma coluna.

d = ser1 + ser2 # todos os objetos retornaram NaN.

# NOTE: "operações dentro do Pandas é orientado por índices"

print(dic)
print(a)
print(b)
print(ser1)
print(c)
print(d)
