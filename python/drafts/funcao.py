
print ('-'*20) ################## EXEMPLO 1

# usa-se 'def' para indicar criação de uma função;
# em seguida, dá-se nome a ela e coloca-se valores dentro dos parênteses;

def somma (h, g: float) -> float: # o ': float' não é obrigatório, somente indica que tipo de variável será a entrada, assim como o '-> float', que só indica a saída;
 print(h + g) # dentro da função se determina o que será feito;
 
h = input('Primeiro valor: ')
g = input('segundo valor: ')

# foi preciso transformar os tipos das variáveis para que a soma funcionasse;
h = float(h)
g = float(g)

# por fim, o uso da função:
somma(h, g)

print('-'*20) ################### EXEMPLO 2

email = str(input('Insira seu email: '))

def user_domain (mail):
  mail_splitted = mail.split(sep='@')
  user = mail_splitted[0]
  domain = mail_splitted[1]
  return user, domain

user, domain = user_domain(email)

print(f'Usuário: {user}')
print(f'Domínio: {domain}')

print('-'*20) #################### EXEMPLO 3
# invertendo caracteres ou elementos de uma lista:

shakira = ['Estoy aqui', ['queriendote', 'ahogando...'], 'entre fotos y quadernos...']
hanson = 'I will come to you. Ohhh, I will come to you'

def function (a, b):
 a = a[::-1]
 b = b.upper()
 return a , b
#

print(function(shakira, hanson))

print('-'*20) ################## EXEMPLO 4

parole_dordine = [" cB402","As293","8jfu ","d19dJ"," 437"]

def trattare_parola(string): # faz função para tratar um elemento selecionado dentre os elementos, já que os métodos não funcionam em listas.

  string = string.upper()
  string = string.strip()
  return string

for i, parola in enumerate(parole_dordine): # trata cada elemento, um por um, de uma lista.
  
  parole_dordine[i] = trattare_parola(parola)

print (parole_dordine)

print ('-'*20) ###################### EXEMPLO 5

def maiusculo(texto: str) -> str:
  
  texto_maiusculo = texto.upper()
  return texto_maiusculo # se não colocar esse retorno, o programa vai retornar o valor None, pois não entrega nada.

nome = 'Fellipe'

nome_maiusculo = maiusculo(texto=nome)
print (nome_maiusculo)

print ('-'*20) ###################### EXEMPLO 5

# função autocontida, na qual não é necessaŕio retirnar valor, podendo determiná-lo como None.

def constante() -> None:
  print(837.45)
  return None

print (constante())

print ('-'*20) ###################### EXEMPLO 6

#1 cria a função contendo nos parênteses as três variáveis que vão ser utilizadas, e informando que o valor final vai ser Booleano;
#2 dentro da função: usa o 'try-except' para colocar o 'with open' e o 'for-in' e, caso algo dê errado, vai retornar valor False;
#3 cria o arquivo com 'with open () as _:', cria uma linha para cabeçalho a inserir no documento em criação;
#4 usa 'for _ in _' para fazer a mesma coisa recém-feita, mas dessa vez pegando cada elemento de uma lista a ser determinada e inserindo novas linhas;
#5 fecha o 'try-except' com return True para caso tudo ocorra bem;
#6 cria uma variável que vai chamar a função.

nome_archivio = 'archivio.csv'
intestazione = 'Cabeçalho' + '\n'
contenuti = ['Guarda','Ascolta','Tocca','Annusa']

def creazione_file (a: str, b: str, c: list) -> bool:
  try:
    with open (file= a, mode='w', encoding='utf8') as fp:
      riga = b + '\n'
      fp.write(riga)

      for contenuto in c:
        riga = str(contenuto + '\n')
        fp.write(riga)

  except Exception as eccezione:
    print(eccezione)
    return False

  return True

rivela_successo = creazione_file(a= nome_archivio, b=intestazione, c= contenuti)
print (rivela_successo)

print ('-'*20) ###################### EXEMPLO 7


def juros_compostos_anual(
valor_inicial: float,
taxa_juros_anual: float,
anos: int) -> float:
valor_final = valor_inicial
for ano in range(1, anos+1):
valor_final =
valor_final * (
1 + taxa_juros_anual
)
valor_final = round(valor_final, 2)
print(
f'Para um valor inicial de R$ {valor_inicial} ' +
'e uma taxa de juros anual de {taxa_juros_anual}, ' +
'em {anos} anos você terá R$ {valor_final}')
return valor_final
valor_inicial, taxa_juros_anual, anos = 1000.00, 0.05, 10
valor_final = juros_compostos_anual(
valor_inicial=valor_inicial,
taxa_juros_anual=taxa_juros_anual,
anos=anos
)
valor_inicial, taxa_juros_anual, anos = 1020.00, 0.03, 10
valor_final = juros_compostos_anual(
valor_inicial=valor_inicial,
taxa_juros_anual=taxa_juros_anual,
anos=anos
)

print ('-'*20) ################## EXEMPLO 8
# Extraindo coluna de arquivo .csv com função:

def extrai_coluna (nome_arquivo: str, numero_coluna: int):

  coluna_extraida = []
  
  with open(file=nome_arquivo, mode='r', encoding='utf8') as dados:
    linha = dados.readline() # lê o cabeçalho
    #linha = dados.readline() # lê a primeira linha   
    while linha:
      coluna = linha.split(sep=',') # quebra a string nas virgulas e salva os resultados em uma lista
      coluna_desejada = coluna[numero_coluna - 1] # seleciona o segundo elemento da lista
      coluna_extraida.append(coluna_desejada) # salva o valor na lista de valor_venda
      linha = dados.readline() # lê uma nova linha, se a linha não existir, salva o valor None
  return coluna_extraida

insira_nome_arquivo = input('Nome do arquivo: ')
insira_numero_coluna = input('numero_coluna: ')

coluna_arquivo = extrai_coluna(nome_arquivo=insira_nome_arquivo, numero_coluna=insira_numero_coluna)
print(coluna_arquivo)

