import pandas

df_market = pandas.read_csv('../data/supermarket.csv')

# É possível adicionar uma primeira coluna com sequência númérica como índice, caso ela não tenha sido feita.

a = df_market.reset_index(inplace=True) # a maioria das funções no pandas vem com o método 'inplace', feito para gravar a modificação no dataframe original, mas não no arquivo original. NOTE que se ele modifica o df original, um print dessa ação não vai retornar nada.

b = df_market.set_index('index') # Escolhe qual vai ser o index do dataframe:

print(df_market)
print(a)
print(b)

