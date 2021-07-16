####################################################################################################################
# Homework 2: Operators and Conditional Statements
#
# Name:
####################################################################################################################

# For this homework, please select one of the three mini-projects to complete. I encourage you to do all, but only one
#   is required.

# For each of the mini-projects, be sure to handle error-prone inputs with a `while` loop, like we did in the adventure
#   game. I will be checking for this when we next meet!!

##############################################
# Mini-Project 1 : Chatbot Extension

# Extend the chatbot program to ask the following questions:
#       1) What is the person's favorite food?
#       2) How is the person feeling?
#       3) Guess chatty's favorite number
# For the first question, give the chatbot a favorite food (and see if chatty and the user like the same food). For the
#   second question, have chatty give appropriate responses based on the feeling (you may need a very general `else`
#   statement so chatty doesn't say anything too weird to the user). For the 3rd, give chatty a favorite number. Then
#   have chatty ask the user to guess its favorite number (give the user a range of valid integers to be nice).

# Advice: - For the number guessing part, use a while loop to evaluate each of the user's guesses. You can adapt the
#           code from lesson 2.

# Also this would be a good time to use `time.sleep(...)` to give the chatbot realistic pauses for its responses
#   This will make the chatbot's communications seem more genuine (or more human-like and less robot).

##############################################
# Mini-Project 2 : Animal age convertor

# Write a python program that allows a user to enter the type of animal (e.g., cat, dog, bird). Then enter the
#   animal's age. Then the program should calculate the animal's age in human years! I have listed conversions below
#   for cats and dogs, but you should look up and add other animals. Be sure to provide the available animals to the
#   user.

# Advice: - For dogs, the 1st year is equivalent to 12 years, the 2nd is 24 years, and every additional year after that
#           corresponds to 4 human years
#         - For cats, the 1st year is equivalent to 15 human years, the 2nd is 24, and every additional year after that
#           corresponds to 4 human years
#         - I suggest the following order for inputs: animal, age of animal, calculate age, print in human years
#         - Don't forget to use a while loop to handle invalid 'animal types'. If you want to be more robust, allow the
#           user to try to input an animal 3 times. If they are wrong 3 times, close the program (your while loop will
#           need to use a counter and evaluate a conditional operator statement.

##############################################
# Mini-Project 3 : Game Extension

# Extend the game we built before. We only programmed a purpose for a few of the items and there are paths not
#   finished. Alternatively, you can build a completely new game! I encourage you to be creative (and add what you
#   think is most fun). Here are some suggestions on what you could add:
#       1) Add more text and story elements
#       2) Add to the 4 paths that we ended the lesson on (i.e., north, south, east, west)
#       3) Have someone ask a riddle to the player. If they get it right, they can continue

# Advice: - It may be helpful to write out a flowchart to see how to structure the if-then statements
#         - when adding an option, be sure to check all possible paths for that option (to make sure there are
#           no errors!)
#         - While normally you would allow a user to go backwards (between places), this will be harder to program
#           using only what we know so far. So I recommend that once a user makes a decision, they are 'stuck' on that
#           path. Example: if they user goes 'West', then they can only proceed down the 'West' choice path (i.e., they
#           can't go backwards and then choose 'North' without replaying the game).
