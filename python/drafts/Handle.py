doc_to_read = input('Nome do documento a ser lido: ')

# CONVERTER FORMATO

class Handle(object):

  def __init__(self, doc_to_read):
    self.doc = doc_to_read
    self.convert = self.converter()
    self.clean = self.cleaner()

  def converter(self):

    doc_to_make = input('Nome do documento a ser criado: ')

    with open (file=doc_to_read, mode='r', encoding='utf8') as doc_read:
      with open(file=doc_to_make, mode='w', encoding='utf8') as doc_new:

        line = doc_read.readline()

        while line:
          doc_new.write(line)
          line = doc_read.readline()

# LIMPAR OS DADOS

  def cleaner(self):

    doc_read_list = [])

    with open (file=doc_to_make, mode='r', encoding='utf8') as doc_read:

      line = doc_read.readline

      while line:
        line_treated = line.strip().split(sep=',')
        doc_read_list.append(line_treated)
        line = doc_read.readline()

# SOMAR O VALOR DAS FATURAS
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
