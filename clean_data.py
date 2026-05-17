
import pandas as pd
from sqlalchemy import create_engine

df= pd.read_csv('supermarket_sales.csv')

df['datetime']= df['date'] + ' ' + df['time']
df['datetime']= pd.to_datetime(df['datetime'])

df = df.drop_duplicates()
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.info())

engine = create_engine(
    "mysql+pymysql://root:(passwort)@localhost:3306/testdb?charset=utf8mb4"
)
df.to_sql(
    name="supermarkt_sales",
    con=engine,
    if_exists="replace",
    index=False
)
