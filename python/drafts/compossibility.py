from random import random 

spazio_campionale = [int(100 * random()) for _ in range(0, 10)] # programa um sorteio para criar lista com espaço amostral;

print(spazio_campionale)

from functools import reduce #

# criar uma variável inicialmente com reduce(), e, no lugar da coleção, colocar outra função dentro - todas com seus lambda - tipo boneca russa.

ridurre_confronta_due = reduce(lambda a, b : a if a > b else b, filter(lambda a : a > 50, map(lambda a : a * 2, spazio_campionale))) 

print(ridurre_confronta_due)
