from random import randint

def Id_Generator():
    order_id = randint(100000, 999999)
    return order_id

def display_product_list(product, prices):
    for product, price in prices.items():
        print(f"● Product: {product}\n  Price : ₹{price}/-")
        print(" ")
