import pandas
from ydata_profiling import ProfileReport

DATA = './brasil.csv'

dataframe = pandas.read_csv(DATA)

df_profile = ProfileReport(dataframe)

df_profile.to_file('ydata_brasil.html')


