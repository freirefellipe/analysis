import pandas
from ydata_profiling import ProfileReport

# read the csv for a database with pandas.read_csv
# create variable for ydata
# write the variable to an .html file

DATA = './titanic.csv'

dataframe = pandas.read_csv(DATA)

profile = ProfileReport(dataframe)

profile.to_file('./titanic-analysis.html')
