from sat_online_market import user_input_saver
from sat_online_market import Id_Generator, display_product_list
from tabulate import tabulate

def get_matching_products(product_list, user_input):
    return [product for product in product_list.keys() if user_input in product.lower()]

def choose_product(matching_products):
    if matching_products:
        print("Matching Products:")
        for i, product in enumerate(matching_products, 1):
            print(f"{i}. {product}")
        product_choice = input("Enter the number of the product you want to order: ")
        if product_choice.isdigit() and 1 <= int(product_choice) <= len(matching_products):
            return matching_products[int(product_choice) - 1]
    return None

def handle_order(product_list, prices, chosen_product):
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
            order_id = Id_Generator()
            user_input_saver(order_id, chosen_product, price_1, user_ip, total_price, us_name, us_state, us_dist, us_city, us_pin)
            print("Operation Menu : \n\t[PRESS 1] : To Access Bill\n\t[PRESS 0] : To Access Personal & Order Details")
            choice_2 = int(input("Enter Your Choice: "))
            if choice_2 == 1:
                display_bill(chosen_product, price_1, user_ip, total_price)
            elif choice_2 == 0:
                print(f" • Order Details :\n • Product Name : {chosen_product}\n • Name :{us_name}\n • State :{us_state}\n • District :{us_dist}\n • City:{us_city}\n • Pinvode :{us_pin} ")
                print(f"::::::::Order ID:::::::::\n(You Easily Track Your Product Using Order ID)\nOrder ID : {order_id}")
            else:
                print("Invalid choice!")
        elif choice == 0:
            shopping_process()
        else:
            print("Invalid choice!")
    else:
        print("OUT OF STOCK")

def display_bill(product, price, quantity, total):
    print("       :::::::::::Bill:::::::::::")
    bill_data = [[product, price, quantity, total]]
    bill_header = ["Product", "Price", "Quantity", "Total Amount"]
    print(tabulate(bill_data, headers=bill_header, tablefmt="grid"))

def check_availability_and_order(product_list, prices):
    user_input = input("To Check Whether Product Available Or Not, Enter Product Name: ").lower()
    matching_products = get_matching_products(product_list, user_input)
    chosen_product = choose_product(matching_products)
    if chosen_product:
        if chosen_product in prices:
            handle_order(product_list, prices, chosen_product)
        else:
            print("Price not found for chosen product.")
    else:
        print("Invalid product choice!")

def shopping_process(iPhoneList, WatchList, AirpodesList, iPhonePrice, WatchPrice, AirpodesPrice):
    exit_var = 1
    while exit_var != 0:
        print("Product Available At SAT Mobile Shopee")
        print("● SmartPhone[PRESS 1]\n● Watch     [PRESS 2]\n● Airpodes  [PRESS 3]\n● MacBook   [PRESS 4]")
        choice_3 = int(input("Enter Your Choice: "))
        if choice_3 == 1:
            print("  ::::::::::SmartPhone:::::::::")
            print(" ")
            display_product_list(iPhoneList, iPhonePrice)
            check_availability_and_order(iPhoneList, iPhonePrice)
        elif choice_3 == 2:
            print("  ::::::::::Watch:::::::::")
            print(" ")
            display_product_list(WatchList, WatchPrice)
            check_availability_and_order(WatchList, WatchPrice)
        elif choice_3 == 3:
            print("  ::::::::::Airpodes:::::::::")
            print(" ")
            display_product_list(AirpodesList, AirpodesPrice)
            check_availability_and_order(AirpodesList, AirpodesPrice)
        else:
            print("Invalid Choice")
        exit_var = int(input("Operation Menu : \n[PRESS 1] : Continue Shopping \n[PRESS 0] : Exit\n "))

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
