import sqlite3
import os

# Define the path to your folder

folder_path = r"C:\Users\aws.admin\Desktop\com7033-labactivities\week6\lab activities week6"

# Make sure the folder exists, if not, create it
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Define the full path to the SQLite database file
db_path = os.path.join(folder_path, 'currency.db')

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a query to retrieve data from the desired table
cursor.execute("SELECT * FROM currency;")

# Fetch all rows from the result of the query
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the connection
conn.close()