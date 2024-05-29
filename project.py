from classes import Store,Category,Product,Customer,Transaction,Employee,Supplier,SupplierProduct,TransactionItem,Promotion


def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. Add Customer")
        print("2. View All Customers")
        print("3. Update Customer Email")
        print("4. Delete Customer")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            contact_number = input("Enter customer contact number: ")
            email = input("Enter customer email: ")
            customer_obj = Customer(name, contact_number, email)
            print(customer_obj.insert())

        elif choice == "2":
            print(Customer.select_all())

        elif choice == "3":
            name = input("Enter customer name: ")
            new_email = input("Enter new email: ")
            customer_obj = Customer(name, "", "")
            print(customer_obj.update_email(new_email))

        elif choice == "4":
            name = input("Enter customer name to delete: ")
            customer_obj = Customer(name, "", "")
            print(customer_obj.delete())

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

def transaction_menu():
    while True:
        print("\nTransaction Menu:")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. Update Transaction Total Amount")
        print("4. Delete Transaction")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            store_id = int(input("Enter store ID: "))
            customer_id = int(input("Enter customer ID: "))
            transaction_date = input("Enter transaction date (YYYY-MM-DD): ")
            total_amount = float(input("Enter total amount: "))
            transaction_obj = Transaction(store_id, customer_id, transaction_date, total_amount)
            print(transaction_obj.insert())

        elif choice == "2":
            print(Transaction.select_all())

        elif choice == "3":
            store_id = int(input("Enter store ID of transaction: "))
            customer_id = int(input("Enter customer ID of transaction: "))
            new_amount = float(input("Enter new total amount: "))
            transaction_obj = Transaction(store_id, customer_id, "", 0)
            print(transaction_obj.update_total_amount(new_amount))

        elif choice == "4":
            store_id = int(input("Enter store ID of transaction to delete: "))
            customer_id = int(input("Enter customer ID of transaction to delete: "))
            transaction_obj = Transaction(store_id, customer_id, "", 0)
            print(transaction_obj.delete())

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

def employee_menu():
    while True:
        print("\nEmployee Menu:")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee Salary")
        print("4. Delete Employee")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            store_id = int(input("Enter store ID: "))
            salary = float(input("Enter employee salary: "))
            employee_obj = Employee(name, position, store_id, salary)
            print(employee_obj.insert())

        elif choice == "2":
            print(Employee.select_all())

        elif choice == "3":
            name = input("Enter employee name: ")
            new_salary = float(input("Enter new salary: "))
            employee_obj = Employee(name, "", 0, 0)
            print(employee_obj.update_salary(new_salary))

        elif choice == "4":
            name = input("Enter employee name to delete: ")
            employee_obj = Employee(name, "", 0, 0)
            print(employee_obj.delete())

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")



def supplier_menu():
    while True:
        print("\nSupplier Menu:")
        print("1. Add Supplier")
        print("2. View All Suppliers")
        print("3. Update Supplier Contact Number")
        print("4. Delete Supplier")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter supplier name: ")
            contact_number = input("Enter supplier contact number: ")
            supplier_obj = Supplier(name, contact_number)
            print(supplier_obj.insert())

        elif choice == "2":
            print(Supplier.select_all())

        elif choice == "3":
            name = input("Enter supplier name: ")
            new_contact_number = input("Enter new contact number: ")
            supplier_obj = Supplier(name, "")
            print(supplier_obj.update_contact_number(new_contact_number))

        elif choice == "4":
            name = input("Enter supplier name to delete: ")
            supplier_obj = Supplier(name, "")
            print(supplier_obj.delete())

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


def supplier_product_menu():
    while True:
        print("\nSupplier Product Menu:")
        print("1. Add Supplier Product")
        print("2. View All Supplier Products")
        print("3. Delete Supplier Product")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            supplier_id = int(input("Enter supplier ID: "))
            product_id = int(input("Enter product ID: "))
            supplier_product_obj = SupplierProduct(supplier_id, product_id)
            print(supplier_product_obj.insert())

        elif choice == "2":
            print(SupplierProduct.select_all())

        elif choice == "3":
            supplier_id = int(input("Enter supplier ID: "))
            product_id = int(input("Enter product ID: "))
            supplier_product_obj = SupplierProduct(supplier_id, product_id)
            print(supplier_product_obj.delete())

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


def transaction_item_menu():
    while True:
        print("\nTransaction Item Menu:")
        print("1. Add Transaction Item")
        print("2. View All Transaction Items")
        print("3. Update Transaction Item Quantity")
        print("4. Delete Transaction Item")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            transaction_id = int(input("Enter transaction ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            unit_price = float(input("Enter unit price: "))
            transaction_item_obj = TransactionItem(transaction_id, product_id, quantity, unit_price)
            print(transaction_item_obj.insert())

        elif choice == "2":
            print(TransactionItem.select_all())

        elif choice == "3":
            transaction_id = int(input("Enter transaction ID: "))
            product_id = int(input("Enter product ID: "))
            new_quantity = int(input("Enter new quantity: "))
            transaction_item_obj = TransactionItem(transaction_id, product_id, 0, 0)
            print(transaction_item_obj.update_quantity(new_quantity))

        elif choice == "4":
            transaction_id = int(input("Enter transaction ID: "))
            product_id = int(input("Enter product ID: "))
            transaction_item_obj = TransactionItem(transaction_id, product_id, 0, 0)
            print(transaction_item_obj.delete())

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

def promotion_menu():
    while True:
        print("\nPromotion Menu:")
        print("1. Add Promotion")
        print("2. View All Promotions")
        print("3. Update Promotion Description")
        print("4. Delete Promotion")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter promotion name: ")
            description = input("Enter promotion description: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            promotion_obj = Promotion(name, description, start_date, end_date)
            print(promotion_obj.insert())

        elif choice == "2":
            print(Promotion.select_all())

        elif choice == "3":
            name = input("Enter promotion name: ")
            new_description = input("Enter new description: ")
            promotion_obj = Promotion(name, "", "", "")
            print(promotion_obj.update_description(new_description))

        elif choice == "4":
            name = input("Enter promotion name to delete: ")
            promotion_obj = Promotion(name, "", "", "")
            print(promotion_obj.delete())

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

def store_menu():
    while True:
        print("\nStore Menu:")
        print("1. Add Store")
        print("2. View All Stores")
        print("3. Update Store Location")
        print("4. Delete Store")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            store_name = input("Enter store name: ")
            location = input("Enter store location: ")
            contact_number = input("Enter store contact number: ")
            store_obj = Store(store_name, location, contact_number)
            print(store_obj.insert())

        elif choice == "2":
            print(Store.select_all())

        elif choice == "3":
            store_name = input("Enter store name: ")
            new_location = input("Enter new location: ")
            store_obj = Store(store_name, "", "")
            print(store_obj.update_location(new_location))

        elif choice == "4":
            store_name = input("Enter store name to delete: ")
            store_obj = Store(store_name, "", "")
            print(store_obj.delete())

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


def category_menu():
    while True:
        print("\nCategory Menu:")
        print("1. Add Category")
        print("2. View All Categories")
        print("3. Update Category Name")
        print("4. Delete Category")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            category_name = input("Enter category name: ")
            category_obj = Category(category_name)
            print(category_obj.insert())

        elif choice == "2":
            print(Category.select_all())

        elif choice == "3":
            category_name = input("Enter category name: ")
            new_name = input("Enter new category name: ")
            category_obj = Category(category_name)
            print(category_obj.update_category_name(new_name))

        elif choice == "4":
            category_name = input("Enter category name to delete: ")
            category_obj = Category(category_name)
            print(category_obj.delete())

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


def product_menu():
    while True:
        print("\nProduct Menu:")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Update Product Quantity")
        print("4. Delete Product")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_name = input("Enter product name: ")
            category_id = int(input("Enter category ID: "))
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product_obj = Product(product_name, category_id, price, quantity)
            print(product_obj.insert())

        elif choice == "2":
            print(Product.select_all())

        elif choice == "3":
            product_name = input("Enter product name: ")
            new_quantity = int(input("Enter new quantity: "))
            product_obj = Product(product_name, 0, 0.0, 0)
            print(product_obj.update_quantity(new_quantity))

        elif choice == "4":
            product_name = input("Enter product name to delete: ")
            product_obj = Product(product_name, 0, 0.0, 0)
            print(product_obj.delete())

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\n Assalomu alaykum Korzinka.uz ning ma'lumotlar bazasiga xush kelibsiz 👨‍💻:")
        print("1. Customer Menu")
        print("2. Transaction Menu")
        print("3. Employee Menu")
        print("4. Supplier Menu")
        print("5. Supplier Product Menu")
        print("6. Transaction Item Menu")
        print("7. Promotion Menu")
        print("8. Store Menu")
        print("9. Category Menu")
        print("10. Product Menu")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer_menu()

        elif choice == "2":
            transaction_menu()

        elif choice == "3":
            employee_menu()

        elif choice == "4":
            supplier_menu()

        elif choice == "5":
            supplier_product_menu()

        elif choice == "6":
            transaction_item_menu()

        elif choice == "7":
            promotion_menu()
        elif choice == "8":
            store_menu()
        elif choice == "9":
            category_menu()
        elif choice == "10":
            product_menu()

        elif choice == "0":
            print("Exiting..............")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


