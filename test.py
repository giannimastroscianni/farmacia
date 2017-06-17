import cx_Oracle

try:
    con = cx_Oracle.connect('gianni/gianni@localhost:1521/orcl')
except:
    print "Connection refused"

cursor = con.cursor()
cursor.execute("select * from paziente")
rows = cursor.fetchall()
to_return = []
for row in rows:
    to_return.append(row)
cursor.close()
con.close()
print to_return
