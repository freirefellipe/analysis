def linha(): print ('-'*20) 

linha() ################# ESEMPIO 1

costante = float(input('Insira o valor: '))

lambda_funzione = lambda i: (i + 7) * 3

print (lambda_funzione(costante))


linha() ################# ESEMPIO 2

# calcular resultado final de um investimento (valor_investimento) com juros (juros_dinamico) 

juros_dinamico = float(input('Valor de juros: '))
valor_investimento = float(input('Valor do investimento: '))


resultado = valor_investimento * (1 + 0.05)

print (resultado)

linha() ################# ESEMPIO 3

endereco_email = str(input('Insira seu email: '))

extrai_usuario_email = lambda endereco_email:endereco_email.split(sep='@')[0]

nome_usuario = extrai_usuario_email(endereco_email)
print(f'Nome de usuário: {nome_usuario}')

linha() ################# ESEMPIO 4

numero_par = lambda numero: True if numero % 2 == 0 else False

numeros = range(0, 10 + 1)

for numero in numeros:
    print(f'{numero} é par.') if numero_par(numero) == True else print(f'{numero} não é par.')

linha() ################# ESEMPIO 5

emails = ['freirefellipe@gmail.com','freirefellipe@outlook.com','lipeoliv@mail.com']

extrai_nome_usuario = lambda email: email.split(sep='@')[0]

nomes_usuario = []

for email in emails: # dá para fazer isso com a função anônima 'map'
    usuario = extrai_nome_usuario(email)
    nomes_usuario.append(usuario)

print(nomes_usuario)


