import sqlite3

db = sqlite3.connect(":memory:")
cur = db.cursor()
cur.execute("drop table if exists andy;")
cur.execute("create table andy (id int);")
cur.execute("insert into andy (id) values (1);")
db.commit()
data = cur.execute("select count(*) from andy ;")
assert len(cur.fetchall()) == 1
db.close()
db = None
