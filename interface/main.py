from sat_online_market.customer import shopping_process, track_order
from sat_online_market.admin import stock_upadation_menu, login_process

def main():
    choice = int(input("[PRESS 1] : ADMIN ACCESS\n[PRESS 2] : Continue as a Customer\n"))

    if choice == 2:
        print("[PRESS 1] : Access Products Available\n[PRESS 2] : Track My Order Product\n")
        choice_4 = int(input("Enter Your Choice: "))
        if choice_4 == 1:
            shopping_process()
        elif choice_4 == 2:
            order_id_by_customer = input("Enter Product ID: ")
            track_order(order_id_by_customer)
        else:
            print("Invalid Choice")
    elif choice == 1:
        if login_process():
            print("[PRESS 1] : Stock Updation\n[PRESS 2] : Product Status Updation\n")
            choice_4 = int(input("Enter Your Choice: "))
            if choice_4 == 1:
                stock_upadation_menu(iPhoneList, WatchList, AirpodesList)
            elif choice_4 == 2:
                status_updation_menu()  # Ensure you have this function in the appropriate module
            else:
                print("Invalid Choice")
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()
