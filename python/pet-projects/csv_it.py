name = str(input('Nome do documento (sem incluir o formato): ')) + str('.csv')
header = str(input('Nome do cabeçalho: ')).lower()

def csv_it (name: str, header: str, conteudo: list) -> bool:
  with open(file=name, mode='w', encoding='utf8') as local:
    local.write(header + '\n')
    for ogni in conteudo:
      local.write(ogni + '\n') # o prof. André Sanchez antes escreve o conteúdo da linha em uma variável e a insere entre os parênteses.
  return True

csv_it(name=name], header=header, conteudo=) # será necessário criar uma forma de buscar listas em outros csvs e inserir o nome da lista no momento de executar o programa.

# csv_it(name='usernames.csv', header='usernames', conteudo=usernames)

print('Programa perfeitamente concluído.')

# PROGRAMA PARA TRANSFORMAR UMA LISTA EM UM DOCUMENTO CSV, INSERINDO: NOME DO DOCUMENTO, NOME DO CABEÇALHO, VARIÁVEL EM LISTA.
