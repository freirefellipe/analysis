def Rendimento(investimento: float, meses: int, taxa: float):
	for i in range(meses):
		print(round(investimento, 2))
		rendimento_mensal = investimento * taxa
		investimento += rendimento_mensal
	
	print(round(investimento, 2))

investimento, meses, taxa = float(input('Qual será o investimento inicial? R$')), int(input('Quantos meses de rendimento você estima? ' )), float(input('Qual a taxa de rendimento mensal que se aplica? '))

Rendimento(investimento, meses, taxa)

# PROGRAMA PARA SABER QUANTO O DINHEIRO VAI RENDER EM DETERMINADO TEMPO, INSERINDO: INVESTIMENTO, MESES, TAXA.

