######################################################################################################################
# Lesson 3: Functions, Random, Loops with a List
#
# Paul Zivich (2021/7/5)
######################################################################################################################

# In the previous lessons, we sometimes had to write lengthy bits of code. Even worse, we had to use the same (or
#   similar chunks of code) multiple times. We wrote them over and over. However, that is tiresome, allows for coding
#   errors, and is unnecessary. Instead, we will learn how to use functions!

# To start, let's learn how to calculate the mean of a list using python.
#   We can do so using two built-in utilities; sum() and len()

# sum() calculate the sum of a list
x = [1, 9, 10]
print(sum(x))

# len() counts the number of items in an object (in this case a list)
print(len(x))

# so we can calculate the mean by using the following
mean = sum(x) / len(x)
print(mean)

# Now, we could memorize that chunk of code and re-write it any time we want to calculate the mean.
#   But that's more work than I want to do. Instead, we can use functions!

# Functions are a generalized chunk of code that we can use over and over. In this case, our function will take a
#   list of objects and calculate the mean of that list for us


def mean_of_list(input_list):
    """Documentation for the function can be put here. If you call the help() function, then this comment will be
    output. So please be sure to detail the function here

    This function calculate the mean of a list of integers or floats. It does this by using the sum() and len()
    built-in functions

    Parameters
    ----------
    input_list : list
        List of numbers to calculate the mean for

    Returns
    -------
    mean : float
    """
    # Add together all items in the list
    summand = sum(input_list)
    # Calculate the number of items in the list
    n = len(input_list)
    # Calculate the mean
    mean = summand / n
    return mean  # return is a special function that ends the function and returns the specified object


m1 = mean_of_list(x)
print(m1)

m2 = mean_of_list(input_list=[1, 1, 1, 1, 2])
print(m2)

# Functions are especially useful for blocks of code that we will use a lot or particularly long chunks of code.
#   The mean is simple to calculate, but the functions makes it easy for us to do (without having to remember the
#   formula or other details).

import turtle
shelly = turtle.Turtle()

# Let's return to our turtle friend. We will write a function that generates a shape with a given number of sides.
#   This function will use some specific features:
#       1) error checking (our shape will need at least 3 sides)
#       2) optional argument(s)


def draw_regular_polygon(sides, distance=50, left=True):
    """Tells turtle to draw a specific shape based on the number of sides
    """
    # Step 1 Error Checking
    if not isinstance(sides, int):
        raise ValueError("`sides` must be an integer")
    if sides < 3:
        raise ValueError("`sides` must be at least 3")

    # Step 2 Draw the Shape
    angle = 360 / sides
    for i in range(sides):
        shelly.forward(distance)
        if left:
            shelly.left(angle)
        else:
            shelly.right(angle)


# Example of our new shape
draw_regular_polygon(sides=3)
draw_regular_polygon(sides=4)
draw_regular_polygon(sides=5)
draw_regular_polygon(sides=7, distance=75)
draw_regular_polygon(sides=7, distance=75, left=False)


# for i in range(3, 20):
#     draw_regular_polygon(sides=i)

turtle.done()  # Tells turtle we are done creating graphics (be nice to the turtle!)
