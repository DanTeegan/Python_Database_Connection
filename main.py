# Here we are importing
import pyodbc

# Here we are creating a class called Connect
class Connect:
        # Here we are creating the method for the connection to the database
    def database_con(self):
            server = 'databases2.spartaglobal.academy'
            database = 'Northwind'
            username = 'SA'
            password = 'Passw0rd2018'
            connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=' + database +';UID='+ username +';PWD='+ password)

            # Here we are creating a cursor
            cursor = connections.cursor()
            print("Connection is successful")
            # Here we are returning the cursor for use in the querys
            return cursor


            # try:
            #     with pyodbc.connect(connections, timeout=10) as connection:
            #         print("Connection did not time out")
            # except:
            #     print("Connection Timed out")
            # else:
            #     cursor = connections.cursor()
            #             print("Connection sucesful")
            #             return cursor


            # query_result_products = cursor.execute('SELECT * FROM Products')
            # query_result_customers = cursor.execute('SELECT * FROM Customers')
            # query_result_ = cursor.execute('SELECT * FROM ')













