import sqlite3
import pandas as pd


df = pd.read_csv('edtech_subscriptions.csv')
conn = sqlite3.connect('edtech.db')
df.to_sql('subscriptions', conn, index=False, if_exists='replace')
print("Database 'edtech.db' created successfully with table 'subscriptions'!")
conn.close()
