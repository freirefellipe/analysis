ids, candidates, votes, ranking = [], [], [], []

inputfile = str(input('Qual arquivo a ser lido? -'))

with open (file=inputfile, mode='r', encoding='utf8') as localfile:
  line = localfile.readline()

  while line:
    line = line.strip() if (len(line) < 11) else line.strip('\n')

    if ('.' not in line) and (len(line) == 8):
      ids.append(line)
    if (len(line) > 11):
      candidates.append(line)
    if '.' in line:
      votes.append(line)
    if (len(line) < 5 ):
      ranking.append(line)
    line = localfile.readline()
    
outputfile = str(input('Escolha o nome do documento: '))

with open (file=outputfile, mode='a', encoding='utf8') as tocsv:
  for i in range(len(ids)):
    tocsv.write(f'{ids[i]};{candidates[i]};{votes[i]};{ranking[i]}\n')

print(f'O documento {outputfile} foi gerado com sucesso')

