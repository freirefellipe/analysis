# https://www.pythontutorial.net/python-basics/python-write-csv-file/


eta = [44,22,63,21,27]

elenco = []

while data != 'stop.':
   data = str(input('Insira os dados, e digite "stop." para parar: '))
   elenco.append(data)

with open(file=nome_nuovo_file, mode='w', encoding='utf8') as fp:

 riga = 'Età' + '\n' # cria uma linha para servir de cabeçalho;
 fp.write(riga) # envia a linha recém criada para o arquivo recém criado e apelidado;
  
 for x in eta:  # começa a inserir cada ítem da lista no novo arquivo .csv usando o 'for...in' para mudar o conteúdo da linha a cada repetição;
  riga = str(x) + '\n' # transforma o novo conteúdo em String e quebra a linha para inserção da próxima; 
  fp.write(riga) # insere a nova linha no documento .csv;
 
