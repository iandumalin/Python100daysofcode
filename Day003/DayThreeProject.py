side = input("Welcome to Treasure Island\nYour mission is to find the treasure\nwYou're at a cross road, where do you want to go? Left or right?\n").lower()
if side == "right" or side == "r" :
    print("Game Over...")
elif side == "left" or side == "l" :
    swim_or_wait = input("Do you want to swim or will you wait?\n").lower()
    if swim_or_wait == "swim" or swim_or_wait == "s" :
        print("Game Over...")
    elif swim_or_wait == "wait" or swim_or_wait == "w" :
        door = input("Do you choose the yellow, red or blue door?\n").lower()
        if door == "red" or door == "r" :
            print("Game Over...")
        elif door == "blue" or door == "b" :
            print("Game Over...")
        elif door == "yellow" or door == "y" :
            print("You win!")