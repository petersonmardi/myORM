import sqlite3

con = sqlite3.connect('employee.db')
print('Database opened successfully')

cur = con.cursor()
cur.execute('''
CREATE TABLE Employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    address TEXT NOT NULL
)
''')
con.commit()
print('Table created successfully')
con.close()