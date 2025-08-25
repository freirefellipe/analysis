FONTE: https://www.youtube.com/watch?v=Kh_5NYtZrHU
---
**BAIXAR NO TERMINAL**
$ sudo apt install mysql-server
    - login dever ser feito com sudo. Após definir senha, sudo só será possível inserindo a senha
    
**DETERMINAR SENHA PARA O ROOT**
-> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '<senha>';

**FAZENDO LOGIN COMO ROOT**
$ mysql -uroot -p (vai quebrar a linha para inserir a senha)
ou
$ mysql -uroot -p <senha> (a senha fica visível)

**EXECUTAR O SCRIPT DE CONFIGURAÇÃO DO MYSQL:**
$ sudo mysql_secure_installation

**IMPORTANDO CSV**
após mover os csv's para a pasta /var/lib/mysql-files/ 
criar uma tabela com colunas iguais a do doc a ser importado, exemplo:
-> CREATE TABLE <nome>(
    coluna1 varchar(255),
    coluna2 int(10)
    );
    
-> IMPORT DATA INFILE '<endereco_arquivo>'
    INTO TABLE <tabela>
    FIELDS TERMINATED BY '<separador>'
    ENCLOSED BY '<encapsulamento>'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;
    
-- after selecting the desired query on a table...
-> INTO OUTFILE '<filename>'
-> FIELDS TERMINATED BY '<separador>'
-> FIELDS ENCLOSED BY '<encapsulamento>'
-> LINES TERMINATED BY '\n'

**CRIANDO USUÁRIOS**
-> CREATE USER '<username>'@'%'; (% significa que pode acessar de qualquer lugar)
-> IDENTIFIED BY '<senha>'; (letras maiúsculas e minúsculas, números, caracteres especiais)
-> FLUSH PRIVILEGES; (atualiza sem precisar reiniciar)
-> SELECT user,host FROM mysql.user; (mostra os usuários e respectivos hosts)
-> GRANT ALL PRIVILEGES ON *.* TO 'fellipe'@'%'; (os asteríscos significam [1] todos os bacnos de dados, e [2] todas as tabelas)
-> WITH GRANT OPTIONS 




