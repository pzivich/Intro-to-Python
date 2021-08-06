import random, sys, time

width = 70
pause_len = 0.05

lwidth = 20
gwidth = 10

while True:
    rwidth = width - gwidth - lwidth
    # printing current descent level
    print(("#"*lwidth) + (" "*gwidth) + ("#"*rwidth))

    # Check to see if exit
    try:
        time.sleep(pause_len)
    except KeyboardInterrupt:
        sys.exit()

    # adjusting left side
    roll = random.randint(1, 6)
    if roll == 1 and lwidth > 1:
        lwidth = lwidth - 1
    elif roll == 2 and lwidth + gwidth < width - 1:
        lwidth = lwidth + 1
    else:
        pass

    # Adjusting gap width dynamically
    roll = random.randint(1, 6)
    if roll == 1 and gwidth > 1:
        gwidth = gwidth - 1
    elif roll == 2 and lwidth + gwidth < width - 1:
        gwidth = gwidth + 1
    else:
        pass
