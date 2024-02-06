catalogue = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

discount_rules = {
    "flat_10_discount": 200,
    "bulk_5_discount": 10,
    "bulk_10_discount": 20,
    "tiered_50_discount": 30
}

gift_wrapfee = 1
shipping_feepackage = 5
units_package = 10

def calculate_discounteprice(quantity, price):
    total_price = quantity * price

 
    if quantity > discount_rules["tiered_50_discount"] and quantity > 15:
        return quantity * price - ((quantity - 15) * price * 0.5)
    elif quantity > discount_rules["bulk_10_discount"]:
        return total_price * 0.9
    elif quantity > discount_rules["bulk_5_discount"]:
        return total_price * 0.95
    elif total_price > discount_rules["flat_10_discount"]:
        return total_price - 10
    else:
        return total_price

def calculate_shippingfee(quantity):
    return (quantity // units_package) * shipping_feepackage

def calculate_totalamount(products):
    subtotal = 0
    discount_name = ""
    discount_amount = 0
    shipping_fee = 0
    gift_wrap_fee_total = 0

    for product, quantity, gift_wrapped in products:
        price = catalogue[product]
        total_price = calculate_discounteprice(quantity, price)
        subtotal += total_price

       
        if quantity > discount_rules["tiered_50_discount"] and quantity > 15:
            discount_name = "tiered_50_discount"
            discount_amount = (quantity - 15) * price * 0.5
        elif quantity > discount_rules["bulk_10_discount"]:
            discount_name = "bulk_10_discount"
            discount_amount = total_price * 0.1
        elif quantity > discount_rules["bulk_5_discount"]:
            discount_name = "bulk_5_discount"
            discount_amount = total_price * 0.05
        elif total_price > discount_rules["flat_10_discount"]:
            discount_name = "flat_10_discount"
            discount_amount = 10

        shipping_fee += calculate_shippingfee(quantity)

        if gift_wrapped:
            gift_wrap_fee_total += quantity * gift_wrapfee

    total = subtotal - discount_amount + shipping_fee + gift_wrap_fee_total

    return subtotal, discount_name, discount_amount, shipping_fee, gift_wrap_fee_total, total

def get_userinput():
    products = []
    for product in catalogue.keys():
        quantity = int(input(f"Enter quantity of {product}: "))
        gift_wrapped = int(input(f"Is {product} wrapped as a gift? (1 for Yes, 0 for No): "))
        products.append((product, quantity, bool(gift_wrapped)))
    return products

def display(products, subtotal, discount_name, discount_amount, shipping_fee, gift_wrap_fee_total, total):
    print("Product\t\tQuantity\tTotal Amount")
    for product, quantity, _ in products:
        price = catalogue[product]
        total_price = calculate_discounteprice(quantity, price)
        print(f"{product}\t\t{quantity}\t\t{total_price}")

    print(f"\nSubtotal: {subtotal}")
    print(f"Discount Applied: {discount_name} (${discount_amount})")
    print(f"Shipping Fee: {shipping_fee}")
    print(f"Gift Wrap Fee: {gift_wrap_fee_total}")
    print(f"Total: {total}")

if __name__ == "__main__":
    user_products = get_userinput()
    subtotal, discount_name, discount_amount, shipping_fee, gift_wrap_fee_total, total = calculate_totalamount(user_products)
    display(user_products, subtotal, discount_name, discount_amount, shipping_fee, gift_wrap_fee_total, total)

