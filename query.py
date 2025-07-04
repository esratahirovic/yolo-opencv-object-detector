import sqlite3
import pandas as pd

conn = sqlite3.connect('detections.db')
df = pd.read_sql_query("SELECT * FROM detections LIMIT 10", conn)
print(df)
conn.close()
