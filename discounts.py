def apply_discounts(prices, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        return "Invalid discount"
    return   [round(price * (1 - discount_percent / 100), 2) for price in prices]
