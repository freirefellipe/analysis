# CODE FINISHED. DON'T MESS UP.
# THIS SCRIPT INSERTS A STUDENT'S GRADES INTO A DATABASE

import pandas

students_list_df = pandas.read_csv('students_list.csv', delimiter=';')

NOME_COMPLETO = students_list_df['NOME_COMPLETO']

print(NOME_COMPLETO) # show the list with numbers as reference to choose one

student_chosen = int(input('Insira o número na lista referente ao aluno: '))

import os
import csv

entry_types = ['NOME', 'ORAL', 'AUDITIVA', 'ESCRITA', 'EXERCICIOS', 'PARTICIPACAO', 'FREQUENCIA']

# cria ou abre um arquivo csv para escrever as notas dos alunos

if os.path.exists('student_grades.csv') == False:

	student_grades_csv = open('student_grades.csv', mode='w', encoding='utf8')

	student_grades = csv.writer(student_grades_csv, delimiter=';')
  
	student_grades.writerows([entry_types])


student_grades_csv = open('student_grades.csv', mode='a', encoding='utf8')

student_grades = csv.writer(student_grades_csv, delimiter=';')
  
student_grades.writerows([[
  				NOME_COMPLETO[student_chosen], 
  				float(input(entry_types[1])), 
  				float(input(entry_types[2])),
  				float(input(entry_types[3])),
  				float(input(entry_types[4])),
  				float(input(entry_types[5])),
  				float(input(entry_types[6])),
  			]])

student_grades_csv.close()

