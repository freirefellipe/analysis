eta = [44,22,63,21,27]

with open (file='eta.csv', mode='w', encoding='utf8') as fp:
  riga = 'Età' + '\n'
  fp.write(riga)
  
  for eta_elenco in eta:
    riga = str(eta_elenco) + '\n'
    fp.write(riga)
  
with open (file='eta.csv', mode='a', encoding='utf8') as fp:
  
  # já vai direto para o comando de repetição com 'for...in';
  for i in eta:
     riga = str(i + 100) + '\n' # modifica o conteúdo da variavel riga;
     fp.write(riga)
     

