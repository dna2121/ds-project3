import psycopg2
import csv

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
cur = conn.cursor()

cur.execute("""
        CREATE TABLE IF NOT EXISTS region_copy(
        id serial PRIMARY KEY,
        postal_code text,
        region text,
        country text)
        """
)

conn.commit()

with open('D:\\Python\\ds-project3\\source\\region.csv', 'r') as f :
    next(f)
    cur.copy_from(f,'region_copy', sep=',', columns=('postal_code', 'region', 'country'))

conn.commit()

cur.execute("""
        SELECT * FROM region_copy
        """
)

cur.fetchall()