def countdown(n):
    if n == 0:
        print("Liftoff!")
        return
    print(n)
    return countdown(n - 1)
countdown(5)