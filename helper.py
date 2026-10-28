def calculate_discounted_total(price, quantity, discount_rate, delivery_fee):
    subtotal = price * quantity
    discount_amount = subtotal * discount_rate
    discounted_subtotal = subtotal - discount_amount
    total = delivery_fee + discounted_subtotal
    return total




print(calculate_discounted_total(100, 3, 0.10, 50))
print(calculate_discounted_total(500, 2, 0.20, 200))
