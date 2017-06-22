--TIPI
create or replace type pazientety as object(
  cf varchar(16),
  nome varchar(20),
  cognome varchar(20))final;
/
create or replace type medicoty as object(
  cod varchar(3),
  nome varchar(20),
  cognome varchar(20))final;
/
create or replace type casa_farmaceuticaty as object(
  nome varchar(20),
  recapito varchar(10))final;
/
create or replace type prodottoty as object(
  id integer,
  nome varchar(20),
  descrizione varchar(50),
  casa_farmaceutica ref casa_farmaceuticaty)not final;
/
create or replace type farmacoty under prodottoty(
  prescrivibile number(1)) not final;
/
create or replace type brevettatoty under farmacoty(
  fino_a date) final; 
/
create or replace type genericoty under farmacoty(
  brevettato ref brevettatoty) final;
/
create or replace type di_profumeriaty under prodottoty() not final;
/
create or replace type cosmeticoty under di_profumeriaty() final;
/
create or replace type per_igienety under di_profumeriaty() final;
/
create or replace type cura_bimboty under di_profumeriaty() final;
/
create or replace type venditaty as object(
  id number,
  data date,
  prodotti ref_prodottiNT) final;
/
create or replace type ref_prodottity as object(
  prodotto ref prodottoty,
  qta number);
/
create or replace type ref_prodottiNT as table OF ref_prodottity;
/
create or replace type prescrizionety as object(
  id number,
  paziente ref pazientety,
  medico ref medicoty,
  vendita ref venditaty,
  farmaci ref_farmaciNT) final;
/
create or replace type ref_farmacity as object(
  farmaci ref farmacoty);
/
create or replace type ref_farmaciNT as TABLE OF ref_farmacity;

--TABELLE
create table paziente of pazientety(
  primary key(cf));
/
create table medico of medicoty(
  primary key(cod));
/
create table casa_farmaceutica of casa_farmaceuticaty(
  primary key(nome, recapito));
/
create table prodotto of prodottoty(
  primary key(id),
  foreign key(casa_farmaceutica) references casa_farmaceutica);
/
create table vendita of venditaty(
  primary key(id)) nested table prodotti store as prodottint_tab;
/
create table prescrizione of prescrizionety(

  primary key(id),

  foreign key(medico) references medico,

  foreign key(vendita) references vendita,

  foreign key(paziente) references paziente) nested TABLE farmaci store as farmacint_tab;  
/









