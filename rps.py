from random import randint

t = ["Rock", "Paper", "Scissors"]

while True:
    computer = t[randint(0, 2)]
    player = False

    while player==False:
        player = input("Enter your choice?: ").capitalize()  # Convert player input to uppercase
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")

    ans = int(input("Do you want to play again? (1 for yes, 0 for no): "))
    if ans != 1:
        print("Game end")
        break
