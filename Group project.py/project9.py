import random
def My9_program():
    guessed = random.randint(1, 9)

    while True: 
        user = int(input("type number: "))
        if user > guessed:
            print("Guessed Too High.")
            continue
        elif user < guessed:
            print("Guessed Too Low.")
            continue
        elif user == guessed:
            print("Correct Guess.")


        play_again = input("Do you want to continue?Y/N ")
        if play_again == "y":
            continue
        elif play_again == "n":
            break
My9_program()

