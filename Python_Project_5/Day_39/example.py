import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data2.db")
cursor = connection.cursor()

# Query all the data based on a condition
cursor.execute("SELECT * FROM events WHERE date='2025.10.15'")
rows = cursor.fetchall()
print(rows)

# Query certain columns based on a condition
cursor.execute("SELECT band, date FROM events WHERE date='2025.10.15'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
nw_rows = [('Cats', 'Cats City', '2025.10.21'),
           ('Dogs', 'Dogs City', '2025.10.19')]

cursor.executemany("INSERT INTO events VALUES(?, ?, ?)", nw_rows)
connection.commit()

# Query all the database
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)
