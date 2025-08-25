famiglia = ['pai','Deraldo','mãe','Fátima','irmão','Thiago']

famiglia = {famiglia[0]:famiglia[1],famiglia[2]:famiglia[3],famiglia[4]:famiglia[5]}

print (famiglia['pai']) # é possível ver o valor de uma chave em específico.

famiglia['irmao'] = 'Victor' # assim como é possível mudar o valor de uma chave em específico.

print (famiglia['irmao'])

# utilizando métodos para dicionários:

family = dict(father='Deraldo', mother='Fátima', child_one='Fellipe')

print (family)

family.update({'child_one':'Thiago'}) # substituindo

print (family)

family.update({'child_two':'Fellipe'}) # aditando

print (family)

# transformando somente as chaves em lista:

family_keys = list(family.keys()) # transformando somente as chaves em lista.
family_items = list(family.items()) # transformando chaves e valores em lista sendo cada elemento uma tupla relacionando chave com seu valor.

print (family_keys)
print (family_items)
