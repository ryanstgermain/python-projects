from random import randint

player = input("Rock, paper, or scissors? ").lower()
random_num = randint(0, 2)

if random_num == 0:
    computer = "rock"
elif random_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer chooses {computer}.")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("The bot wins!")
elif player == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("The bot wins!")
elif player == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("The bot wins!")
else:
    print("Please enter a valid move.")

