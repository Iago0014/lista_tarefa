

create database if not exists bd_lista_tarefas;

use bd_lista_tarefas;

create table listagem (idLista integer primary key auto_increment not null, nomeTarefa varchar(255), dataCriacao datetime, dataRealizar datetime, statusList boolean);

select * from listagem;

desc listagem;

alter table listagem add column statusList boolean;

update listagem set statusList = 1 where idLista = 34; 