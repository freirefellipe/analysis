# ESSE SCRIPT PEDE PARA INSERIR NÚMEROS NO PROMPT, E OS COLOCA EM TUPLA PARA CONTAR QUANTAS VEZES ESSE NÚMERO SE REPETE.

num = (
input('Digite um número: '),
input('Digite o segundo número: '),
input('Digite o terceiro número: '),
input('Digite o quarto, e ultimo, número: ')
)

print(f"Os números que você digitou foram {num}")
print(f"O número {num[1]} apareceu {num.count(num[1])} vezes.")
