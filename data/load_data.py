import sqlite3
import pandas as pd

# Load CSV (semicolon-separated)
df = pd.read_csv('data/marketing_campaign.csv', sep=';')

# Connect to (or create) the database
conn = sqlite3.connect('data/marketing.db')

# Write to SQLite, replacing table if it exists
df.to_sql('customers', conn, if_exists='replace', index=False,
    dtype={
        'ID':                   'INTEGER',
        'Year_Birth':           'INTEGER',
        'Education':            'TEXT',
        'Marital_Status':       'TEXT',
        'Income':               'REAL',
        'Kidhome':              'INTEGER',
        'Teenhome':             'INTEGER',
        'Dt_Customer':          'TEXT',
        'Recency':              'INTEGER',
        'MntWines':             'REAL',
        'MntFruits':            'REAL',
        'MntMeatProducts':      'REAL',
        'MntFishProducts':      'REAL',
        'MntSweetProducts':     'REAL',
        'MntGoldProds':         'REAL',
        'NumDealsPurchases':    'INTEGER',
        'NumWebPurchases':      'INTEGER',
        'NumCatalogPurchases':  'INTEGER',
        'NumStorePurchases':    'INTEGER',
        'NumWebVisitsMonth':    'INTEGER',
        'AcceptedCmp1':         'INTEGER',
        'AcceptedCmp2':         'INTEGER',
        'AcceptedCmp3':         'INTEGER',
        'AcceptedCmp4':         'INTEGER',
        'AcceptedCmp5':         'INTEGER',
        'Complain':             'INTEGER',
        'Z_CostContact':        'INTEGER',
        'Z_Revenue':            'INTEGER',
        'Response':             'INTEGER'
    }
)

print(f"Rows loaded: {pd.read_sql('SELECT COUNT(*) FROM customers', conn).iloc[0,0]}")
print(pd.read_sql('SELECT * FROM customers LIMIT 5', conn))
conn.close()
