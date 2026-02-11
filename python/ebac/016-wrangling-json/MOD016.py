# imported: json, pandas


# with localfile .json open
# make a var with the first element of the whole file
# each element has a dict which you can select its keys

# OPEN LOCAL JSON FILE 
import json

with open (file='deliveries.json' , mode='r', encoding='utf8') as localfile:
    file_ = json.load(localfile) # o load carrega todo o arquivo. O loads carrega apenas texto
    sample = file_[0]
    print(sample.keys()) # peguei somente um elemento pra poder exibir o cabeçalho
    #print(sample['origin']['lat']) # colchetes seguidos pq tem dicionário dentro de dicionário


# WRANGLING 
#USING PANDAS TO LOAD A DATAFRAME
import pandas

deliver_df = pandas.DataFrame(file_)
print(deliver_df.head(20))

# aqui inicio desaninhamento de dicionários dentro de uma coluna, utilizando o pandas.json_normalize()

deliver_origin = pandas.json_normalize(deliver_df['origin']) # o pandas.json_normalize() já serve para tirar o formato de diciodndário dentro de um df, e transformá-lo também em df
deliver_merged = pandas.merge(left=deliver_df, right=deliver_origin, how='inner', left_index=True, right_index=True)

print(deliver_merged)

deliver_exploded = deliver_df[["deliveries"]].explode("deliveries") # o explode deve ser feito lá no df antes do normalized. Seleciona a coluna e comanda .explode(<coluna>) para tirar o formato de dicionário de dentro da coluna.

print(deliver_exploded)

deliver_normal = pandas.concat([
  pandas.DataFrame(deliver_exploded["deliveries"].apply(lambda record: record["size"])).rename(columns={"deliveries": "delivery_size"}),
  pandas.DataFrame(deliver_exploded["deliveries"].apply(lambda record: record["point"]["lng"])).rename(columns={"deliveries": "delivery_lng"}),
  pandas.DataFrame(deliver_exploded["deliveries"].apply(lambda record: record["point"]["lat"])).rename(columns={"deliveries": "delivery_lat"}),
], axis= 1)

print(deliver_normal)

deliver_final = pandas.merge(left=deliver_merged, right=deliver_normal, how='right', left_index=True, right_index=True)

print(deliver_final)

# remember to add 'axis=1' when dropping a column.
deliver_final = deliver_final.drop('origin', axis=1) 
deliver_final = deliver_final.drop('deliveries', axis=1)

# organizing the columns
deliver_final = deliver_final[['name','region', 'lng', 'lat', 'vehicle_capacity', 'delivery_size', 'delivery_lng', 'delivery_lat']]
deliver_final.rename(columns={'lng': 'hub_lng' , 'lat':'lat_hub'}, inplace=True) # se usa dicionário para renomear colunas, escrevendo o nome antigo, e o nome desejado em cada chave-valor

print(deliver_final)

