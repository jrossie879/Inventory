def My8_program():
    while True:
        player_1 = input("Player 1. Rock, Paper or Scissors. ")
        player_2 = input("Player 2. Rock, Paper or Scissors. ")

        if player_1 == player_2:
            print("It's a tie. ")
        elif player_1 == 'rock':
            if player_2 == 'scissors':
                print("Rock beats Scissors. Player 1 wins.")
            else:
                print("Player 2 wins.")
        elif player_1 == 'paper':
            if player_2 == 'rock':
                print("Paper beats Rock. Player 1 wins.")
            else:
                print("Player 2 wins.")
        elif player_1 == 'scissors':
            if player_2 == 'paper':
                print("Scissors beats Paper. Player 1 wins.")
            else: 
                print("Player 2 wins.")
        else:
            print("Please pick one option.")
        play_again = input("Do you want to play again.? (yes/no): ")
        if play_again != 'yes':
            print("Thank you for playing! Come again!")
            break
            

My8_program()
