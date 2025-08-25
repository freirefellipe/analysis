print('-') ### ESEMPIO 1

numeros = [2,3,4]
numeros_quadrados = map(lambda numero:numero**2, numeros) # o método map precisa ter a informação da função a ser realizada e da coleção que vai ser utilizada respectivamente.

print(list(numeros_quadrados)) # foi usado aqui o método lista porque "os dados retornados ainda estão brutos", segundo o professor.

print('-')  ### ESEMPIO 2

emails = ['freirefellipe@gmail.com','freirefellipe@outlook.com','lipeoliv@mail.com']

extrai_nome_usuario = lambda email: email.split(sep='@')[0]

nomes_usuario = list(map(extrai_nome_usuario, emails)) # nesse caso, para efeito de ilustração, a função lambda ganhou nome com uma variável. Mas, em geral, a função lambda vai dentro da map para que continue 'anônima', sendo mais prático.

print(nomes_usuario)

print('-')  ### ESEMPIO 3 (mesmo do esempio 2, mas sem criar variável para o lambda)

emails = ['freirefellipe@gmail.com','freirefellipe@outlook.com','lipeoliv@mail.com']

extrai_nomes_usuario = list(map(lambda email: email.split(sep='@')[0], emails))

print(extrai_nomes_usuario)