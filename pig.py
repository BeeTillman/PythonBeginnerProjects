import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players) # Casting String to integer
        if 2 <= players <= 4:
            break
        else:
            print("There must be between 2 - 4 players.")
    else:
        print("Invalid, please try again.")

maxScore = 50
playerScores = [0 for _ in range(players)] # List comprehension (puts 0 in each part of list per player)

while max(playerScores) < maxScore:

    for playerIndex in range(players):
        print("\nPlayer", playerIndex + 1,"turn has just started!\n")
        print("Your total score is:", playerScores[playerIndex], "\n")
        currentScore = 0;

        while True:
            shouldRoll = input("Would you like to roll (y)? ")
            if shouldRoll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                currentScore = 0
                break
            else:
                currentScore += value
                print("You rolled a", value)
            
            print("Your score is:", currentScore)
        
        playerScores[playerIndex] += currentScore
        print("Your total score is:", playerScores[playerIndex])

maxScore = max(playerScores)
winningIndex = playerScores.index(maxScore)
print("Player", winningIndex + 1, "is the winner with a score of:", maxScore)