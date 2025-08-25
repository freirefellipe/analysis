# transformando lista em conjunto para remover lementos iguais.

grupo = [24, 15, 23, 55, 24]
grupo = set(grupo)

print (grupo)


# é possível adicionar ou remover elementos em conjuntos. Como os conjuntos não ordenam elementos com índices, precisa somente do  add() para adicionar, ou remove() para remover.


grupo.add(94)
grupo.remove(15)

print (grupo)

# caso queira manipular elementos de conjuntos, é mais recomendável transformá-lo em lista.
