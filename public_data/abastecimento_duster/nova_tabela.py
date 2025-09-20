with open (file='abastecimento_duster.csv', mode='r', encoding='utf8') as abastecimento_duster:

  abastecimento_duster_csv = []
  
  abastecimento_duster_line = abastecimento_duster.readline().split(sep=';')
  abastecimento_duster_line.insert(0, 'data')
  print(abastecimento_duster_line)
  
  while abastecimento_duster_line == True:
    abastecimento_duster_line = abastecimento_duster.readline().split(sep=';')
    print(abastecimento_duster_line)

#    if len(i) != 8:
#      i[0].insert(0, '-')

  
#print(abastecimento_duster_)
#  for i in abastecimento_duster_csv:
#    lambda i : i.strip()
#    if len(i) != 8:
#      i[0].insert(0, '-')

#print(abastecimento_duster_full)
