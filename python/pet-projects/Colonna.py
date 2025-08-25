# ESSE PROGRAMA PERGUNTA QUAL A COLUNA DESEJADA DE UMA TABELA SEMI-ESTRUTURADA (TXT, CSV, ETC) PARA EXTRAI-LA E ENTREGAR O RESULTADO EM UMA LISTA
 # Necessita reparo no início, no que diz respeito à criação de classe. A função _colonna está funcionando perfeitamente.

class Colonna(object):

  def __init__(self, name_doc: str):
    self.name = name_doc
    self.colonna = self._colonna()
  
  def _colonna(self):

    column = []

    with open (file=name_doc, mode='r', encoding='utf8') as fp:
      header = fp.readline().strip().split(sep=',')

      print(header)

      column_entry = str(input('Qual o nome da coluna dentre as opções? >'))
      column_choice = header.index(column_entry)
      line = fp.readline()

      while line:
        data_wanted = line.strip().split(sep=',')[column_choice]
        column.append(data_wanted)
        line = fp.readline()

      return column

name_doc = str(input('Pegar coluna de arquivo de texto. Insira o nome do arquivo desejado. >'))
print(Colonna(name_doc))


