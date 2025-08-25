-- CREATE DATABASE PCPB;

-- CREATE TABLE pcpb_survey;

USE PCPB;

CREATE TABLE pcpb_survey( 
dia VARCHAR(999), 
hora VARCHAR(999), 
email VARCHAR(999), 
nome VARCHAR(999), 
telefone VARCHAR(999), 
uf VARCHAR(999), 
ocupacao VARCHAR(999), 
estado_civil VARCHAR(999), 
cargo VARCHAR(999), 
classificacao VARCHAR(255), 
cfp VARCHAR(255), 
outro_concurso VARCHAR(255), 
sacrifica_para_cfp VARCHAR(255), 
muda_estado VARCHAR(255), 
pcpb_definitiivo VARCHAR(255), 
sugestao_acao VARCHAR(255), 
comparece_atos VARCHAR(255), 
cargos_aptos VARCHAR(255), 
preferencia_cargo VARCHAR(255), 
classificacao_cargos VARCHAR(999)
);

(dia, hora, email, nome, telefone, uf, ocupacao, estado_Civil, cargo, classificacao, cfp, outro_concurso, sacrifica_para_cfp, muda_estado, pcpb_definitivo, sugestao_acao, comparece_atos, cargos_aptos, preferencia_cargo, classificacao_cargos)

SET 
    dia = NULLIF(dia, ''),
    hora = NULLIF(hora, ''),
    email = NULLIF(email, ''),
    nome = NULLIF(nome, ''),
    uf = NULLIF(uf, '')
    ocupacao = NULLIF(ocupacao, '')
    estado_civil = NULLIF(estado_civil, '')
    cargo = NULLIF(cargo, '')
    classificacao = NULLIF(classificacao, '')
    cfp = NULLIF(cfp, '')
    outro_concurso = NULLIF(outro_concurso, '')
    sacrifica_para_cfp = NULLIF(sacrifica_para_cfp, '')
    telefone = NULLIF(telefone, '')
    uf = NULLIF(uf, '')
    ocupacao = NULLIF(ocupacao, '')
    estado_civil = NULLIF(estado_civil, '')
    cargo = NULLIF(cargo, '')
    classificacao = NULLIF(classificacao, '')
    cfp = NULLIF(cfp, '')
    outro_concurso = NULLIF(outro_concurso, '')
    sacrifica_para_cfp = NULLIF(sacrifica_para_cfp, '')
    muda_estado = NULLIF(muda_estado, '')
    pcpb_definitivo = NULLIF(pcpb_definitivo, '')
    sugestao_acao = NULLIF(sugestao_acao, '')
    comparece_atos = NULLIF(comparece_atos, '')
    cargos aptos = NULLIF(cargos_aptos, '')
    preferencia_cargo = NULLIF(preferencia_cargo, '')
    classificacao_cargos = NULLIF(classificacao_cargos, '');


LOAD DATA INFILE 'levantamento-aprovados-pcpb.csv'
INTO TABLE pcpb_survey
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS
