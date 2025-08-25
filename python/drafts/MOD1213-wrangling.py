# DATAFRAMES COM PANDAS

dicio_dict = dict(
#		um = ['1.1', '1.2', '1.3', '1.4'],
		dois = ['2.1', '2.2', '2.3', '2.4'],
		três = ['3.1', '3.2', '3.3', '3.4'],
		quatro = ['4.1', '4.2', '4.3', '4.4']
	)

dicio_brackets = {
		'um': ['1.1', '1.2', '1.3'], 
		'dois': ['2.1', '2.2', '2.3']#, 
#		'três': ['3.1', '3.2', '3.3', '3.4'], 
#		'quatro': ['4.1', '4.2', '4.3', '4.4']
	}

dicio_list = [
	{'um':'1', 'dois':'2', 'três':'3'},
	{'um':'11', 'dois':'22', 'três':'33'},
	{'um':'111', 'dois':'222', 'três':'333'}
]

import json

dicioto_str_JSON = json.dumps(dicio_list, indent=4)
str_to_dicioJSON = json.loads(dicioto_str_JSON)
JSON_to_dicio = json.load(open('taxa.json', mode='r'))

import pandas as pd

# DFs

DICIO = dict(
		dicio_df = pd.DataFrame(dicio_brackets),
		credito_df = pd.read_csv('credito.csv', sep=';'), # abrindo com .DataFrame(open('credito.csv', mode='r')) de forma genérica não reconhece colunas
		github_df = pd.read_csv('github.csv', sep=';') # puxando direto de um documento csv com um comando específico do pandas é a forma correta.
)


dicio = dict(
		stars__stars_today = DICIO['github_df'][['stars','stars_today']] # cria uma tabela com séries (colunas) específicas da tabela-maior. Detalhe: [[]]
	)


# ADICIONANDO NOVA LINHA AO DF


nova_linha = {'Nome':'Fellipe', 'Idade':'37', 'Sexo':'Bom demais'}

df.append(pd.DataFrame([nova_linha]))


# ATRIBUTOS


a = 'Colunas:', DICIO['dicio_df'].columns[1] # mostra os cabeçalhos, sendo até possível selecionar uma pelo índice como em uma lista. 

b = 'Index:', DICIO['dicio_df'].index # mostra a 'distância' do Dataframe, incluindo o 0, e excluindo o último número, como faz o comando in range()

c = 'Forma:', DICIO['dicio_df'].shape # linha (incluindo o cabeçalho) por coluna

d = DICIO['dicio_df'].head(n=2) # três primeiros, sem contar com o cabeçalho, a não ser que atribua uma quantidade com m=?

e = DICIO['dicio_df'].tail(n=1) # três últimos, sem contar com o cabeçalho, a não ser que atribua uma quantidade com n=?

f = DICIO['dicio_df'].info() # mostra várias dessas informações, mas em um só comando

#g = DICIO['credito_df']#[['idade', 'id']].describe().T # descreve a tabela quando somente .describe(). O .T horizontaliza a coluna.


# MÉTODOS E FUNÇÕES


h = DICIO['github_df'].describe().T

i = DICIO['github_df'].columns

j = DICIO['github_df'][['project','language']].describe().T

k = DICIO['github_df'][['stars','stars_today']].describe().T

l = DICIO['github_df']['stars'].loc[0:4] # .loc[] 'localiza' uma quantidade de índices (linhas, segundo o Pandas) de uma série.

m = DICIO['github_df']['stars'][lambda a : a > 10000]

n = DICIO['github_df']['stars'][lambda a : a > 10000].reset_index(drop=True) # .reset_index() vai contar do 0 depois de extrair os índices aleatórios

o = dicio['stars__stars_today'].loc[0:4][lambda a : a > 500] 

p = DICIO['github_df'].loc[3, ['stars', 'language']] # o primeiro valor dentro do .loc escolhe o índice. O segundo (opcional) escolhe as séries.

q = DICIO['github_df'].query('language == "python" | forks > 50') # QUERY é chamado --filtro funcional-- de busca

r = DICIO['github_df'].query('language == "python" & forks > 1000')


# INSERÇÃO E REMOÇÃO DE DADOS EM TABELAS PANDAS


github_append = DICIO['github_df']['project'].append(pd.Series('projetos-do-fellipão'), ignore_index=True)

github_remove = DICIO['github_df']['project'][lambda value : value != 'n8n'] # lambda dentro de chaves. Refaz a série com a condinção imposta.

github_update1 = DICIO['github_df']['project'].loc[0] = 'projetos-do-fellipão'
github_update2 = DICIO['github_df']['project'].loc[0:2] = pd.Series(['projetos-do-fellipão', 'iuiu'])

github_update_lambda = DICIO['github_df']['language'][lambda value : value == 'go'] = 'come' # não é possível modificar o 'NaN' por não ser str

  # esses comandos anteriores estão realmente modificando o DataFrame carregado, mas não modifica o documento original.
   
dicio_list_df = pd.DataFrame(dicio_list) # pega um dataframe
dicio_list_um = dicio_list_df['um'] # pega uma série (coluna)
dicio_list_um_ = dicio_list_um.append(pd.Series(['nova série', 'iuiu']), ignore_index=True) # inclui novos valores à coluna

  # é possível também incluir uma linha inteira, adicionando pelo .append() um 'verbete' de diconário em forma de sub DataFrame:

github_new_line = DICIO['github_df'].append(pd.Series(dict(
								ranking = 1,
								project = 'melhor-projeto-do-fellipão',
								language = 'python',
								stars = 'todas',
								stars_today = 'todas-também',
								forks = 'muitos'
				)), ignore_index=True) # André da EBAC diz que precisa ser em lista, mas não coloquei e deu certo.

github_update3 = DICIO['github_df'].loc[1, 'project'] = 'iuiu-não-mais'


# AGREGAÇÕES E ORDENAÇÃO

 # agragação com o método .describe().T e .agg()

s = DICIO['github_df'][['stars', 'stars_today', 'forks']].describe().T # além de detalhar as séries horizontalmente. Isso é agregação

t = s.loc['stars', 'max'] # o método .loc[] traz de volta o formato Dataframe. Combinando com o describe() torna-se um detalhamento ainda mias minucioso 

u = DICIO['github_df'][['stars', 'stars_today', 'forks']].agg(['min', 'max', 'sum']) # Faz soma com .agg() escolhendo uma ou mais colunas. + q 1 é vira tabelinha

v = u.loc['max', 'stars'] # e ainda se aprofunda mais pegando um só valor da tabelinha com .loc(), escolhendo linha e coluna

 # agragação com o método .groupby()

w = DICIO['github_df'][['language', 'stars', 'stars_today', 'forks']].groupby('language').agg(['sum', 'min', 'max']) # faz a tabelinha sem describe e escolhe o critério de agrupamento com .groupby() e a tarefa a realizar com .agg('sum')

x = w.loc['python', 'stars'].loc['sum'] # usa-se o .loc[] para localizar valores específicos em tabelas, de preferência muito grandes

y = DICIO['github_df'].sort_values(by=['language', 'forks'], ascending=False) # ordena valores da cela escolhida. 'ascending=False' vai do maior ao menor.

z = DICIO['github_df'].sort_index(ascending=False)


# COMBINAÇÃO DE DATAFRAMES DIFERENTES

 # o método .concat() combina linhas para formar colunas, e o método .merge() combina colunas.

aa = DICIO['credito_df']
ab = DICIO['credito_df'].query('idade <= 30') 
ac = DICIO['credito_df'].query('idade > 30')
ad = pd.concat([ab, ac])
ae = pd.concat([aa[['id','idade']], aa[['sexo', 'idade']]]) # atenção para os NaN's que aparecem por, sendo diferentes, não ser possível completar a tabela.

 # o método .merge() combina  mais de uma tabela baseando-se nas colunas. Para entende-lo, usa-se comumente o diagrama de Venn.

af = pd.DataFrame(dicio_dict)
ag = pd.DataFrame(dicio_brackets)

ah = pd.merge(left=ag, right=af, on='dois', how='inner') # Inner exibi somente valores da interseção do diagrama de Venn
ai = pd.merge(left=ag, right=af, on='dois', how='outer') # Outer exibe todo o diagrama
aj = pd.merge(left=ag, right=af, on='dois', how='left') # Left exibe tudo que é comume  exculisvo do Left
ak = pd.merge(left=ag, right=af, on='dois', how='right') # Right exibe tudo que é comum e exclusivo do Right

# TÉCNICAS AVANÇADAS

 # proporção linguagens vs ranking com Gráfico em PIZZA usando MatplotLib

amount = {'amount':len(DICIO['github_df'])*[1]} # criou-se um diconário para ser uma nova coluna a concatenar com uma coluna de outro dataframe.

al = pd.concat([DICIO['github_df'][['language']], pd.DataFrame(amount)], axis=1) 

am = al.groupby('language').agg('sum') # agg é chamado "métrica de interesse". Nesse caso a métrica é Soma

an = am.plot.pie(y='amount', figsize=(12,7)) # mostra um gráfico de pizza em um caderno virtual como o Google Colab
an.get_figure().savefig('an.png')

 # proporção Stars vs Forks com gráfico SCATTER usando MatplotLib
 
ao = DICIO['github_df'].plot.scatter(x='stars' ,y='forks') # exibe um gráfico de pontos espalhados
ao.get_figure().savefig('ao.png')

ap = DICIO['github_df'].query('stars < 1000').plot.scatter(x='stars', y='forks', c='ranking', colormap='viridis') # inclui mais uma dimensão com 'ranking'
ap.get_figure().savefig('ap.png')

 # valores nulos

aq = DICIO['github_df'].isnull() # o método .isnull() mostra o Dataframe com True ou False no lugar de valores. Se o valor na célula é None, retorna True.
ar = DICIO['credito_df'].isnull().any() # adicionando o método .any(), ele mostra somente se a coluna tem célula vazia
at = DICIO['github_df'].isnull().any().any() # mostrará somente uma palavra indicando se tem célula vazia no Dataframe

def cenulo(df: pd.DataFrame) -> bool: # crio uma função para indicar se tem célula vazia no Dataframe
    return df.isnull().any().any()

 # ou remove ou preenche a célula

av = DICIO['github_df'].dropna() # o nétodo .dropna() remove as linhas que tem pelo menos uma célula com NaN

ax = DICIO['github_df'].fillna('Oi!') # o método .fillna() preenche NaN

print(am)

