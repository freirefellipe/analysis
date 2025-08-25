nome = 'Fellipe Freire Oliveira'

nome = list(nome)

nome[7] = ';'
nome[-9] = ';'

nome = "".join(nome)

print(nome)

nome_completo = open(file='nome-completo.csv', mode='a', encoding='utf8')
nome_completo.write(nome)
nome_completo.close()
