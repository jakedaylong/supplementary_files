import pymonad.tools


@pymonad.tools.curry(3)
def db_connect(dbname, user, password):
    # long drawn out code for connection goes here
    print(f"connected to {dbname} with {user} using {password}")


db_connect("postgres", "andy", "1234")

db_connect_pg = db_connect("postgres")
db_connect_pg("fred", "456")

db_connect_mysql = db_connect("mysql")

db_connect_mysql("x", "y")
