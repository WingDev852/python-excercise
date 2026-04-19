print("Welcome to the Treasure Island. Your mission is to find the treasure.")

player_choice = input("Choose Left or Right: ").lower()

if player_choice == "left":
    second_choice = input("You are now standing on a island do you want to wait or swim? ").lower()
    if second_choice == "wait":
        third_choice = input("A door is appearing choose the right door color: Red, Blue or Yellow ").lower()
        if third_choice == "red":
            print("You got burned by fire. Game Over.")
        elif third_choice == "blue":
            print("You got eaten by beasts. Game Over.")
        elif third_choice == "yellow":
            print("You won the game congratulations !!")
        else:
            print("You lose the game. Game Over")

    else:
        print("You got attacked by trouleftts. Game Over.")
else:
    print("You fell in to a hole. Game Over.")
