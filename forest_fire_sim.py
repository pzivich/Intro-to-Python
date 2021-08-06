import random, sys, time
import bext

width = 120
height = 50

tree = "A"
fire = "w"
empty = " "

init_tree_density = 0.20
grow_chance = 0.01
fire_chance = 0.01

pause_length = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)

        nextForest = {"width": forest['width'],
                      "height": forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue
                if ((forest[x, y] == empty) and random.random() <= grow_chance):
                    nextForest[(x, y)] = tree
                elif ((forest[x, y] == tree) and random.random() <= fire_chance):
                    nextForest[(x, y)] = fire
                elif forest[x, y] == fire:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if forest.get((x+ix, y+iy)) == tree:
                                nextForest[(x+ix, y+iy)] = fire
                    nextForest[(x, y)] = empty
                else:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest
        time.sleep(pause_length)


def createNewForest():
    forest = {'width': width, "height": height}
    for x in range(width):
        for y in range(height):
            if (random.random() * 100) <= init_tree_density:
                forest[(x, y)] = tree
            else:
                forest[(x, y)] = empty
    return forest


def displayForest(forest):
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == tree:
                bext.fg("green")
                print(tree, end="")
            elif forest[(x, y)] == fire:
                bext.fg("red")
                print(fire, end="")
            elif forest[(x, y)] == empty:
                print(empty, end="")
        print()
    bext.fg("reset")
    print("Grow chance: {}%".format(grow_chance*100), end="")
    print("Fire chance: {}%".format(fire_chance*100), end="")
    print("Press Ctrl-C to quit.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

