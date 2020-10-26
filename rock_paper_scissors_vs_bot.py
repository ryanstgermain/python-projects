from random import randint

player_wins = 0
computer_wins = 0
rounds = 3

print(f"Best out of {rounds}.")

while player_wins < rounds and computer_wins < rounds:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    player = input("Rock, paper, or scissors? ").lower()
    random_num = randint(0, 2)

    if player == "quit" or player == "q":
        break
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
            player_wins += 1
        else:
            print("The bot wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("You win!")
            player_wins += 1
        else:
            print("The bot wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
            player_wins += 1
        else:
            print("The bot wins!")
            computer_wins += 1
    else:
        print("Please enter a valid move.")

if player_wins > computer_wins:
    print("Congrats, you won!")
elif player_wins == computer_wins:
    print("The game is a tie.")
else:
    print("Computer wins.")

