print("Rock...")
print("Paper...")
print("Scissors..")

player1 = input("Player 1, rock, paper, or scissors? ")
print("-----------------------------------------------------\n" * 15)
print("-------------------- NO CHEATING --------------------\n")
print("-----------------------------------------------------\n" * 15)
player2 = input("Player 2, rock, paper, or scissors? ")

if player1 == player2:
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins!")
    elif player2 == "paper":
        print("Player 2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins!")
    elif player2 == "scissors":
        print("Player 2 wins!")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1 wins!")
    elif player2 == "rock":
        print("Player 2 wins!")
else:
    print("Something went wrong")

