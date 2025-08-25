# THIS SCRIPT IS MEANT TO EXIBIT DATAFRAMES WITH SPECIFIC INFORMATION REQUESTED BY THE USER COMMANDS, AND GENERATE ITS GRAPHICS.

# imported: pandas, seaborn


import pandas

grades_df = pandas.read_csv('student_grades.csv', delimiter=';')

print(grades_df) 

nome_aluno = str(input('Nome completo do aluno: '))

student_df = grades_df.query(f'NOME == "{nome_aluno}"')

print(student_df)


import seaborn

with seaborn.axes_style('whitegrid'):

  student_grapho = seaborn.lineplot(data=student_df)

student_grapho.get_figure().savefig('student_chart.png')

print('Um gráfico em .png foi gerado com sucesso.')






