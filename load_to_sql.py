import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root:sriii2005@localhost/internprep')

df_sales = pd.read_csv('fact_sales.csv')
df_products = pd.read_csv('dim_products.csv')
df_customers = pd.read_csv('dim_customers.csv')

# Push them into SQL tables using the engine
df_sales.to_sql('fact_sales', engine, if_exists='replace', index=False)
df_products.to_sql('dim_products', engine, if_exists='replace', index=False)
df_customers.to_sql('dim_customers', engine, if_exists='replace', index=False)

print("Database Loaded! ")