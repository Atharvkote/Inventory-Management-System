from sat_online_market import write_data_to_csv, read_data_from_csv

admin_credentials = { 
    'Atharva@123': '74',  # Admin 1
    'Sairaj@123': '92',   # Admin 2
    'Tushar@123': '90'    # Admin 3   
}

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

def stock_upadation_menu():
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

def status_updation_menu():
    order_id_by_admin = input("Enter Product ID: ").lower()

    new_status = input("Enter New Status (Company Outlet, Shipping, Out for Delivery): ")
    valid_statuses = ["Company Outlet", "Shipping", "Out for Delivery"]
    if new_status not in valid_statuses:
        print("Invalid status provided.")
        return

    update_order_status(order_id_by_admin, new_status)
