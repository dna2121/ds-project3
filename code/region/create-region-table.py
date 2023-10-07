import psycopg2
import csv

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
cur = conn.cursor()

cur.execute("""
        CREATE TABLE IF NOT EXISTS region(
        id serial PRIMARY KEY,
        postalZip text,
        region text,
        country text)
        """
)

conn.commit()

with open('D:\\Python\\ds-project3\\source\\region.csv', 'r') as f :
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
                postalZip, region, country = row
                cur.execute(
                        "INSERT INTO region VALUES (default, %s, %s, %s) ON CONFLICT DO NOTHING", 
                        row)
                
conn.commit()

cur.execute("""
        SELECT * FROM region
        """
)

cur.fetchall()