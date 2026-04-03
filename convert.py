import sqlite3
import pandas as pd

# Load the data we generated in Step 1
df = pd.read_csv('edtech_subscriptions.csv')

# Create a connection to a new SQLite database
conn = sqlite3.connect('edtech.db')

# Write the data to a table named 'subscriptions'
df.to_sql('subscriptions', conn, index=False, if_exists='replace')

print("Database 'edtech.db' created successfully with table 'subscriptions'!")
conn.close()