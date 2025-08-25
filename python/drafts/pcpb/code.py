#import pandas
#df_ = pandas.read_csv('levantamento-aprovados-pcpb.csv')

with open (file='levantamento-aprovados-pcpb.csv', mode='r', encoding='utf8') as localfile:
    header = localfile.readline()
    print(header)
