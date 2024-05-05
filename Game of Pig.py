import random

# a dictionary of dice - a data structure to make the game pretty
# - in Thonny increase font size under view to see them properly
dice = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}


# Function to roll a die and return the result
def roll_die():
    return random.randint(1, 6)


# Game Variables
humanBank = 0
humanScore = 0
computerBank = 0
computerScore = 0

# Welcome Screen - human instructions
print("""\
   ___                       __   ___ _      
  / __|__ _ _ __  ___   ___ / _| | _ (_)__ _ 
 | (_ / _` | '  \/ -_) / _ \  _| |  _/ / _` |
  \___\__,_|_|_|_\___| \___/_|   |_| |_\__, |
                                       |___/ """)
print("Welcome to the Game of Pig!")
print("Instructions:")
print("1. You and the computer take turns rolling a six-sided die.")
print("2. Each number rolled adds to your current turn score, except for 1.")
print(
    "3. If you roll a 1, your turn ends and you lose all points for that turn."
)
print(
    "4. You can choose to 'hold' at any time, adding your turn score to your banked score."
)
print("5. First player to reach 100 banked points wins.")
print()

# GAME LOOP
while True:
    # HUMAN PLAYER GOES FIRST
    humanScore = 0
    while True:
        answer = input("(r)oll or (h)old? ")
        if answer.lower() == 'r':
            die = roll_die()
            print("You rolled:", dice[die])
            if die == 1:
                print("You rolled a 1. Turn score lost.")
                humanScore = 0
                break
            else:
                humanScore += die
                print("Current Turn Score:", humanScore)
        elif answer.lower() == 'h':
            humanBank += humanScore
            print("Turn score added to banked score. Current Banked Score:",
                  humanBank)
            break
        else:
            print("Invalid input. Please enter 'r' to roll or 'h' to hold.")

    # Check if Human Player won
    if humanBank >= 100:
        print("You win! Congratulations!")
        break

    # COMPUTER PLAYER TURN
    computerScore = 0
    while computerScore < 20:  # Computer rolls until it accumulates at least 20 points
        die = roll_die()
        print("Computer rolled:", dice[die])
        if die == 1:
            print("Computer rolled a 1. Turn score lost.")
            computerScore = 0
            break
        else:
            computerScore += die
            print("Current Computer Score:", computerScore)

    computerBank += computerScore
    print("Computer decides to hold. Current Computer Banked Score:",
          computerBank)

    # Check if Computer Player won
    if computerBank >= 100:
        print("Computer wins! Better luck next time!")
        break

    # Display Current Scores
    print("Current Scores:")
    print("Your Banked Score:", humanBank)
    print("Computer's Banked Score:", computerBank)
    print()

    # Ask to Play Again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break

# End Game
print("""\
         ___                   ___              
        / __|__ _ _ __  ___   / _ \__ _____ _ _ 
       | (_ / _` | '  \/ -_) | (_) \ V / -_) '_|
        \___\__,_|_|_|_\___|  \___/ \_/\___|_|  """)
print("Thank you for playing!")
