print ('-'*20) ################# EXEMPLO 1
# leitura do arquivo completo.

arquivo_fonte = './dados.csv' # colocar aqui o endereço  do arquivo a ser lido.
var_arquivo_fonte = [] # variável onde vão ser colocadas as linhas a serem lidas. É uma boa pŕatica criar antecipadamente a variável, mesmo que ainda não vá receber valor.

with open (file=arquivo_fonte, mode='r', encoding='utf8') as fp:
  var_arquivo_fonte = fp.read()

print(var_arquivo_fonte)

print ('-'*20) ################# EXEMPLO 2
# leitura de um arquivo linha por linha, já que a leitura do arquivo completo pode pesar demais.

arquivo_fonte = './dados.csv' 
var_arquivo_fonte = []

with open (file=arquivo_fonte, mode='r', encoding='utf8') as fp:
  linha = fp.readline()
  
  while linha:
    var_arquivo_fonte.append(linha) # importante lembrar desse passo de inserir a linha com os dados na nova variável
    linha = fp.readline()

print(var_arquivo_fonte)

print('-'*20)

for linha in var_arquivo_fonte:
   print (linha)


print ('-'*20) ################# EXEMPLO 3

# TRANSFERINDO DADOS DE ARQUIVO .CSV PARA DICIONÁRIOS DENTRO DE LISTAS, INDEXANDO COLUNAS 

dati = [] # crio uma lista para colocar os dados desejados

with open (file='dados.csv', mode='r', encoding='utf8') as arquivo: # chamo o arquivo a ser lido

    header = arquivo.readline().strip().split(sep=',') # transformo o cabeçalho em uma variável

    riga = arquivo.readline() # leio a próxima linha com dados importantes

    while riga: # crio um loop para repetir a criação de dicionários e inclusão na variável inicial

       collona_dati = riga.strip().split(sep=',') # separar o texto em dados

       riga_dizio = {} # criar um dicionário vazio

# incluir os dados provindos do texto no dicionário, relacionando chave (o cabeçalho de antes) e valor (os elementos provindos do texto) corretamente

       riga_dizio[header[0]] = collona_dati[0]

       riga_dizio[header[1]] = collona_dati[1]

       riga_dizio[header[2]] = collona_dati[2]

       riga_dizio[header[3]] = collona_dati[3]

       dati.append(riga_dizio) # adicionar o dicionário na lista do início

       riga = arquivo.readline() # ler a próxima linha

for dato in dati:
    print(dato)


print ('-'*20) ################# EXEMPLO 4 (FALTA RESOLVER)

class DocumentoCSV(object):

  def __init__(self, nome_documento):
    self.documento = nome_documento
    self.conteudo = self._copiar_documento()
#   self.coluna = self._coluna_documento()

  def _copiar_documento(self):

    self.documento_copiado = []

    with open (file=self.documento, mode='r', encoding='utf8') as doc:
      header = doc.readline().strip().split(sep=',')
      line = doc.readline()

      while line:
        datum = line.strip().split(sep=',')
        dicio = {}
        for indice in range (len(header)):
          dicio[header[indice]] = datum[indice]  
        self.documento_copiado.append(dicio)
        line = doc.readline()
      return self.documento_copiado

#  def _coluna_documento(self, coluna_documento):
#
#    self.coluna_extraida = []
#    
#    for i in self.documento_copiado:
#       self.coluna_extraida.append(self.documento_copiado[i][coluna_documento])
#    return self.coluna_extraida

documento_csv = DocumentoCSV(nome_documento='dados.csv')

print(documento_csv.conteudo)

#coluna_1 = [documento_csv.conteudo[0]['coluna_1'], documento_csv.conteudo[1]['coluna_1'], documento_csv.conteudo[2]['coluna_1'], documento_csv.conteudo[3]['coluna_1']]

print(coluna_1)

