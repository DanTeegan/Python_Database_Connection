import pyodbc



server = 'databases2.spartaglobal.academy'
#databases2.spartaglobal.academy
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=' + database +';UID='+ username +';PWD='+ password)
cursor = connections.cursor()
print(connections)
print(cursor)

# We create a variable
query_result = cursor.execute('SELECT * FROM Products')

# print("Printing query_result object:", query_result)

# Code for fetching one row - use fetchone - use fetchmany if you want to fetch many rows. fetchall = fetch all rows

# This would give you the second collumn of rows
# print(rows[1])

rows=query_result.fetchone()
print(type(rows))
print(rows[1])
print(rows.ProductName)

rows=query_result.fetchone()
print(type(rows))
print(rows[1])
print(rows.ProductName)

# print("Executing fetch many:", query_result.fetchmany(20))

rows = query_result.fetchmany(30)
for row in rows:
    print(row)


rows=query_result.fetchall()
for row in rows:










# Establishing a database connection
# We are trying to get the data from the database into the python console.

# ODBC - Open database conectivty. Used with microsoft applications. is an API

#pyodbc is a python library tha helps you to connect to the database

# Extablishing a connection to the database that we want to use
# server = 'databases2.spartaglobal.academy'
# database = 'Northwind'
# username = 'SA'
# password = 'Passw0rd2018'
#
#
# connections = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
#
#
# # try:
#     with pyodbc.connect(connections, timeout=10) as connection:
#         print("Connection did not time out")
# except:
#     print("Connection Timed out")
# else:
#     cursor = connections.cursor()
#     print(connections)
#     print(cursor)