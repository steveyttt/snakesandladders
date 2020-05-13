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

    players = {}
    Grid = 25
    Game = "running"

    print("Welcome to Snakes and Ladders!!")
    input("Hit any key to PLAY or CTRL-C to cancel:")
    NumPlayers = int(input("Please enter the number of players:"))
    
    for i in range(NumPlayers):
        player = "player" + str(i)
        username = str(input(f"Please enter {player}'s username:"))
        players[player] = {"name" : username, "score" : 0}

    while Game == "running":

        for player, value in list(players.items()):

            ## Primary roll
            if value["score"] == 0:
                print("..................")
                print("Welcome", value["name"])
                input("Hit enter to roll the dice!!")
                value["score"] = roll(0)

            # Repeat roll
            else:
                print("..................")
                print("Welcome", value["name"], "you are at position", value["score"] )
                input("Roll again?")
                value["score"] = roll(value["score"])

                ## Winning roll
                if value["score"] == Grid:
                    print(f"You hit {Grid}! congratulations!")
                    print("Player", value["name"], "wins")
                    Game = "finished"
                    break

                ## Over roll
                if value["score"] > Grid:
                    backstep = value["score"] - Grid
                    print(f"You went over the grids maximum size! ({Grid}) by {backstep}")
                    value["score"] = Grid - backstep
                    print("Your new position is:", value["score"])
                    value["score"] = gridcheck(value["score"])

gamestart()
