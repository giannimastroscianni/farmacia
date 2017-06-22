import cx_Oracle

try:
    con = cx_Oracle.connect('gianni/gianni@localhost:1521/orcl')
except:
    print "Connection refused"

cursor = con.cursor()
cursor.execute("insert into vendita select venditaty(46, to_date('2017-06-14', 'yyyy-mm-dd'), ref_prodottint(ref_prodottity((select ref(p) from prodotto p where p.id=100),2)))from dual")
cursor.close()
con.commit()
con.close()

