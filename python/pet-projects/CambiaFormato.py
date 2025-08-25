# abre o arquivo que vai ler, no formato que não quer;
# cria o arquivo que vai receber o conteúdo do arquivo de extensão indesejada;
# cria variável que recebe linha lida;
# usa a estrutura de repetição mais simples, while, para copiar linha por linha;
# cocmando para escrever;
# comando para ler a próxima linha.

class CambiaFormato(object):
   
   def __init__(self, nome_file: str):
     self.nome = nome_file
     self.formato = self._cambia_formato()
      
   def _cambia_formato(self):
     with open (file=self.nome, mode='r', encoding='utf8') as DaLeggere: 
      with open (file=nome_nuovo_file, mode='w', encoding='utf8') as DaScrivere: 
  
        riga = DaLeggere.readline() 
  
        while riga: 
          DaScrivere.write(riga) 
          riga = DaLeggere.readline() 

##

nome_file_daCambiare = str(input('Nome del file da cambiare: '))
nome_nuovo_file = str(input('Nome del nuovo file: '))
CambiaFormato(nome_file_daCambiare)
