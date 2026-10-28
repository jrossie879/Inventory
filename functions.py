def calculate_item_total(price, quantity=1, tax_rate = 0.07,discount = 0.0):
    price = float(price)
    subtotal = price * quantity
    discountedsubtotal = subtotal - discount
    tax = discountedsubtotal * tax_rate
    finaltotal = discountedsubtotal  + tax 
    print(round(finaltotal, 2))

calculate_item_total(15, 3)
calculate_item_total(50.00, 1, 0.05, 10.00)
calculate_item_total(20.00, 2, 0.10, 5.00)


def print_receipt(item_name, total_price, currency="$"):
    print(f"Receipt: {item_name} | Final Total: {currency}{total_price}")

