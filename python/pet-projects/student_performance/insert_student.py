# CODE FINISHED. DON'T MESS UP.
# THIS SCRIPT CREATES A .CSV FILE WITH THE NAMES OF ALL THE STUDENTS INSERTED IN THE INPUT COMMAND.

import os
import csv

# import .py file with names_list

if os.path.exists('students_list.csv') == False: 

	header_names = ['NOME_COMPLETO', 'PRIMERIO_NOME', 'SEGUNDO_NOME', 'TERCEIRO_NOME', 'QUARTO_NOME']

	students_list_csv = open(file='students_list.csv', mode='w', encoding='utf8')

	students_list = csv.writer(students_list_csv, delimiter=';') # criar variável para inserir linhas 
	  
	students_list.writerows([header_names]) # escrever cabeçalho no arquivo csv caso ainda não exista;
	  
	students_list_csv.close()


student_name = str(input('Nome completo do aluno: '))

student_name_split = student_name.split()

students = []

with open (file='students_list.csv', mode='r', encoding='utf8') as students_list_csv: # escrever nome completo, depois separar cada nome em uma coluna;

	header = students_list_csv.readline()
	
	line = students_list_csv.readline()

	while line: # linha que faz uma lista com os nomes completos do documento students_list.csv
	
		line_sep = line.split(sep=';')
		
		full_name = line_sep[0]
		
		students.append(full_name)
		
		line = students_list_csv.readline()

	for i in range(len(students)):

		if student_name == students[i]:

			raise Exception ('Esse aluno já está cadastrado.')

with open (file='students_list.csv', mode='a', encoding='utf8') as students_list_csv:

	students_list = csv.writer(students_list_csv, delimiter=';')

	students_list.writerows([[
		
	student_name, 
	student_name_split[0], 
	student_name_split[1], 
	student_name_split[2] 

	]])

print('Aluno inserido com sucesso.')
