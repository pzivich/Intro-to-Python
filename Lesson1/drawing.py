######################################################################################################################
# Lesson 3: Some Basic Drawing / Art
#
# Paul Zivich (2021/6/8)
######################################################################################################################

import turtle

sh = turtle.Turtle()

# Drawing a basic square
sh.forward(100)
sh.right(90)
sh.forward(100)
sh.right(90)
sh.forward(100)
sh.right(90)
sh.forward(100)
sh.right(90)

# Thats a lot of steps. Lets do a loop instead.
sh.reset()  # Resets the turtle
for i in range(4):
    sh.forward(100)
    sh.right(90)

sh.color("red")
for i in range(4):
    sh.forward(100)
    sh.right(90)

sh.reset()

turtle.bgcolor("black")
turtle.speed("fastest")

sh.color("white")
for i in range(20):
    sh.forward(5*i)
    sh.right(90)

sh.reset()

sh.hideturtle()
sh.color("white")

for i in range(36):
    sh.circle(100)
    sh.right(10)

color_list = ["red", "yellow", "blue", "orange", "green", "red"]
for n in range(36):
    #sh.begin_fill()
    for i in range(6):
        sh.color(color_list[i])
        sh.forward(100)
        sh.left(60)
    #sh.end_fill()
    sh.right(10)

turtle.done()
