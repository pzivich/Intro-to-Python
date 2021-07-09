######################################################################################################################
# Project 2: Adventure Game
#
# Paul Zivich (2021/7/9)
######################################################################################################################

import time

game_name = "Paul's very fun and very good and very creative game"


# Introduction to Adventure Game
print("==================================================================================================")
print("WELCOME TO " + game_name)
print("==================================================================================================")
time.sleep(2)
print("You are in Chapel Hill, North Carolina about to embark on a long hike.")

# Item Selection
print("To prepare for the journey, you decide to take one item with you.")
print("Which item do you take:")
time.sleep(1)
print("map(m), flashlight(f), chocolate(c), rope(r)")
item = input("What do you choose?\n")
while not (item == "m" or item == "f" or item == "c" or item == "r"):
    print("Unfortunately that is not an option...")
    item = input("What do you choose?\n")

# First decision
print("You leave your house and depart along the trail.")
time.sleep(2)
print("Suddenly you hear a noise!")
choice_1 = input("Do you follow the noise? Enter y or n\n")
while not (choice_1 == "y" or choice_1 == "n"):
    print("Unfortunately that is not an option...")
    choice_1 = input("Do you follow the noise? Enter y or n\n")

if choice_1 == "y":
    print("You move closer to where the sound is coming from...")
    time.sleep(2)
    print("As you approach, the sound suddenly stops.")
    time.sleep(2)
    print("You look around and don't recognize the surroundings.")
    print("It looks like you are lost!!")

else:
    print("You wisely decide to stick to the trail you know.")
    time.sleep(2)
    print("But the sound persists around you.")
    time.sleep(2)
    print("It sounds like it is getting closer...")
    time.sleep(4)
    print("You panic and start running to the entrance!")
    action = input("Do you start running(r) or use your phone to call for help(c)?\n")
    while action.lower() != "r":
        print("There is no signal!")
        print("The sound is getting closer! Better start to run")
        action = input("Do you start running(r) or use your phone to call for help(c)?\n")

    print("You start to run. The sound gets really loud.")
    time.sleep(2)
    print("But as you keep running, the sound suddenly stops.")
    time.sleep(2)
    print("You look around and don't recognize the surroundings.")
    print("It looks like you are lost!!")


# Second decision
print("It looks like you can head north, east, south, or west")
direction = input("Which direction do you go?")
while direction.lower() not in ["north", "south", "east", "west"]:
    print("Unfortunately you are stuck going either north, south, east, or west")
    direction = input("Which direction do you go?")

