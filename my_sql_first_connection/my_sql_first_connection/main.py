import MySQLdb

host = "localhost"
user = "aplicacao"
password = "123456"
db = "sakila"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

print(con)