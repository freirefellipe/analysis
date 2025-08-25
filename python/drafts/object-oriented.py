# A programação em Python segue outro paradigma além do script (que se propõe a resolver um problema em linhas sequencialmente cadenciadas) chamada de ORIENTAÇÃO A OBJETOS. É uma forma de programar objetos cheios de características (chamadas atributos) e funções (chamadas métodos) para que, quando solicitadas, façam suas tarefas, e não necessariamente numa ordem preordenada como acontece com os scripts. Exemplo de programação orientada a objetos é a programação para controle remoto, ou personagens de videogame.

class PersonagemControlavel:
   def __init__(self, nome_dele, classe_dele, arma_dele): # Métodos com nomes entre underscores se chamam métodos mágicos. 
      self.nome = nome_dele
      self.classe = classe_dele
      self.armas = ['espada','arco e flecha']
      if arma_dele in self.armas:
         self.arma = arma_dele
      else:
         print('Essa arma não existe nesse universo.')
   
   def action(self, botao):
      if botao == 'a':
         print(f'{self.nome} atacou.')
      elif botao == 'b':
         print(f'{self.nome} defendeu-se.')
      elif botao == 'x':
         print(f'{self.nome} pulou.')
      elif botao == 'y':
         print(f'{self.nome} usou seu especial.')
         
liam = PersonagemControlavel(nome_dele='Liam', classe_dele='Druída', arma_dele='Palavras')
neeson = PersonagemControlavel(nome_dele='Neeson', classe_dele='Guerreiro', arma_dele='Arco e Flecha')

liam.action(str(input('Botão: ')))

neeson.action(str(input('Botao: ')))


### ESEMPIO 2

from time import sleep

class Pessoa(object):
  def __init__(self, nome_dele: str, idade_dele: int, documento_dele: str = None): # o None no argumento 'documento_dele' está predefinindo um valor caso falte.
    self.nome = nome_dele
    self.idade = idade_dele
    self.documento = documento_dele

  def dormir(self, horas: int) -> None: # criar um loop que vai contar as horas.
    for hora in range(1, horas+1):
      print(f'Dormindo há {hora} hora(s).')
      sleep(1)

  def falar(self, texto: str) -> None:
    print(texto)

  def __str__(self) -> str:
    return f'{self.nome}, {self.idade} anos e documento número {self.documento}'
    

fellipe = Pessoa(nome_dele='Fellipe', idade_dele=15, documento_dele='99001199764')
victor = Pessoa(nome_dele='Victor', idade_dele=33, documento_dele='65292387')
escore_credito = {'99001199764':958,'65292387':938 }

print(victor)
fellipe.dormir(3)

# Criar uma função para comparar a idade de uma pessoa e constar se tem mais de dezoito anos;
# criar uma entrada para o usuário inserir a idade;
# comparar as idades.

def maior_idade(i: int) -> bool:
  return i >= 18

fellipe.idade = int(input('Idade: '))

if maior_idade(fellipe.idade):
  print(f'{fellipe.nome} tem {fellipe.idade} anos, e é maior de idade.')
else:
  print(f'{fellipe.nome} tem {fellipe.idade} anos, não é maior de idade.')


print('Seu escore de crédito é:', escore_credito[fellipe.documento])

print(fellipe)

### ESEMPIO 3

class PersonagemFicticio:
  def __init__(self, nome_dele, classe_dele, arma_dele):
    self.nome = nome_dele
    self.classe = classe_dele
    self.arma = arma_dele

personagens_dicio = [
  {'Nome':'Ryan', 'Classe':'Guerreiro', 'Arma':'Escudo'}, 
  {'Nome':'Rob', 'Classe':'Druída', 'Arma':'Natureza'},
  {'Nome':'Lycan', 'Classe':'Cantor', 'Arma':'Grito Agudo'},
  {'Nome':'Malon', 'Classe':'Ladrão', 'Arma':'Chave-mestra'}]

Ryan = PersonagemFicticio(personagens_dicio[0]['Nome'], personagens_dicio[0]['Classe'], personagens_dicio[0]['Arma'])
Malon = PersonagemFicticio(personagens_dicio[1]['Nome'], personagens_dicio[1]['Classe'], personagens_dicio[1]['Arma'])

x = Malon.classe

print(x)

### ESEMPIO 4

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


### ESEMPIO 5

class ClasseUm(object):

   def __init__(self, nome_doc: str):
      self.nome = nome_doc
      self.conteudo = self._extrair_conteudo()
      self.colunas = self._extrair_nome_colunas()
   
   def _extrair_conteudo(self):

      conteudo = None

      with open (file=self.nome, mode='r', encoding='utf8') as doc:
         
         conteudo = doc.readlines()
         return conteudo 

   def _extrair_nome_colunas(self):
     return self.conteudo[0].strip().split(sep=',')


dados_csv = ClasseUm(nome_doc='dados.csv')

doc_escolhido = input('Documento: ')

if doc_escolhido == 'carros.csv':
   print(ClasseUm(nome_doc='carros.csv').colunas)
   
elif doc_escolhido == 'dados.csv':
   print(ClasseUm(nome_doc='dados.csv').colunas)

# print(doc_escolhido.conteudo)


### ESEMPIO 6

class DocumentoCSV(object):

  def __init__(self, nome_documento: str):
    self.documento = nome_documento
    self.conteudo = self._copiar_documento()
    self.colunas = self._mostrar_colunas()

  def _copiar_documento(self): # copiando documento inteiro, sem dicionários em listas.
    
    conteudo = None

    with open (file=self.documento, mode='r', encoding='utf8') as doc:
       conteudo = doc.readlines()
       return conteudo

  def _mostrar_colunas(self):
    return self.conteudo[0].strip().split(sep=',')

  def coluna_documento(self, indice_coluna: str): # Essa função não precisou estar ligada aos atributos do objeto. Talvez por ter argumento.

    coluna_extraida = list()

    for linha in self.conteudo:
       coluna = linha.strip().split(sep=',')
       coluna_extraida.append(coluna[indice_coluna])
    coluna_extraida.pop(0)
    return coluna_extraida

#  def _copiar_documento(self): # com dicionários em listas.
#
#    self.documento_copiado = []
#
#    with open (file=self.documento, mode='r', encoding='utf8') as doc:
#      header = doc.readline().strip().split(sep=',')
#      line = doc.readline()
#
#      while line:
#        datum = line.strip().split(sep=',')
#        dicio = {}
#        for indice in range (len(header)):
#          dicio[header[indice]] = datum[indice]  
#        self.documento_copiado.append(dicio)
#        line = doc.readline()
#      return self.documento_copiado


documento_csv = DocumentoCSV(nome_documento='dados.csv')

print(f'Conteúdo: {documento_csv.conteudo}')
print(f'Colunas: {documento_csv.colunas}')

coluna_3 = documento_csv.coluna_documento(indice_coluna=2)

print(f'Coluna 3: {coluna_3}')


### ESEMPIO 7

class DocumentoCSV(object):

  def __init__(self, nome_documento: str):
    self.documento = nome_documento
    self.conteudo = self._copiar_documento()
    self.colunas = self._mostrar_colunas()

  def _copiar_documento(self): # copiando documento inteiro, sem dicionários em listas.
    
    conteudo = None

    with open (file=self.documento, mode='r', encoding='utf8') as doc:
       conteudo = doc.readlines()
       return conteudo

  def _mostrar_colunas(self):
    return self.conteudo[0].strip().split(sep=',')

  def coluna_documento(self, indice_coluna: str): # Essa função não precisou estar ligada aos atributos do objeto. Talvez por conter argumento.

    coluna_extraida = list()

    for linha in self.conteudo:
       coluna = linha.strip().split(sep=',')
       coluna_extraida.append(coluna[indice_coluna])
    coluna_extraida.pop(0)
    return coluna_extraida

#

class OutroDocumento(DocumentoCSV):
   
   def __init__(self):
      super().__init__(documento, conteudo, colunas) # No Google Colab o argumento não pode ter o tipo especificado, ou deixa de ser reconhecido como classe pai.
#     self.copia = self.copiar_documento()
   
   def copiar_documento(self): # com dicionários em listas.

      documento_copiado = []

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

#    

documento_csv = DocumentoCSV(nome_documento='dados.csv')

print(f'Conteúdo: {documento_csv.conteudo}')
print(f'Colunas: {documento_csv.colunas}')

coluna_3 = documento_csv.coluna_documento(indice_coluna=2)

print(f'Coluna 3: {coluna_3}')

outro_documento = OutroDocumento('dados.csv')
print(outro_documento._copiar_documento)


