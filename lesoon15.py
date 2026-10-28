prices = [8.50, 42.00, 12.00, 95.00, 15.00, 25.50]
result = list(map(lambda p: round(p * 1.10, 2), filter(lambda p: p >= 15.00, prices)))
result2 = [round(p * 1.10, 2) for p in prices if p >= 15.00]
print (result)
print (result2)
    