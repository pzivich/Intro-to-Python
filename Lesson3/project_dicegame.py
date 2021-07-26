######################################################################################################################
# Project 3: Dice Game
#
# Paul Zivich (2021/7/5)
######################################################################################################################

# In this case, we will make a simple dice game to play against the computer. The goal of the game is to get the
#   highest total for the dice. The rules of the game are simple: each player will roll a set number of dice. They
#   can then choose to re-roll any dice (or keep select dice)

# To have randomness in our dice rolls, we will be using the random module. it will allow us to pick pseudo-random
#   numbers.
import random
import time

# Here we tell the user the rules of the game.
print("====================================================================================")
print("                    ~~ Paul's very cool and fun dice game ~~ ")
print(r"""
                (( _______                       (( _______                              
      _______     /\O    O\            _______     /\O    O\            _______ ))        
     /O     /\   /  \      \          /O     /\   /  \      \          /O     /\  
    /   O  /O \ / O  \O____O\ ))     /   O  /O \ / O  \O____O\ ))     /   O  /O \  
 ((/_____O/    \\    /O     /     ((/_____O/    \\    /O     /     ((/_____O/    \    
   \O    O\    / \  /   O  /        \O    O\    / \  /   O  /        \O    O\    /     
    \O    O\ O/   \/_____O/          \O    O\ O/   \/_____O/          \O    O\ O/       
     \O____O\/ ))          ))         \O____O\/ ))          ))         \O____O\/ ))    
   ((                               ((                               ((                            
""")
print("====================================================================================")
print("GOAL: the goal of the game is simple; to have the highest total.")
print("------------------------------------------------------------------------------------")
print("RULES:")
print("You and the computer will each take turns rolling five (5) dice. Any of the dice can")
print("be re-rolled on your turn. After both players decide what dice to re-roll, the dice ")
print("are rolled again. The total is then determined and the winner is declared")
print("====================================================================================\n\n")

# Now we will ask the user if they are ready to play
ready = input("Ready to play? Hit enter")


# In this step, we will define the functions we will use!
def roll_dice_init(n):
    """This function does the initial dice roll for the user and the computer.

    Parameters
    ----------
    n : int
        Number of dice to roll

    Returns
    -------
    list :
        List of the d6 dice rolls
    """
    # Empty list to store the dice rolls
    dice = []

    # for-loop to roll n 6-sided dice
    for i in range(n):
        dice_roll = random.randint(1, 6)  # random integer between 1 and 6
        dice.append(dice_roll)

    # return the dice rolls
    return dice


def determine_winner(user_dice, comp_dice):
    """Function to calculate the dice totals and determine the winner of the game. Uses the sum() function to total
    up the dice. Then checks via logic who wins

    Parameters
    ----------
    user_dice : list
        User's dice rolls
    comp_dice : list
        Computer's dice rolls

    Returns
    -------
    None
    """
    # Adding up scores
    user_total = sum(user_dice)
    comp_total = sum(comp_dice)

    # Breaking ties randomly
    if user_total == comp_total:
        print("Looks like its a tie at " + str(user_total)+"!!")
        print("Determining the winner by a final dice roll! Winner takes all")
        tied = True
        while tied:
            # Roll single die for computer
            print("Rolling computer's dice...")
            comp_tie_roll = roll_dice_init(n=1)
            time.sleep(1.2)
            print("Computer's roll:", comp_tie_roll)
            print("")
            time.sleep(0.7)

            # Roll single die for user
            print("Rolling your dice...")
            user_tie_roll = roll_dice_init(n=1)
            time.sleep(1.2)
            print("Your roll:      ", user_tie_roll)
            print("")

            time.sleep(0.7)
            if user_tie_roll > comp_tie_roll:
                print("You win!")
                tied = False
            elif user_tie_roll < comp_tie_roll:
                print("Computer wins!")
                tied = False
            else:
                print("Another tie!")
                print("Determining the winner by another dice roll! Winner takes all\n")
    # If user wins
    elif user_total > comp_total:
        print("You win!")
    # If computer wins
    elif comp_total > user_total:
        print("Computer wins!")


def reroll_dice(dice, choices):
    """Takes the dice and the choices regarding whether to re-roll and determines re-rolls as necessary

    Parameters
    ----------
    dice : list
        List of current dice rolls
    choices : string
        String indicating choices regarding re-rolls.

    Returns
    -------
    dice_updated : list
        List of re-rolled dice
    """
    print("Re-rolling requested dice...")
    time.sleep(0.4)
    dice_updated = dice.copy()
    for i in range(len(dice)):
        if choices[i] == 'r':
            dice_updated[i] = random.randint(1, 6)

    return dice_updated


def artificial_intelligence_dice_roller(comp_dice, user_dice, strategy=1):
    """AI to determine dice rolling (actually just a few different simple strategies to decide what to do)

    Returns
    -------
    rerolls : string
        Formatted string for dice re-rolls as determined by the strategy
    """
    print("Computer is calculating best course of action...")
    time.sleep(2.5)
    dice_n = len(comp_dice)

    if strategy == 1:  # This strategy re-rolls all dice (ignoring their value)
        rerolls = "r"*dice_n

    elif strategy == 2:  # This strategy re-rolls anything that is below a 4
        rerolls = ""
        for i in comp_dice:
            if i >= 4:
                rerolls += "-"
            else:
                rerolls += "r"
    else:
        raise ValueError("Computer can't find a good strategy!")

    print("Computer has decided!")
    return rerolls


def play_one_round(number_of_dice=6, rounds_of_rerolls=2):
    """Plays through one round of the dice game.
    """

    print("")

    print("Rolling computer's dice...")
    comp_roll = roll_dice_init(n=number_of_dice)
    time.sleep(0.4)
    print("Computer's roll:", comp_roll)

    print("Rolling your dice...")
    user_roll = roll_dice_init(n=number_of_dice)
    time.sleep(0.4)
    print("Your roll:      ", user_roll)

    for i in range(rounds_of_rerolls):
        # Computer is deciding re-roll
        print("")
        comp_reroll_request = artificial_intelligence_dice_roller(comp_dice=comp_roll, user_dice=user_roll, strategy=2)

        # Select dice to re-roll
        print("")
        print("Please select which dice you would like to re-roll. Use 'r' to indicate re-roll and '-' to indicate keep")
        print("".join([str(x) for x in user_roll]))
        user_reroll_request = input("")

        comp_roll = reroll_dice(dice=comp_roll, choices=comp_reroll_request)
        print("Computer's roll:", comp_roll)
        time.sleep(1)
        user_roll = reroll_dice(dice=user_roll, choices=user_reroll_request)
        print("Your roll:      ", user_roll)

    # determine_winner(user_dice=user_roll, comp_dice=comp_roll)
    determine_winner(user_dice=user_roll, comp_dice=comp_roll)


# Using the function(s) above, we can now have the game be played by the user!

play_again = True
while play_again:
    # Starting the game
    play_one_round()

    # asking if the user would like to play again
    decision = input("Play again (y/n)?\n")
    while decision.lower() not in ["y", "n"]:
        decision = input("Please select y or n:\n")
    if decision == "n":
        play_again = False


print("Thanks for playing!")
