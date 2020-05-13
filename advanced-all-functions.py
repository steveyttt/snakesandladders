import random

## roll simulates a 1d6 dice roll and takes a Position parameter as the starting coordinate.
## should return the value of the dice roll + the existing grid location
def roll(Position):
    DiceRoll = (random.randint(1,6))
    Position = DiceRoll + Position
    print(f"You rolled a: {DiceRoll}")
    print(f"Your position on the grid is: {Position}")
    return gridcheck(Position)

## gridcheck is run after roll() to check if a player has landed on a snake or a ladder
## takes one position parameter
## if player lands on a snake or ladder it returns a modified position, else it should return the parameter originally provided.
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
            print(f"You have landed on a SNAKE!!!")
            print(f"Slither on down to {value}")
            return value

    for key, value in ladders.items():
        if Position == key:
            print(f"You have landed on a LADDER!!!")
            print(f"Climb on up to {value}")
            return value

    return Position

## gamestart starts the game of snakes and ladders
## creates an inifinte loop which should break if someone wins by landing on the grid value
## takes no parameters and has 4 different stages
    ## ## Primary roll - first dice roll for a player
    ## ## Over roll - A roll that progresses past the final number on the grid, the position should be set back on the grid by the number they rolled over
    ## ## Repeat roll - Simple additional roll
    ## ## Winning roll - Player lands on the last grid position and becomes the winner
def gamestart():

    Position = 0
    Grid = 25

    while True:

        ## Primary roll
        if Position == 0:
            print("..................")
            print("Welcome to Snakes and Ladders!!")
            print("Roll the dice to begin!!")
            input("Hit any key to ROLL or CTRL-C to cancel:")
            Position = roll(Position)

        ## Over roll
        elif Position > Grid:
            backstep = Position - Grid
            print(f"You went over the grids maximum size! ({Grid}) by {backstep}")
            Position = Grid - backstep
            print(f"Your new position is: {Position}")
            Position = gridcheck(Position)

        ## Winning roll
        elif Position == Grid:
            print(f"You hit {Grid}! congratulations!")
            print("Player wins")
            break

        ## Repeat roll
        print("..................")
        input("Roll again?")
        Position = roll(Position)

gamestart()