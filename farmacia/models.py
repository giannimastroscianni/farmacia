# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime as dt
import traceback


class Paziente:
    def __init__(self, cf):
        self.cf = cf

    def get_cf(self):
        return self.cf


class Medico:
    def __init__(self, cod):
        self.cod = cod

    def get_cod(self):
        return self.cod


class Casa_Farmaceutica:
    def __init__(self, nome, recapito):
        self.nome = nome
        self.recapito = recapito

    def get_nome(self):
        return self.nome

    def get_recapito(self):
        return self.recapito


class Prodotto:
    def __init__(self, id, nome, descrizione, casa):
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.casa = casa

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_descrizione(self):
        return self.descrizione

    def get_casa(self):
        return self.casa


class Farmacot(Prodotto):
    def __init__(self, id, nome, descrizione, casa, prescrivibile):
        Prodotto.__init__(id, nome, descrizione, casa)
        self.prescrivibile = prescrivibile

    def get_prescrivibile(self):
        return self.prescrivibile


class Farmaco(Prodotto):
    def __init__(self, id, nome, descrizione, casa, prescrivibile):
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.casa = casa
        self.prescrivibile = prescrivibile

    def get_prescrivibile(self):
        return self.prescrivibile


class Brevettato(Farmaco):
    def __init__(self, id, nome, descrizione, casa, prescrivibile, durata):
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.casa = casa
        self.prescrivibile = prescrivibile
        self.durata = durata

    def get_durata(self):
        return self.durata


class Generico(Farmaco):
    def __init__(self, id, nome, descrizione, casa, prescrivibile, brevettato):
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.casa = casa
        self.prescrivibile = prescrivibile
        self.brevettato = brevettato

    def get_brevettato(self):
        return self.brevettato


class Profumeria(Prodotto):
    def __init__(self, id, nome, descrizione, casa):
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.casa = casa


class Cosmetici(Profumeria):
    def __init__(self, id, nome, descrizione, casa):
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.casa = casa


class Igiene(Profumeria):
    def __init__(self, id, nome, descrizione, casa):
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.casa = casa


class CuraBimbo(Profumeria):
    def __init__(self, id, nome, descrizione, casa):
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.casa = casa


class Vendita:
    def __init__(self, id, data, prodotti):
        self.id = id
        self.data = data
        self.prodotti = prodotti

    def get_id(self):
        return self.id

    def get_data(self):
        return self.data

    def get_prodotti(self):
        return self.prodotti


class Prescrizione:
    def __init__(self, id, medico, paziente, farmaci):
        self.id = id
        self.medico = medico
        self.paziente = paziente
        self.farmaci = farmaci

    def get_id(self):
        return self.id

    def get_medico(self):
        return self.medico

    def get_paziente(self):
        return self.paziente

    def get_farmaci(self):
        return self.farmaci


class Dao:
    import cx_Oracle
    try:
        con = cx_Oracle.connect('gianni/gianni@localhost:1521/orcl')
    except:
        traceback.print_exc()

    def get_pazienti(self):
        cursor = self.con.cursor()
        cursor.execute("select * from paziente order by cf")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(Paziente(row[0]))
        cursor.close()
        return to_return

    def get_medici(self):
        cursor = self.con.cursor()
        cursor.execute("select * from medico order by cod")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(Medico(row[0]))
        cursor.close()
        return to_return

    def get_case(self):
        cursor = self.con.cursor()
        cursor.execute("select * from casa_farmaceutica order by nome, recapito")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(Casa_Farmaceutica(row[0], row[1]))
        cursor.close()
        return to_return

    def get_prodotti(self):
        cursor = self.con.cursor()
        cursor.execute("select p.id, p.nome, p.descrizione,"
                       "deref(p.casa_farmaceutica).nome,"
                       "deref(p.casa_farmaceutica).recapito "
                       "from prodotto p order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            casa = row[3] + ", " + row[4]
            to_return.append(Prodotto(row[0], row[1], row[2], casa))
        cursor.close()
        return to_return

    def get_farmaci(self):
        cursor = self.con.cursor()
        cursor.execute("select p.id, p.nome, p.descrizione,"
                       "deref(treat(value(p) as farmacoty).casa_farmaceutica).nome,"
                       "deref(treat(value(p) as farmacoty).casa_farmaceutica).recapito,"
                       "treat(value(p) as farmacoty).prescrivibile "
                       "from prodotto p "
                       "where value(p) is of type (farmacoty) "
                       "order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            casa = row[3] + ", " + row[4]
            to_return.append(Farmaco(row[0], row[1], row[2], casa, row[5]))
        cursor.close()
        return to_return

    def get_brevettati(self):
        cursor = self.con.cursor()
        cursor.execute("select p.id, p.nome, p.descrizione,"
                       "deref(treat(value(p) as brevettatoty).casa_farmaceutica).nome,"
                       "deref(treat(value(p) as brevettatoty).casa_farmaceutica).recapito,"
                       "treat(value(p) as brevettatoty).prescrivibile,"
                       "treat(value(p) as brevettatoty).fino_a "
                       "from prodotto p "
                       "where value(p) is of type (brevettatoty) "
                       "order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            dat = row[6].strftime("%Y/%m/%d")
            date = dt.strptime(dat, "%Y/%m/%d").timetuple()
            fino_a = (date[0], date[1], date[2])
            casa = row[3] + ", " + row[4]
            to_return.append(Brevettato(row[0], row[1], row[2], casa, row[5], fino_a))
        cursor.close()
        return to_return

    def get_generici(self):
        cursor = self.con.cursor()
        cursor.execute("select p.id, p.nome, p.descrizione,"
                       "deref(treat(value(p) as genericoty).casa_farmaceutica).nome,"
                       "deref(treat(value(p) as genericoty).casa_farmaceutica).recapito,"
                       "treat(value(p) as genericoty).prescrivibile,"
                       "deref(treat(value(p) as genericoty).brevettato).id "
                       "from prodotto p "
                       "where value(p) is of type (genericoty) "
                       "order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            casa = row[3] + ", " + row[4]
            to_return.append(Generico(row[0], row[1], row[2], casa, row[5], row[6]))
        cursor.close()
        return to_return

    def get_profumeria(self):
        cursor = self.con.cursor()
        cursor.execute("select p.id, p.nome, p.descrizione,"
                       "deref(treat(value(p) as di_profumeriaty).casa_farmaceutica).nome,"
                       "deref(treat(value(p) as di_profumeriaty).casa_farmaceutica).recapito "
                       "from prodotto p "
                       "where value(p) is of type (di_profumeriaty) "
                       "order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            casa = row[3] + ", " + row[4]
            to_return.append(Profumeria(row[0], row[1], row[2], casa))
        cursor.close()
        return to_return

    def get_cosmetici(self):
        cursor = self.con.cursor()
        cursor.execute("select p.id, p.nome, p.descrizione,"
                       "deref(treat(value(p) as cosmeticoty).casa_farmaceutica).nome,"
                       "deref(treat(value(p) as cosmeticoty).casa_farmaceutica).recapito "
                       "from prodotto p "
                       "where value(p) is of type (cosmeticoty) "
                       "order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            casa = row[3] + ", " + row[4]
            to_return.append(Profumeria(row[0], row[1], row[2], casa))
        cursor.close()
        return to_return

    def get_igiene(self):
        cursor = self.con.cursor()
        cursor.execute("select p.id, p.nome, p.descrizione,"
                       "deref(treat(value(p) as per_igienety).casa_farmaceutica).nome,"
                       "deref(treat(value(p) as per_igienety).casa_farmaceutica).recapito "
                       "from prodotto p "
                       "where value(p) is of type (per_igienety) "
                       "order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            casa = row[3] + ", " + row[4]
            to_return.append(Profumeria(row[0], row[1], row[2], casa))
        cursor.close()
        return to_return

    def get_cura_bimbo(self):
        cursor = self.con.cursor()
        cursor.execute("select p.id, p.nome, p.descrizione,"
                       "deref(treat(value(p) as cura_bimboty).casa_farmaceutica).nome,"
                       "deref(treat(value(p) as cura_bimboty).casa_farmaceutica).recapito "
                       "from prodotto p "
                       "where value(p) is of type (cura_bimboty) "
                       "order by id")
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            casa = row[3] + ", " + row[4]
            to_return.append(Profumeria(row[0], row[1], row[2], casa))
        cursor.close()
        return to_return

    def get_vendite(self):
        cursor = self.con.cursor()
        cursor.execute("select v.id, v.data "
                       "from vendita v")  # aggiungere nested table
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            dat = row[1].strftime("%Y/%m/%d")
            date = dt.strptime(dat, "%Y/%m/%d").timetuple()
            data = (date[0], date[1], date[2])
            t = (row[0], data)
            to_return.append(t)
        cursor.close()
        return to_return

    def get_prescrizioni(self):
        cursor = self.con.cursor()
        cursor.execute("select p.id,"
                       "deref(p.medico).cod,"
                       "deref(p.paziente).cf "
                       "from prescrizione p")  # aggiungere nested table
        rows = cursor.fetchall()
        to_return = []
        for row in rows:
            to_return.append(row)
        cursor.close()
        return to_return

    def insert_paziente(self, cf):
        cursor = self.con.cursor()
        cursor.execute("insert into paziente values('" + cf + "')")
        cursor.close()
        self.con.commit()

    def insert_medico(self, cod):
        cursor = self.con.cursor()
        cursor.execute("insert into medico values('" + cod + "')")
        cursor.close()
        self.con.commit()

    def insert_casa(self, nome, recapito):
        cursor = self.con.cursor()
        cursor.execute("insert into casa_farmaceutica values('" + nome + "', '" + recapito + "')")
        cursor.close()
        self.con.commit()

    def insert_brevettato(self, id, nome, descrizione, nome_casa, recapito_casa, prescrivibile, durata):
        cursor = self.con.cursor()
        print nome_casa, recapito_casa
        query = "insert into prodotto select brevettatoty(" + id + ", '" + nome + "', '" + descrizione + "', " \
                "(select ref(c) from casa_farmaceutica c where c.nome='" + nome_casa + "' and c.recapito='" + recapito_casa + "'),"\
                + prescrivibile + ",to_date('" + durata + "', 'yyyy-mm-dd')) from dual;"
        print query
        cursor.execute(query)
        cursor.close()
        self.con.commit()