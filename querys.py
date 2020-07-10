from main import Connect
import pyodbc

# Creating a new function, Inheriting the class from the main file.
class Queries(Connect):

    def query_products (self):
        object = Connect()
        cursor = object.database_con()
        cursor.execute("SELECT ProductID, ProductName, UnitPrice FROM products")
        products = cursor.fetchall()
        for product in products:
            print(product)

    def query_citys(self):
        object = Connect()
        cursor = object.database_con()
        cursor.execute("SELECT city, country FROM customers WHERE country LIKE 'UK'")
        customers = cursor.fetchmany(10)
        for customer in customers:
            print(customer)

    def query_employees(self):
        object = Connect()
        cursor = object.database_con()
        cursor.execute("SELECT Firstname, Lastname from employees")
        employees = cursor.fetchall()
        for employee in employees:
            print(employee)


    def query_average(self):
        object = Connect()
        cursor = object.database_con()
        cursor.execute("SELECT AVG(UnitPrice) FROM Products ")
        averages =cursor.fetchall()
        for average in averages:
            print(average)



