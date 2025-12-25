print("Welcome to the treasure island. \n Your mission is to find the treasure.\n")
cross_road = input("You are at a crossroad. Where your wanna go? - Type 'left' for going left and 'right' for going right.\n")
if cross_road == 'right':
    print("Game Over!")
else:
    swim = input("You reached a lake. Do you wanna swim or wait for a boat? Type 'swim' for swimming and 'wait' for boat\n")
    if swim == 'swim':
        print("Game Over!")
    else:
        door_color = input("You are in a house. There are three doors - Red, Blue and Yellow. Which one do you choose? - Type 'Red' for red, 'Blue' for blue and 'Yellow' for yellow. \n")
        if door_color == 'Red' or door_color == 'Blue':
            print("Game Over!")
        else:
            print("Congrats Nigga! You win!")
