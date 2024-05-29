from manage import Database

class Store:
    table_name = "Stores"

    def __init__(self, store_name, location, contact_number):
        self.store_name = store_name
        self.location = location
        self.contact_number = contact_number

    def insert(self):
        query = f"""
            INSERT INTO {self.table_name} (Store_Name, Location, Contact_Number)
            VALUES ('{self.store_name}', '{self.location}', '{self.contact_number}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def select_all():
        query = f"SELECT * FROM {Store.table_name}"
        return Database.connect(query, "select")

    def update_location(self, new_location):
        query = f"""
            UPDATE {self.table_name}
            SET Location = '{new_location}'
            WHERE Store_Name = '{self.store_name}'
        """
        return Database.connect(query, "update")

    def delete(self):
        query = f"""
            DELETE FROM {self.table_name}
            WHERE Store_Name = '{self.store_name}'
        """
        return Database.connect(query, "delete")

    @staticmethod
    def join_with_categories():
        query = f"""
            SELECT s.Store_Name, s.Location, s.Contact_Number, c.Category_Name
            FROM {Store.table_name} s
            INNER JOIN Categories c ON s.Store_ID = c.Store_ID
        """
        return Database.connect(query, "select")


class Category:
    table_name = "Categories"

    def __init__(self, category_name):
        self.category_name = category_name

    def insert(self):
        query = f"""
            INSERT INTO {self.table_name} (Category_Name)
            VALUES ('{self.category_name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def select_all():
        query = f"SELECT * FROM {Category.table_name}"
        return Database.connect(query, "select")

    def update_category_name(self, new_name):
        query = f"""
            UPDATE {self.table_name}
            SET Category_Name = '{new_name}'
            WHERE Category_Name = '{self.category_name}'
        """
        return Database.connect(query, "update")

    def delete(self):
        query = f"""
            DELETE FROM {self.table_name}
            WHERE Category_Name = '{self.category_name}'
        """
        return Database.connect(query, "delete")


class Product:
    table_name = "Products"

    def __init__(self, product_name, category_id, price, quantity):
        self.product_name = product_name
        self.category_id = category_id
        self.price = price
        self.quantity = quantity

    def insert(self):
        query = f"""
            INSERT INTO {self.table_name} (Product_Name, Category_ID, Price, Quantity)
            VALUES ('{self.product_name}', {self.category_id}, {self.price}, {self.quantity})
        """
        return Database.connect(query, "insert")

    @staticmethod
    def select_all():
        query = f"SELECT * FROM {Product.table_name}"
        return Database.connect(query, "select")

    def update_quantity(self, new_quantity):
        query = f"""
            UPDATE {self.table_name}
            SET Quantity = {new_quantity}
            WHERE Product_Name = '{self.product_name}'
        """
        return Database.connect(query, "update")

    def delete(self):
        query = f"""
            DELETE FROM {self.table_name}
            WHERE Product_Name = '{self.product_name}'
        """
        return Database.connect(query, "delete")

    @staticmethod
    def join_with_categories():
        query = f"""
            SELECT p.Product_Name, p.Price, p.Quantity, c.Category_Name
            FROM {Product.table_name} p
            INNER JOIN Categories c ON p.Category_ID = c.Category_ID
        """
        return Database.connect(query, "select")


class Customer:
    table_name = "Customers"

    def __init__(self, name, contact_number, email):
        self.name = name
        self.contact_number = contact_number
        self.email = email

    def insert(self):
        query = f"""
            INSERT INTO {self.table_name} (Name, Contact_Number, Email)
            VALUES ('{self.name}', '{self.contact_number}', '{self.email}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def select_all():
        query = f"SELECT * FROM {Customer.table_name}"
        return Database.connect(query, "select")

    def update_email(self, new_email):
        query = f"""
            UPDATE {self.table_name}
            SET Email = '{new_email}'
            WHERE Name = '{self.name}'
        """
        return Database.connect(query, "update")

    def delete(self):
        query = f"""
            DELETE FROM {self.table_name}
            WHERE Name = '{self.name}'
        """
        return Database.connect(query, "delete")


class Transaction:
    table_name = "Transactions"

    def __init__(self, store_id, customer_id, transaction_date, total_amount):
        self.store_id = store_id
        self.customer_id = customer_id
        self.transaction_date = transaction_date
        self.total_amount = total_amount

    def insert(self):
        query = f"""
            INSERT INTO {self.table_name} (Store_ID, Customer_ID, Transaction_Date, Total_Amount)
            VALUES ({self.store_id}, {self.customer_id}, '{self.transaction_date}', {self.total_amount})
        """
        return Database.connect(query, "insert")

    @staticmethod
    def select_all():
        query = f"SELECT * FROM {Transaction.table_name}"
        return Database.connect(query, "select")

    def update_total_amount(self, new_amount):
        query = f"""
            UPDATE {self.table_name}
            SET Total_Amount = {new_amount}
            WHERE Store_ID = {self.store_id} AND Customer_ID = {self.customer_id}
        """
        return Database.connect(query, "update")

    def delete(self):
        query = f"""
            DELETE FROM {self.table_name}
            WHERE Store_ID = {self.store_id} AND Customer_ID = {self.customer_id}
        """
        return Database.connect(query, "delete")


class Employee:
    table_name = "Employees"

    def __init__(self, name, position, store_id, salary):
        self.name = name
        self.position = position
        self.store_id = store_id
        self.salary = salary

    def insert(self):
        query = f"""
            INSERT INTO {self.table_name} (Name, Position, Store_ID, Salary)
            VALUES ('{self.name}', '{self.position}', {self.store_id}, {self.salary})
        """
        return Database.connect(query, "insert")

    @staticmethod
    def select_all():
        query = f"SELECT * FROM {Employee.table_name}"
        return Database.connect(query, "select")

    def update_salary(self, new_salary):
        query = f"""
            UPDATE {self.table_name}
            SET Salary = {new_salary}
            WHERE Name = '{self.name}'
        """
        return Database.connect(query, "update")

    def delete(self):
        query = f"""
            DELETE FROM {self.table_name}
            WHERE Name = '{self.name}'
        """
        return Database.connect(query, "delete")


class Supplier:
    table_name = "Suppliers"

    def __init__(self, supplier_name, contact_number):
        self.supplier_name = supplier_name
        self.contact_number = contact_number

    def insert(self):
        query = f"""
            INSERT INTO {self.table_name} (Supplier_Name, Contact_Number)
            VALUES ('{self.supplier_name}', '{self.contact_number}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def select_all():
        query = f"SELECT * FROM {Supplier.table_name}"
        return Database.connect(query, "select")

    def update_contact_number(self, new_contact_number):
        query = f"""
            UPDATE {self.table_name}
            SET Contact_Number = '{new_contact_number}'
            WHERE Supplier_Name = '{self.supplier_name}'
        """
        return Database.connect(query, "update")

    def delete(self):
        query = f"""
            DELETE FROM {self.table_name}
            WHERE Supplier_Name = '{self.supplier_name}'
        """
        return Database.connect(query, "delete")


class SupplierProduct:
    table_name = "Supplier_Products"

    def __init__(self, supplier_id, product_id):
        self.supplier_id = supplier_id
        self.product_id = product_id

    def insert(self):
        query = f"""
            INSERT INTO {self.table_name} (Supplier_ID, Product_ID)
            VALUES ({self.supplier_id}, {self.product_id})
        """
        return Database.connect(query, "insert")

    @staticmethod
    def select_all():
        query = f"SELECT * FROM {SupplierProduct.table_name}"
        return Database.connect(query, "select")

    def delete(self):
        query = f"""
            DELETE FROM {self.table_name}
            WHERE Supplier_ID = {self.supplier_id} AND Product_ID = {self.product_id}
        """
        return Database.connect(query, "delete")


class TransactionItem:
    table_name = "Transactions_Items"

    def __init__(self, transaction_id, product_id, quantity, unit_price):
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price

    def insert(self):
        query = f"""
            INSERT INTO {self.table_name} (Transaction_ID, Product_ID, Quantity, Unit_Price)
            VALUES ({self.transaction_id}, {self.product_id}, {self.quantity}, {self.unit_price})
        """
        return Database.connect(query, "insert")

    @staticmethod
    def select_all():
        query = f"SELECT * FROM {TransactionItem.table_name}"
        return Database.connect(query, "select")

    def update_quantity(self, new_quantity):
        query = f"""
            UPDATE {self.table_name}
            SET Quantity = {new_quantity}
            WHERE Transaction_ID = {self.transaction_id} AND Product_ID = {self.product_id}
        """
        return Database.connect(query, "update")

    def delete(self):
        query = f"""
            DELETE FROM {self.table_name}
            WHERE Transaction_ID = {self.transaction_id} AND Product_ID = {self.product_id}
        """
        return Database.connect(query, "delete")


class Promotion:
    table_name = "Promotions"

    def __init__(self, promotion_name, description, start_date, end_date):
        self.promotion_name = promotion_name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def insert(self):
        query = f"""
            INSERT INTO {self.table_name} (Promotion_Name, Description, Start_Date, End_Date)
            VALUES ('{self.promotion_name}', '{self.description}', '{self.start_date}', '{self.end_date}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def select_all():
        query = f"SELECT * FROM {Promotion.table_name}"
        return Database.connect(query, "select")

    def update_description(self, new_description):
        query = f"""
            UPDATE {self.table_name}
            SET Description = '{new_description}'
            WHERE Promotion_Name = '{self.promotion_name}'
        """
        return Database.connect(query, "update")

    def delete(self):
        query = f"""
            DELETE FROM {self.table_name}
            WHERE Promotion_Name = '{self.promotion_name}'
        """
        return Database.connect(query, "delete")

