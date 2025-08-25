
# VISUALIZAÇÃO

# o Seaborn trabalha com polegadas


def polegadas(a):
  return a * 2.54

import seaborn

a = seaborn.get_dataset_names() # busca datasets já preparados para estudo

tips_df = seaborn.load_dataset('tips')

c = tips_df.head()

d = seaborn.relplot(data=tips_df, x='total_bill', y='tip', hue='day', style='day', palette='dark') # palette: dark ou pastel

#e = seaborn.relplot(data=b, x='total_bill', y='tip', hue='day', style='day', col='time', row='sex') # .relplot() cria um gráfico de pontos coloridos. col='' e row='' separam gráficos de acordo com o número de itens da coluna escolhida. style='' dá uma forma diferente para cada item da coluna escolhida

'-------------------------------------------------------------------------------------------------------------------------------------------------'

# ELEMENTOS (Títulos e eixos. Alterar textos no gráfico com ajuda do matplotlib)

#d.axes.set_title("Gorjetas", fontsize=12, fontweight="bold"); # Título
d.set_xlabels("Valor da conta (USD)", fontsize=10); # horizontal
d.set_ylabels("Valor da gorjeta (USD)", fontsize=10); # vertical
d.legend.set_title('Dias da semana', prop={'size':10, 'weight':'bold'}) # Edita as informações no canto direito do gráfico.
polegadas = d.fig.set_size_inches(w=polegadas(4), h=polegadas(4)) # w = width | h = height

#d.savefig(fname='tips.png', bbox_inch='tight') # bbox_inch é para não cortar a imagem

'-------------------------------------------------------------------------------------------------------------------------------------------------'

# GRÁFICO EM BARRA (útil para variáveis categóricas, no qual um eixo será categoria, outro será número. O eixo com mais valores deverá ser sempre o 'y')

e = seaborn.barplot(data=tips_df, x='day', y='total_bill', errorbar=None, palette='pastel') # 'ci' tá defasado. Usar ao invés errorbar=None
 # é possível configurar o gráfico com somente a função set, e, dentro, indicar o desejado, assim como deixá-lo para dar nomes aos eixos e etc.
e.set(title='Esse aqui é um gráfico responsa.', xlabel='Dia da semana', ylabel='Valor da conta') 
e.get_figure().savefig(fname='barplot.png')

 # caso necessária mais uma variável a ser estudada, esta será o 'hue' (português: matiz, cor)

f = seaborn.barplot(data=tips_df, x='day', y='total_bill', hue='time', palette='pastel')
f.set(title='Valor da conta por dia e período da semana', xlabel='Dia da semana', ylabel='Valor da conta')
f.get_figure().savefig('barplot-hue.png')

'-------------------------------------------------------------------------------------------------------------------------------------------------'

# GRÁFICO DE PIZZA (Secondo me, é mias útil para se exibir divisões de uma TOTALIDADE. O pacote seaborn não tem pizza, e recomenda gráfico em barra instead, uma vez que é complicado estudar proporções com àngulos)

f = tips_df[['tip', 'day']].groupby('day').agg('sum').reset_index()
f['tip_percent'] = 100 * tips_df['tip'] / tips_df['tip'].sum() # espero um dia entender isso aqui melhor. Sei que cria uma nova série chamada 'tip_percent'.
print(f.head())


f.plot.pie(y='tip_percent', labels=f['day'])
 # f.get_figure().savefig('tip-pie.png') # Não sei por que não funcionou.



'-------------------------------------------------------------------------------------------------------------------------------------------------'

# GRÁFICO EM LINHA OU AREA (importante lembrar de que o eixo relacionado ao tempo decorrido deverá ter seus valores em ordem crescente ou decrescente)

 # LINHA

flights_df = seaborn.load_dataset('flights')

flights_df_ = flights_df.query('1955 <= year < 1960') # quero os anos entre 55 e 59.


 # g = flights_df.groupby('month').agg('sum').reset_index().head(10)

with seaborn.axes_style('whitegrid'): # cria um grid que facilita a leitura.
  h = seaborn.lineplot(data=flights_df_, x='month', y='passengers', hue='year', palette='pastel')
  h.set(title='Passageiros por mês', xlabel='Mês', ylabel='Passageiros') # o .set() vai cuidar dos nomes no gráfico.
  h.get_legend().set_title('ano')
  image = h.get_figure().savefig('flights.png')

print('Sucesso.')


 # AREA

import matplotlib.pyplot as plt

with sns.axes_style('whitegrid'):

  grafico = sns.FacetGrid(data=flights, palette="pastel")
  grafico.map(sns.lineplot, "year", "passengers")
  grafico.map(plt.fill_between, 'year', 'passengers', alpha=0.3) # Foi importado o matplotlib.pyplot para poder usar o .fill_between para preencher a area.
  grafico.set(title='Passageiros por ano', xlabel='Ano', ylabel='Passageiros');
  grafico.fig.set_size_inches(w=15/2.54, h=7.5/2.54)



# BOXPLOT


'PREÇO OUTLIER DOS DIAMANTES'

import seaborn

diamonds_ds = seaborn.load_dataset('diamonds')

with seaborn.axes_style('whitegrid'):

  diamonds_graph = seaborn.boxplot(x=diamonds_ds['price']) # o boxplot só precisa de uma coluna. Porém, é possível gerar o gráfico a partir de uma tabela completa.

  diamonds_graph.set(title='Preços dos diamantes', xlabel='Preço (USD)')


# CORRELAÇÃO: SCATTERPLOT


'CORRELAÇÃO PREÇO POR PESO DE CADA TIPO DE TRANSPARÊNCIA'

import seaborn

diamonds_ds = seaborn.load_dataset('diamonds')[['price', 'carat', 'clarity']].groupby('clarity').agg('mean')

with seaborn.axes_style('whitegrid'):

  diamonds_grapho = seaborn.scatterplot(data=diamonds_ds, x='price', y='carat', hue='clarity')

  diamonds_grapho.set(title='Correlação preço por peso dos tipos de transparência.', xlabel='Preço', ylabel='Peso')

  diamonds_grapho.get_legend().set_title('Transparência')



'DISTRIBUIÇÃO CONTÍNUA APROXIMADA DO PESO DOS CARROS'

# por tipos de carro

import seaborn

mpg_ds = seaborn.load_dataset('mpg')

with seaborn.axes_style('whitegrid'):

  mpg_grapho = seaborn.histplot(data=mpg_ds, x='weight', hue=len(mpg_ds['name']), palette='dark', kde=True)

  mpg_grapho.set(title='Distribuição contínua de peso dos carros em seus diversos tipos', xlabel='Peso', ylabel='Carros')

# por anos 

import seaborn

mpg_ds = seaborn.load_dataset('mpg')

with seaborn.axes_style('whitegrid'):

  mpg_grapho = seaborn.histplot(data=mpg_ds, x='weight', hue=mpg_ds['model_year'])

  mpg_grapho.set(title='Distribuição contínua de peso dos carros ao longo dos anos', xlabel='Peso', ylabel='Anos')



# CORRELAÇÃO: CALOR (precisa de três variáveis para fazer um gráfico tipo 3D)

import seaborn

flights_ds = seaborn.load_dataset('flights')

flights_pivot_ds = flights_ds.pivot('month', 'year', 'passengers') # pega duas séries da tabela para fazer uma correlação delas e a terceira variável.

flights_heat_ds = seaborn.heatmap(data=flights_pivot_ds, cmap='Spectral')

flights_heat_ds.set(title='Passageiros: mês por ano', xlabel='Ano', ylabel='Mês') # o método set edita nomes das legendas do gráfico

flights_heat_ds.get_figure().savefig('flights_heat.png')

print('Um gráfico .png com heatmap foi criado com sucesso.')

flights_heatnums_ds = seaborn.heatmap(data=flights_pivot_ds, cmap='Spectral', annot=True, fmt='d')

flights_heatnums_ds.set(title='Passageiros: mês por ano', xlabel='Ano', ylabel='Mês')

flights_heatnums_ds.figure.set_size_inches(w=20/2.54, h=10/2.54)

flights_heatnums_ds.get_figure().savefig('flights_heatnums.png')

print('Outro gráfico .png com heatmap detalhado foi criado com sucesso.')

