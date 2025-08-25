import random

adivinha = 0 # qualquer número para que seja modificado depois 
numero_sorteado = 10 # qualquer número para qeue seja modificado depois

while adivinha != numero_sorteado:
 try:
  numero_sorteado = random.randint(1,6)
  adivinha = int(input('Adivinha o número de 1 a 6 que eu tô pensando agora: '))
  if (adivinha == numero_sorteado) & (adivinha < 7):
    print(f'Isso mesmo. {numero_sorteado}')
  elif (adivinha != numero_sorteado) & (adivinha < 7):
    print(f'Não foi dessa vez. Pensei em {numero_sorteado}')
  else:
    print('Número somente de 1 a 6')

 except TypeError:
   print('Isso não é número')

 except Exception as outro:
   print(type(outro))
   print('Esse não foi o combinado.')

print ('-fim de jogo-')



# esse programa é um jogo de adivinhação.

