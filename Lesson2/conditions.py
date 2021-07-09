######################################################################################################################
# Lesson 2: Operators and Conditional Statements
#       Learning objectives: Boolean data types, operators, conditional statements, conditional loops
#
# Paul Zivich (2021/7/9)
######################################################################################################################

############################
# New Data Type: Boolean
print(True, False)  # These objects are booleans
# bool()  # convert an item into a boolean object

# Assess Equality: returns a boolean object
print(1 == 0)
print("Yes" == "yes")
print(1 != 1)

# Compare values: also returns a boolean object
print(5 > 2)
print(10 >= 10)
print(1 >= 10)
print("X" < "a")

###########################
# Operators: AND, OR, NOT
print(True and False)
print(True or False)
print(not True)
print(not False)

###########################
# Conditions: IF, ELIF, ELSE

# we can take full advantage of boolean objects with conditional statements.
#   Conditional statements allow for certain actions to be taken based on whether a statement is true

# If statements
raining = True
if raining:  # remember that must end with colon
    print("It is wet outside")  # all the conditional statements must be indented!
    print("Bring umbrella")
if not raining:
    print("It may be dry outside")

# If-else statements
#   if-else statements allow for the either/or options in regards to code
day = "Monday"
if day.lower() == "saturday" or day.lower() == "saturday":
    print("SNOOZE")
else:
    print("TIME TO WAKE UP")

# If-ElseIf-Else statements
#   we can also link multiple phrases together in a series of conditions
if day.lower() == "saturday" or day.lower() == "saturday":
    print("SNOOZE")
elif day.lower() == "friday":
    print("Party and Party and Party and Yeah")
else:
    print("TIME TO WAKE UP")

# Nested conditionals
#   Similar to for-loops, you can also nest conditional statements via indents
secret_number = 12
n = input("What number am I thinking of:\n")
n = int(n)  # converting to integer! (why is this necessary?)
if n == secret_number:
    print("Correct! "+str(secret_number)+" was the secret number")
    print(":)")
else:
    if n > secret_number:
        print("Too high!")
    elif n < secret_number:
        print("Too low!")
    else:
        print("Was that a number... :/")

###########################
# Conditional Loops!

# another loop type is a `while` loop. A while-loop continues until the condition becomes false. Below is
#   a simple example of a while-loop
x = 0
while x < 10:  # `while` continues as long as the condition is True!
    print("Adding one to x...")
    x = x + 1
    print("X="+str(x))

# NOTE: infinite loops (where the while condition is always true) is possible
#       in general it is better to use a for loop whenever possible to avoid this problem

# So let's make a better number guessing game!
secret_number = 83
n = input("What number am I thinking of:\n")
n = int(n)
while not (n == secret_number):
    if n > secret_number:
        print("Too high!")
    else:
        print("Too low!")
    n = input("Guess again:\n")
    n = int(n)

print("Correct! The number was " + str(n))
