import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('D:\\Python\\ds-project3\\source\\region.csv', sep=',')
engine = create_engine('postgresql://postgres:1234@127.0.0.1:5432/postgres')

df.to_sql("region_from_file", engine)

df_read = pd.read_sql("select * from region_from_file", engine)