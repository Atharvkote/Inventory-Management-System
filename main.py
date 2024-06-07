from customer import shopping_process, track_order 
from admin import status_updation_menu, stock_upadation_menu, login_process
from database import read_data_from_csv

iPhoneList=read_data_from_csv('iPhoneData.csv')
WatchList=read_data_from_csv('WatchData.csv')
AirpodesList=read_data_from_csv('AirpodesData.csv')
iPhonePrice=read_data_from_csv('iPhonePriceData.csv')
WatchPrice=read_data_from_csv('WatchPriceData.csv')
AirpodesPrice=read_data_from_csv('AirpodesPriceData.csv')
def main():
    choice = int(input("[PRESS 1] : ADMIN ACCESS\n[PRESS 2] : Continue as a Customer\n"))

    if choice == 2:
        print("[PRESS 1] : Access Products Available\n[PRESS 2] : Track My Order Product\n")
        choice_4 = int(input("Enter Your Choice: "))
        if choice_4 == 1:
            shopping_process(iPhoneList, iPhonePrice ,WatchList,WatchPrice, AirpodesList,AirpodesPrice  )
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
                stock_upadation_menu()
            elif choice_4 == 2:
                status_updation_menu()  # Ensure you have this function in the appropriate module
            else:
                print("Invalid Choice")
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()
