def Mysixth_program():
    user = input("type pre-order: ")
    if user == user[::-1]:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
Mysixth_program()