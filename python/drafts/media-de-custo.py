# PERGUNTA A QUANTIDADE DE ITENS COMPRADOS E QUANTO CUSTOU CADA UM PARA SOMAR O TOTAL GASTO E MÉDIA DE PREÇO DE CADA ITEM

cds = int(input('Quantidade de CDs: ')) # entrada para quantidade de cds

preco = 0 # cria a variável de preço antes, com valor, que deve ser 0

for a in range(cds): # laço for para o número de cds inseridos
	preco = preco + float(input(f'Digite o preço do CD {a + 1}: ')) # variável de preço aumenta gradualmente
print(f'Preço total: R${preco:.2f}.\nMédia de custo por CD: R${preco/cds:.2f}') # exibe o resultado

