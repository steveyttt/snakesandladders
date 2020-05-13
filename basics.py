import random

def roll():
    return(random.randint(1,6))

while True:

    Grid = 10

    if "Position" not in locals():
        print("Welcome to Snakes and Ladders!!")
        print("Roll the dice to begin!!")
        input("Hit any key to ROLLL or CTRL-C to cancel:")
        
        DiceRole = roll()
        Position = DiceRole
        print("You rolled a:", DiceRole)
        print("Your position on the grid is:", Position)

    input("Roll again?")
    DiceRole = roll()
    print("You rolled a:", DiceRole)
    Position = Position + DiceRole
    print("Your position on the grid is:", Position)

    if Position == Grid:
        print("You hit 10! congratulations!")
        print("Player wins")
        break
    elif Position > Grid:
        # print("You went past 10!")
        backstep = Position - Grid
        print(f"You went over the grid ({Grid}) by {backstep}")
        Position = Grid - backstep
        print("Your new position is:", Position)
