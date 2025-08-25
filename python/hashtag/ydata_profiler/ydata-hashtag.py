# importar pandas e o pacote ydata_profile
import pandas
from ydata_profiling import ProfileReport

# criar link para o arquivo .csv
DATA = './employee_attrition.csv'

dataframe = pandas.read_csv(DATA)

# print(dataframe.head())
# print(dataframe.info()) #exibe as colunas em forma de lista

profile = ProfileReport(dataframe) # chama a classe anteriormente importada para criar uma arquivo .html com detalhamento completo

profile.to_file('./hashtag/eda.html') # precisa ser em html. 


# CORRELAÇÃO entre colunas é sobre se elas são diretamente proporcionais (correlação positiva) ou viceversa.
# O tipo CATEGÓRICO de variável é um tipo que não contém número nem booleano, e têm mais que 2 valores únicos, que são importantes para que se possam ser feitos grupamentos com o comando groupby ou pivot table, por exemplo.
