import sqlite3

conn=sqlite3.connect('myquotes.db')
curs = conn.cursor()

curs.execute("DROP TABLE IF EXISTS quotes_tb")

sql=''' create table quotes_tb(
        question text,
        response text) '''
curs.execute(sql)

curs.execute('''insert into quotes_tb values("Qu'estceque le covid 19?","Le COVID 19 est une maladie causée par un nouveau virus qui se répand rapidement dans le monde entier. Il peut affecter votre système respiratoire - vos poumons et vos voies respiratoires. Il peut se transmettre d une personne à l autre par des germes qui sont sur les mains et sur les surfaces lorsque les personnes infectées toussent ou éternuent.") ''')


conn.commit()
conn.close()