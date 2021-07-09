######################################################################################################################
# Lesson 1: Some Basic Drawing / Art
#
# Paul Zivich (2021/7/9)
######################################################################################################################

# This week we will learn how to do some basic drawing using the python module: turtle. We will use the module to
#   create some pictures. The pictures will draw when we run the code.

# Learning objectives:
#       0: python modules
#       1: for-loops
#       2: lists (a new object type!)

# Modules: modules are sets of functions that we can load and use.
#   This is easier to use more complex functions that aren't immediately available
#   in python. When we installed python, it came with a basic set of modules. We
#   will be using more of these modules as we continue to go through. First, we will
#   use the `turtle` module to make some pictures
# Turtle is one of the basic modules that comes with python. It features a simple
#   animated / drawing library.

import turtle  # loads the turtle module so we can use it (put this at the top of the script)

# to access the turtle module, we need to specify turtle in the code
# then we can use functions within the turtle module
shelly = turtle.Turtle()  # this statement opens the turtle module and the Turtle function

# Drawing a basic square
shelly.forward(100)  # tells the turtle to go forward 100 steps
shelly.right(90)  # tells the turtle to turn 90 degrees to the right
shelly.forward(100)  # tells the turtle to go forward 100 steps
shelly.right(90)
shelly.forward(100)
shelly.right(90)
shelly.forward(100)
shelly.right(90)

shelly.reset()  # Resets the turtle

# That is an annoying way to draw a square though. We have a series of repeated directions. Therefore, if we could
#   repeat the same directions multiple times, our code could be simpler. We will do so by using for-loops

#####################
# for loops

# When we want to do a procedure a bunch of times we can use a `for loop`.  Below is a basic for loop. What does this
#   output? Also what is the `range` function?
for i in range(4):
    print(i)

# Here is a better way to draw a square using a for-loop
for i in range(4):
    shelly.forward(100)
    shelly.right(90)

# Let's change shelly's color for our next set of drawings
shelly.color("red")

# Let's say we wanted to draw multiple squares now. We can also do that using nested for-loops
# there are now 2 loops, the outer loop and the inner loop!
for j in range(4):
    shelly.penup()  # lifts up the pen (so no line is draw)
    shelly.forward(110)
    shelly.right(90)
    shelly.pendown()  # sets the pen back down to draw
    for i in range(4):  # drawing a square
        shelly.forward(50)
        shelly.right(90)

shelly.reset()  # Resets the turtle

# Some additional options
turtle.bgcolor("black")  # set the background color
turtle.speed("fastest")  # sets the turtle speed (this is the fastest)

# Drawing a simple labyrinth! We can do extra things with the loop indicator
shelly.color("white")
for i in range(1, 21):
    shelly.forward(5*i)
    shelly.right(90)

shelly.reset()  # Resets the turtle

# some other options!
shelly.hideturtle()  # Hide the turtle indicator
shelly.color("white")  # set the turtle color
shelly.circle(100)  # Draw a circle with diameter of 100

#####################
# lists

#   Lists are a new object type. They hold collections of other objects in a particular
#   order. The following is an example of a list of 6 different string objects.
#   Lists are useful for storing multiple objects then querying those objects. Also
#   lists allow for a bunch of different object types (you can have a list of strings,
#   integers, and floats with no issues. You can even have a list of lists of lists of ...
color_list = ["red", "yellow", "blue", "orange", "green", "red"]

# you can also make lists of lists of lists. Lists are a very useful object and we will
#   use them lots in future projects

# We can access the objects in the list via the following
print(color_list[0])  # first item in the list
print(color_list[3])  # 4th item in the list
print(color_list[-2])  # second last item in the list

# You can also multiply lists! Give it a try and see what happens

#####################
# loops with lists

# Sometimes we want to do a bunch of processes again and again. Here we use a loop of loops
#   to draw a series of hexagons!
for n in range(36):
    # shelly.begin_fill()
    for i in range(6):
        shelly.color(color_list[i])
        shelly.forward(100)
        shelly.left(60)
    # shelly.end_fill()
    shelly.right(10)

turtle.done()  # Tells turtle we are done creating graphics (be nice to the turtle!)
# will also keep the turtle open until we click the 'X'


