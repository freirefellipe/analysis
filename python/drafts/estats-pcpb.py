# Projeto baseado nos dados em csv fornecidos pelo site da PCPB, link https://sic.pb.gov.br/estatisticas/quantitativas

import pandas 

df_df = pandas.read_csv('pcpb-resumoanual-2023.csv', sep=',')

print(df_df)
