from manage import Database

def create_tables():
    tables = {
        "Stores": """
            CREATE TABLE Stores (
                Store_ID SERIAL PRIMARY KEY,
                Store_Name VARCHAR(255),
                Location VARCHAR(255),
                Contact_Number VARCHAR(20)
            )
        """,
        "Categories": """
            CREATE TABLE Categories (
                Category_ID SERIAL PRIMARY KEY,
                Category_Name VARCHAR(255)
            )
        """,
        "Products": """
            CREATE TABLE Products (
                Product_ID SERIAL PRIMARY KEY,
                Product_Name VARCHAR(255),
                Category_ID INT,
                Price DECIMAL(10, 2),
                Quantity_In_Stock INT,
                FOREIGN KEY (Category_ID) REFERENCES Categories(Category_ID)
            )
        """,
        "Customers": """
            CREATE TABLE Customers (
                Customer_ID SERIAL PRIMARY KEY,
                Name VARCHAR(255),
                Contact_Number VARCHAR(20),
                Email VARCHAR(255)
            )
        """,
        "Transactions": """
            CREATE TABLE Transactions (
                Transaction_ID SERIAL PRIMARY KEY,
                Store_ID INT,
                Customer_ID INT,
                Transaction_Date DATE,
                Total_Amount DECIMAL(10, 2),
                FOREIGN KEY (Store_ID) REFERENCES Stores(Store_ID),
                FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID)
            )
        """,
        "Employees": """
            CREATE TABLE Employees (
                Employee_ID SERIAL PRIMARY KEY,
                Name VARCHAR(255),
                Position VARCHAR(255),
                Store_ID INT,
                Salary DECIMAL(10, 2),
                FOREIGN KEY (Store_ID) REFERENCES Stores(Store_ID)
            )
        """,
        "Suppliers": """
            CREATE TABLE Suppliers (
                Supplier_ID SERIAL PRIMARY KEY,
                Supplier_Name VARCHAR(255),
                Contact_Number VARCHAR(20)
            )
        """,
        "Supplier_Products": """
            CREATE TABLE Supplier_Products (
                Supplier_Product_ID SERIAL PRIMARY KEY,
                Supplier_ID INT,
                Product_ID INT,
                FOREIGN KEY (Supplier_ID) REFERENCES Suppliers(Supplier_ID),
                FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
            )
        """,
        "Transactions_Items": """
            CREATE TABLE Transactions_Items (
                Transaction_Item_ID SERIAL PRIMARY KEY,
                Transaction_ID INT,
                Product_ID INT,
                Quantity INT,
                Unit_Price DECIMAL(10, 2),
                FOREIGN KEY (Transaction_ID) REFERENCES Transactions(Transaction_ID),
                FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
            )
        """,
        "Promotions": """
            CREATE TABLE Promotions (
                Promotion_ID SERIAL PRIMARY KEY,
                Promotion_Name VARCHAR(255),
                Description TEXT,
                Start_Date DATE,
                End_Date DATE
            )
        """
    }

    for table_name, query in tables.items():
        print(f"{table_name}: {Database.connect(query, 'create')}")


if __name__ == "__main__":
    create_tables()
