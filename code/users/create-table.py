import psycopg2
import csv

#connect to postgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
cur = conn.cursor()

#create table
cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY,
        email text,
        name text,
        phone text,
        postalZip text)
        """
)
#setelah execute maka table disave.
conn.commit()


#insert data
with open('D:/Python/ds-project3/source/users_w_postal_code.csv', 'r') as f :
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
                email, name, phone, postalZip = row
                cur.execute(
                        "INSERT INTO users VALUES (default, %s, %s, %s, %s) ON CONFLICT DO NOTHING", 
                        row)
#save
conn.commit()


cur.execute("""
        SELECT * FROM users
        """
)

#menampilkan hasil, tapi harus execute select * dulu
cur.fetchall()
cur.fetchone()