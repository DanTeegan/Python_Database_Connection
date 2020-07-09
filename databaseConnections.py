import pyodbc
# Establishing a database connection
# We are trying to get the data from the database into the python console.

# ODBC - Open database conectivty. Used with microsoft applications. is an API

#pyodbc is a python library tha helps you to connect to the database

# Extablishing a connection to the database that we want to use
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'


connections = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password


try:
    with pyodbc.connect(connections, timeout=10) as connection:
        print("Connection did not time out")
except:
    print("Connection Timed out")
else:
    cursor = connections.cursor()
    print(connections)
    print(cursor)