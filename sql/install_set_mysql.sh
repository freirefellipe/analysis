#!/bin/bash

echo "Atualizando repositórios..."
sudo apt update ; sudo apt -y upgrade

echo "Instalando e configurandp o MySQL..."
sudo apt install mysql-server
sudo mysql_secure_installation -y
sudo echo "local-infile=1" >> /etc/mysql/mysql.conf.d/mysqld.cnf # allows local file loading. Add --local-infile into the login's mysql command.

echo "Criando arquivo executável"
touch db_config.sql

cat << EOF > db_config.sql
-- Criando um banco de dados.
CREATE DATABASE analise;

-- Criando um usuário com senha.
CREATE USER 'fellipe'@'localhost' IDENTIFIED BY 'EfeD;1.FKf';

-- concedendo ao novo usuário todos os privilégios de adm.
GRANT ALL PRIVILEGES ON analise.* TO 'fellipe'@'localhost';

FLUSH PRIVILEGES;

EXIT;

EOF

echo "Reiniciando o MySQL..."
sudo systemctl restart mysql

echo "Iniciando configuração de um banco de dados."
sudo mysql -u root -p < db_config.sql

