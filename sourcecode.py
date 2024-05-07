import csv
from random import randint
from tabulate import tabulate

admin_credentials = {
    
    'Atharva@123': '74',  # Admin 1
    'Sairaj@123': '92',   # Admin 2
    'Tushar@123': '90'    # Admin 3
    
}
# Function to read data from CSV file and initialize dictionary
def read_data_from_csv(filename):
    data = {}
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # To Skip header row
        for row in reader:
            data[row[0]] = int(row[1])  
    return data

iPhoneList = read_data_from_csv('iPhoneData.csv')
AirpodesList = read_data_from_csv('AirpodesData.csv')
WatchList = read_data_from_csv('WatchData.csv')
iPhonePrice = read_data_from_csv('iPhonePriceData.csv')
WatchPrice = read_data_from_csv('WatchPriceData.csv')
AirpodesPrice = read_data_from_csv('AirpodesPriceData.csv')

def Id_Generator():
    order_id = randint(100000, 999999)
    return order_id

def display_product_list(product, prices):
    for product, price in prices.items():
        print(f"● Product: {product}\n  Price : ₹{price}/-")
        print(" ")

def user_input_saver(Ordername, price_1, user_ip, total_price, us_name, us_state, us_dist, us_city, us_pin):
    global order_id
    order_id = Id_Generator()
    file_name = 'DataBase.csv'
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Order ID', 'Product', 'Price', 'Quantity', 'Amount', 'Customer Name', 'State', 'District', 'City', 'Pincode'])
        writer.writerow([order_id, Ordername, price_1, user_ip, total_price, us_name, us_state, us_dist, us_city, us_pin])

def check_availability_and_order(product_list, order_list, prices):
    user_input = input("To Check Whether Product Available Or Not, Enter Product Name: ").lower()
    matching_products = [product for product in product_list.keys() if user_input in product.lower()]
    if matching_products:
        print("Matching Products:")
        for i, product in enumerate(matching_products, 1):
            print(f"{i}. {product}")

        product_choice = input("Enter the number of the product you want to order: ")
        if product_choice.isdigit() and 1 <= int(product_choice) <= len(matching_products):
            chosen_product = matching_products[int(product_choice) - 1]
            if chosen_product in prices:
                pro = product_list[chosen_product]
                user_ip = int(input("Enter Product Quantity: "))
                if user_ip <= pro:
                    print("Product is Available in Stock, You Can Proceed Further!")
                    print("Operation Menu : \n[PRESS 1] : To ORDER\n[PRESS 0] : To View Other Products")
                    choice = int(input("Enter Your Choice: "))
                    if choice == 1:
                        us_name = input("Enter Your Name: ")
                        us_state = input("Enter Your State Name: ")
                        us_dist = input("Enter Your District Name: ")
                        us_city = input("Enter Your City Name: ")
                        us_pin = int(input("Enter Your City PinCode: "))
                        print("Order Placed!")
                        price_1 = prices[chosen_product]  
                        total_price = (price_1 * user_ip)
                        product_list[chosen_product] -= user_ip
                        user_input_saver(chosen_product, price_1, user_ip, total_price, us_name, us_state, us_dist,
                                         us_city, us_pin)
                        print(
                            "Operation Menu : \n\t[PRESS 1] : To Access Bill\n\t[PRESS 0] : To Access Personal & "
                            "Order Details")
                        choice_2 = int(input("Enter Your Choice: "))
                        if choice_2 == 1:
                            print("       :::::::::::Bill:::::::::::")
                            bill_data = [[chosen_product, price_1, user_ip, total_price]]
                            bill_header = ["Product", "Price", "Quantity", "Total Amount"]
                            print(tabulate(bill_data, headers=bill_header, tablefmt="grid"))
                        elif choice_2 == 0:
                            print(
                                f" • Order Details :\n • Product Name : {chosen_product}\n • Name :{us_name}\n • "
                                f"State :{us_state}\n • District :{us_dist}\n • City:{us_city}\n • Pinvode :{us_pin} ")
                            print(
                                f"::::::::Order ID:::::::::\n(You Easily Track Your Product Using Order ID)\nOrder "
                                f"ID : {order_id}")
                        else:
                            print("Invalid choice!")
                    elif choice == 0:
                        shopping_process()
                    else:
                        print("Invalid choice!")
                else:
                    print("OUT OF STOCK")
            else:
                print("Price not found for chosen product.")
        else:
            print("Invalid product choice!")
    else:
        print("Product not found")
        
def shopping_process():
    exit_var = 1
    while exit_var != 0:
        print("Product Available At SAT Mobile Shopee")
        print("● SmartPhone[PRESS 1]\n● Watch     [PRESS 2]\n● Airpodes  [PRESS 3]\n● MacBook   [PRESS 4]")
        choice_3 = int(input("Enter Your Choice: "))
        if choice_3 == 1:
            print("  ::::::::::SmartPhone:::::::::")
            print(" ")
            display_product_list(iPhoneList, iPhonePrice)
            check_availability_and_order(iPhoneList, iPhoneList, iPhonePrice)
        elif choice_3 == 2:
            print("  ::::::::::Watch:::::::::")
            print(" ")
            display_product_list(WatchList, WatchPrice)
            check_availability_and_order(WatchList, WatchList, WatchPrice)
        elif choice_3 == 3:
            print("  ::::::::::Airpodes:::::::::")
            print(" ")
            display_product_list(AirpodesList, AirpodesPrice)
            check_availability_and_order(AirpodesList, AirpodesList, AirpodesPrice)
        else:
            print("Invalid Choice")
        exit_var = int(input("Operation Menu : \n[PRESS 1] : Continue Shopping \n[PRESS 0] : Exit\n "))

def login_process():
    max_attempts = 3
    login_attempts = 0
    while login_attempts < max_attempts:
        username = input("Enter Admin ID: ")
        password = input("Enter Password: ")

        if username in admin_credentials and admin_credentials[username] == password:
            print("Login Successful !!!")
            return True
        else:
            login_attempts += 1
            print("Invalid username or password. Please try again.")
            print(f"Remaining attempts: {max_attempts - login_attempts}")
    print("ACCESS DENIED !!!!!\nMaximum login attempts exceeded. Please try again later !!.")
    return False

def write_data_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product', 'Quantity'])  
        for product, quantity in data.items():
            writer.writerow([product, quantity])

def stock_updation(product_list, filename):
    user_input = input("Enter Name Of the Product Whose Stock YOU Want To Update : ").lower()
    matching_products = [product for product in product_list.keys() if user_input in product.lower()]

    if matching_products:
        print("Matching Products:")
        for i, product in enumerate(matching_products, 1):
            print(f"{i}. {product}")

        product_choice = input("Enter the number of the product you want to update: ")
        if product_choice.isdigit() and 1 <= int(product_choice) <= len(matching_products):
            chosen_product = matching_products[int(product_choice) - 1]
            added_stock = int(input("Enter Added Quantity of the Product : "))
            product_list[chosen_product] += added_stock
            print(f"{chosen_product} Stock Updated!")
            write_data_to_csv(filename, product_list)  
        else:
            print("Invalid product choice!")
    else:
        print("Product not found")

def stock_upadation_Menu():
    if login_process():
        print(":::::::::Stock Updation:::::::::::")
        print("To Update SmartPhone [PRESS 1]\nTo Update Watch  [PRESS 2]\nTo Update Airpodes  [PRESS 3]\nTo Update MacBook   [PRESS 4]")
        choice_3 = int(input("Enter Your Choice: "))     
        if choice_3 == 1:
            stock_updation(iPhoneList, 'iPhoneData.csv')   
        elif choice_3 == 2:
            stock_updation(WatchList, 'WatchData.csv')
        elif choice_3 == 3:
            stock_updation(AirpodesList, 'AirpodesData.csv')
        elif choice_3 == 4:
            stock_updation(AirpodesList, 'AirpodesData.csv') 
        else:
            print("Invalid Choice ")


def update_order_status(order_id, new_status):
    order_id = order_id.lower()  

    with open('DataBase.csv', mode='r') as file:
        reader = csv.DictReader(file)
        orders = list(reader)

    for order in orders:
        if order['Order ID'] == order_id:
            order['Status'] = new_status
            print(f"Status Updated!")
            break

    with open('DataBase.csv', mode='w', newline='') as file:
        fieldnames = ['Order ID', 'Product', 'Price', 'Quantity', 'Amount', 'Customer Name', 'State', 'District', 'City', 'Pincode', 'Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(orders)

def track_order(order_id):
    with open('DataBase.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for order in reader:
            if order['Order ID'] == order_id:
                print(f"Order ID: {order['Order ID']}")
                print(f"Product: {order['Product']}")
                print(f"Status: {order['Status']}")
                break
        else:
            print("Order not found.")

def status_updation_menu():
    order_id_by_admin = input("Enter Product ID: ").lower()

    new_status = input("Enter New Status (Company Outlet, Shipping, Out for Delivery): ")
    valid_statuses = ["Company Outlet", "Shipping", "Out for Delivery"]
    if new_status not in valid_statuses:
        print("Invalid status provided.")
        return

    update_order_status(order_id_by_admin, new_status)

# Main Interface

choice_2 = int(input("[PRESS 1] : ADMIN ACCESS\n[PRESS 2] : Continue as a Customer\n"))

# Customer Block
if choice_2 == 2:
    print("[PRESS 1] : Access Products Available \n[PRESS 2] : Track My Order Product\n")
    choice_4 = int(input("Enter Your Choice: "))
    if choice_4 == 1:
        shopping_process()
    elif choice_4 == 2:
         order_id_by_Customer = input("Enter Product ID: ")
         track_order(order_id_by_Customer)
    else:
         print("Invalid Choice ")

# Admin Block
elif choice_2 == 1:
    if login_process():
        print("[PRESS 1] : Stock Updation \n[PRESS 2] : Product Status Updation\n")
        choice_4 = int(input("Enter Your Choice: "))
        if choice_4 == 1:
            stock_upadation_Menu()
        elif choice_4 == 2:
            status_updation_menu()
        else:
            print("Invalid Choice ")
else:
    print("Invalid Choice ")
