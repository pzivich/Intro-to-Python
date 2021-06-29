######################################################################################################################
# Lesson 1: Setup and Introduction
#
# Paul Zivich (2021/6/8)
######################################################################################################################

# All characters after the '#' mark are comments. As such the computer ignores these lines
# Try writing a comment on a new line by putting a comment below this line

# our first line
print("Hello world!")
# print() is a special function that takes the input and displays it in the console. For example, running this code
#   will display `Hello world!` to the console

##############
# Math

# Let's do some math! First we will add two numbers together and have the computer tell us what they are
print(2 + 2)  # what answer will this give?
# Now some substraction
print(3 - 1)  # what answer will this give?
# Now some multiplication
print(4 * 11)  # what answer will this give?
# Now some division
print(20 / 5)  # what answer will this give?

# whoa, the division gave us something else besides 4. It gives us 4.0 (which is functionally the same)
# this leads to the next section of data types

##############
# Data Types

# python has a bunch of different data types. Previous we have seen strings, integers, and floats, but let's go back
# you can also check the type of something by calling print(type(...))

# Strings: strings are indicated by " or ' wrapped around words. Below are some examples
print("This is a string variable")
print("we " + "can " + "add " + "strings" + "together")
print("we " + "can " + "also " + "multiply."*4)
# print("My favorite number is " + 10)  # this line won't work because you can't add strings and integers
print("My favorite number is " + str(10))  # this uses the special function to convert to a string

# Integers: integers are exactly what their name is. Below are some examples
print(10)
print(5)
# we can also use a special function to convert to integers, int()
print(int(5.9))  # note: this does NOT round. Instead it returns the integer value
print(int("12"))  # converting: string -> integer

# Floats: floats or floating-point are numbers that are not integers. Below are some examples
print(1.)  # Adding a decimal place tells python that the number is a float
print(1.5)
print(float(100))  # converting: integer -> float
print(float("100"))  # converting: string -> float
print(int(float("100")))  # converting: string -> float -> integer

# So why did python return 4.0 before?
# Well for division problems, it converts the number to a float

# There are many other data types, but we will learn those as we continue through the lessons

##############
# Variables

# Consider the following word problem: what is five times seven minus three, all divided by 1.3?

# while we can do complex calculations in one line, we can also break it into pieces. Each of the pieces can be set
#   as a variable. Variables are useful for operations where we want to use some value. Let's demonstrate variables
#   with the preceding math question

part_one = 5 * 7
part_two = 3
part_three = 1.3
print((part_one - part_two) / part_three)  # remember to add parentheses so python knows the operation order we want!


##############
# More Math

# Here is a cheat sheet of some common math operations for generic `x` and `y`

# Addition:         x + y
# Subtraction:      x - y
# Multiplication:   x * y
# Division:         x / y
# Floor Division:   x // y  # only returns the non-decimal part
# Remainder:   x % y  # only returns the remainder from the division
# Exponent:         x ** 2  # x-squared

# to round numbers, you can use round(x, 2). That will round the variable x to 2 decimal places

# END: this concludes lesson 1
