import random

def roll():
    return(random.randint(1,6))

def gridcheck(Position):

    snakes = {
        23: 9,
        16: 6,
        20: 4,
    }

    ladders = {
        3: 14,
        13: 19,
        10: 21,
    }

    for key, value in snakes.items():
        if Position == key:
            print(f"You have landed on {Position} and hit a SNAKE!!!")
            Position = value
            print(f"Slither on down to {Position}")
            return Position

    for key, value in ladders.items():
        if Position == key:
            print(f"You have landed on {Position} and hit a LADDER!!!")
            Position = value
            print(f"Climb on up to {Position}")
            return Position

    return Position

# print(gridcheck(3))


while True:

    Grid = 25

    if "Position" not in locals():
        print("Welcome to Snakes and Ladders!!")
        print("Roll the dice to begin!!")
        input("Hit any key to ROLLL or CTRL-C to cancel:")
        
        DiceRole = roll()
        Position = DiceRole
        print(f"You rolled a: {DiceRole}")
        print(f"Your position on the grid is: {Position}")
        Position = gridcheck(Position)


    elif Position > Grid:
        backstep = Position - Grid
        print(f"You went over the grids maximum size! ({Grid}) by {backstep}")
        Position = Grid - backstep
        print(f"Your new position is: {Position}")
        Position = gridcheck(Position)

    elif Position == Grid:
        print(f"You hit {Grid}! congratulations!")
        print("Player wins")
        break

    input("Roll again?")
    DiceRole = roll()
    print("You rolled a:", DiceRole)
    Position = Position + DiceRole
    print("Your position on the grid is:", Position)
    Position = gridcheck(Position)

