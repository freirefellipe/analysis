def ritorna(commissioni: float): # criou-se uma função de alta ordem (função dentro de uma função). 
    return lambda invest: invest * (1 + commissioni)

# deixa preparada variável com o valor de juros no percentual desejado 
ritorna_5_percento = ritorna(commissioni=0.05)
ritorna_10_percento = ritorna(commissioni=0.10)

# cria variável dessa vez com o valor de investimento, utilizando também as variáveis de juros 
valore_finale = ritorna_5_percento(invest=1000)

valore_finale = ritorna_10_percento(invest=1000)

###

anni = int(input('Anos: '))
valore_inizio = float(input('Valor inicial: '))
valore_finale = valore_inizio

for anno in range(1, anni + 1):
    valore_finale = ritorna_5_percento(invest=valore_finale) # fazer o cálculo do investimento e juros ao longo dos anos

valore_inizio = round(valore_finale, 2)
print(valore_finale)
