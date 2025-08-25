# DOWNLOAD DO PACOTE DESEJADO

import wget 

 # baixando e escolhendo seu nome;

wget.download(url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip', out='dados.zip')

 # descompactação do pacote com 'import zipfile';

import zipfile

with zipfile.ZipFile('dados.zip','r') as zipack:
  zipack.extractall('unzipack')

 # encontrar o documento de conteúdo separado por vírgulas e, se necessário, renomeá-lo para o formato .csv usando 'import os';

import os

os.rename('./unzipack/dow_jones_index.data', './dow_jones_index.csv')


# PROCESSAMENTO DOS DADOS COM PANDAS

import pandas

  # criar uma variável que leia documento csv com o método read_csv;

dow_jones_table = pandas.read_csv('dow_jones_index.csv')
print(dow_jones_table)

for column in dow_jones_table.columns.to_list():
  print(column)

 # escolher linhas e colunas específicas da tabela para fazer uma subtabela, uma tabela interior (ESPERO UM DIA ENTENDER ESSES DOIS CÓDIGOS);

dow_jones_table_MCD = dow_jones_table[dow_jones_table['stock'] == 'MCD']
print(dow_jones_table_MCD)

dow_jones_table_MCD = dow_jones_table_MCD[['date','open','high','low','close']]
print(dow_jones_table_MCD)

 # remover o cifrão dos dados em str de colunas específicas usando o método .apply() para poder usar uma função anônima(lambda, nesse caso);

for celula in ['open','high','low','close']:
  dow_jones_table_MCD[celula] = dow_jones_table_MCD[celula].apply(lambda i: float(i.split(sep='$')[-1]))

 # o processo também pode ser dividido em duas partes, removendo o cifrão primeiro, depois indo nas colunas específicas para transformá-las em float;

#for cell in dow_jones_table_MCD:
#  if ('$' in dow_jones_table_MCD[cell] == True):
#    dow_jones_table_MCD[cell].apply(lambda dado: dado.replace('$', ''))
#    dow_jones_table_MCD[cell] = float(dow_jones_table_MCD[cell])


print(dow_jones_table_MCD)

# VISUALIZAÇÃO DOS DADOS COM SEABORN

import seaborn

 # cria um gráfico de x e y relacionando uma das colunas ao longo do tempo;

plot = seaborn.lineplot(x="date", y="open", data=dow_jones_table_MCD)
_ = plot.set_xticklabels(labels=dow_jones_table_MCD['date'], rotation=90)

 # cria mais um gráfico de x e y relacionando outra coluna ao longo do tempo;

plot = seaborn.lineplot(x="date", y="close", data=dow_jones_table_MCD)
_ = plot.set_xticklabels(labels=dow_jones_table_MCD['date'], rotation=90)

 # cria mais um gráfico de x e y dessa veze com todas as colunas da tabela específica extraída anteriormente;

plot = seaborn.lineplot(x="date", y="value", hue='variable', data=pandas.melt(dow_jones_table_MCD, ['date']))
_ = plot.set_xticklabels(labels=dow_jones_table_MCD['date'], rotation=90)

 # cria uma imagem do último gráfico gerado a partir de todos os outros anteriores.

plot.figure.savefig('McDonalds-chart.png')
