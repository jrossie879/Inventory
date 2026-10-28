def Mysecond_program():
    num = int(input("type num: "))
    check = int(input("type check: "))
    if num % 4 == 0:
        print("Number is divisible by 4.")
    if num % 2 == 0:  
        print("Number is even")
    else:
        print("Number is odd.")
    if check % num == 0:
        print(True)
    else:
        print(False)

Mysecond_program()