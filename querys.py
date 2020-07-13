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

    # Creating a query for citys
    def query_customers_cities(self):
        object = Connect()
        cursor = object.database_con()
        cursor.execute("SELECT city, country FROM customers WHERE country LIKE 'UK'")
        customers = cursor.fetchmany(10)
        for customer in customers:
            print(customer)

    # Creating a method for employees
    def queries_employees(self):
        object = Connect()
        cursor = object.database_con()
        cursor.execute("SELECT Firstname, Lastname from employees")
        employees = cursor.fetchall()
        for employee in employees:
            print(employee)

    # Creating an average method of products
    def querys_average(self):
        object = Connect()
        cursor = object.database_con()
        cursor.execute("SELECT AVG(UnitPrice) FROM Products ")
        averages =cursor.fetchall()
        for average in averages:
            print(average)


