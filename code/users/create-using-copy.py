import psycopg2
import csv

#connect to postgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
cur = conn.cursor()

#create table
cur.execute("""
        CREATE TABLE IF NOT EXISTS users_using_copy(
        id serial PRIMARY KEY,
        email text,
        name text,
        phone text,
        postal_code text)
        """
)

conn.commit()


with open('D:/Python/ds-project3/source/users_w_postal_code.csv', 'r') as f :
    next(f)
    cur.copy_from(f,'users_using_copy', sep=',', columns=('email', 'name', 'phone', 'postal_code'))

conn.commit()


cur.execute("""
        SELECT * FROM users_using_copy
        """
)

cur.fetchall()