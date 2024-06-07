import csv

def read_data_from_csv(filename):
    data = {}
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # To Skip header row
        for row in reader:
            data[row[0]] = int(row[1])  
    return data

def user_input_saver(order_id, Ordername, price_1, user_ip, total_price, us_name, us_state, us_dist, us_city, us_pin):
    file_name = 'DataBase.csv'
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Order ID', 'Product', 'Price', 'Quantity', 'Amount', 'Customer Name', 'State', 'District', 'City', 'Pincode'])
        writer.writerow([order_id, Ordername, price_1, user_ip, total_price, us_name, us_state, us_dist, us_city, us_pin])

def write_data_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product', 'Quantity'])  
        for product, quantity in data.items():
            writer.writerow([product, quantity])
