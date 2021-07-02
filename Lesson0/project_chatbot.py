######################################################################################################################
# Lesson 2: Basics Continued
#
# Paul Zivich (2021/6/8)
######################################################################################################################

# To build off next week, we will we going through a guided project. In this project, we will build a chat bot.
#   Key ideas: special functions (print, input); create and update variables; convert between data types

# Project description: we are going to build a simple chatbot. The object is to write a computer program that appears
#   to talk with the user. In this case, our chatbot will be simple and go through a specific script we give it.
#   Later lessons can be used to extend the chatbot to be more interactive with the user

######################
# Flow diagram

# Before starting to code, let's lay out a flow diagram. In this case it is pretty simple. Our chatbot will do the
#   following actions:
#   Introduction (say hello, ask for name) -> Respond and give bot's name -> ask year of birth -> tell them what year
#       they will turn 100 years old -> ask favorite food -> ask how often they eat favorite food -> Goodbye
# It is always helpful to break writing code into these individual pieces. Seeing each of the pieces and how they fit
#   together is helpful and prevent you from feeling overwhelmed with a complex project.

# Now let's get to work on each of the pieces

######################
# Chatty Info

# Let's give our chatbot a name and the year it was born
chatbot_name = "Chatty9k"
chatbot_dob = 2021

######################
# Introduction
print("Hello!")  # Chatbot starts by saying hello
user_name = input("What is your name?\n")  # then it asks the user for their name
# the \n is a special character telling python to start a new line after the text is displayed
print("Nice to meet you, "+user_name+". My name is " + chatbot_name + ".")  # Say hello to user and then give name

######################
# Year of Birth
year_of_birth = input("What year were you born?\n")  # ask when user was born
when_100 = str(100 + int(year_of_birth))  # calculate what year they will turn 100. Be sure to convert to string!
print("You will be 100 years old in " + when_100 + ". That's amazing!")  # tell user the calculation
print("I was born in " + str(chatbot_dob) + ".")  # tell user when the chatbot was born

######################
# Favorite Food
favorite_food = input("What is your favorite food?\n")  # ask the user for their favorite food
print("I like " + favorite_food + " too!")  # Tell them they like that food too
how_often_food = input("How often do you eat " + favorite_food + "?\n")  # ask how often they eat it
print("Interesting. I wonder if eating " + favorite_food + " " + how_often_food + " is healthy?")
# take both of users previous responses into a sentence

######################
# Bonus

######################
# Goodbye
print("Phew! I am getting tired")  # tell user the bot is tired and close the chat
print("I am too tired to keep talking, but we can chat again.")
print("I liked talking to you!")
print("Goodbye, " + user_name + "!")
