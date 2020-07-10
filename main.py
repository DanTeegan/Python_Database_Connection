# Here we are importing
import pyodbc

class Connect:
    def database_con(self):
            server = 'databases2.spartaglobal.academy'
            database = 'Northwind'
            username = 'SA'
            password = 'Passw0rd2018'
            connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=' + database +';UID='+ username +';PWD='+ password)

            cursor = connections.cursor()

            print("Connection sucesful")
            return cursor


            # query_result_products = cursor.execute('SELECT * FROM Products')
            # query_result_customers = cursor.execute('SELECT * FROM Customers')
            # query_result_ = cursor.execute('SELECT * FROM ')













