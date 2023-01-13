import sqlite3
connect = sqlite3.connect('gta.db')
cursor = connect.cursor()

# Create a table.  A python string is called text in SQL 

cursor.execute("drop table if exists gta")
cursor.execute("create table gta (release_year integer, release_name text, city text)")

# Release list
release_list = [
    (1997, "Grand Theft Auto", "State of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (1997, "Grand Theft Auto III", "Liberty City")
]

# Insert the list into the database
cursor.executemany("insert into gta values (?,?,?)", release_list)

# Print all the rows in the database
for row in cursor.execute("select * from gta"):
     print(row)
     
# Print a specific row in the database
print("******************************************")
cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)

# Close the database connection
connect.close()