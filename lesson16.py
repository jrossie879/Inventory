products = [
    ("Laptop", 1200, 4.5),
    ("Mouse", 25, 4.8),
    ("Monitor", 300, 4.2),
    ("Keyboard", 75, 4.8)
]


sorted_by_price = sorted(products, key=lambda p: p[1])


highest_rated = max(products, key=lambda p: p[2])

print("Sorted by Price:", sorted_by_price)
print("Highest Rated:", highest_rated)