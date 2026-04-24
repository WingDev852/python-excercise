import random

player_choice = int(input("What do you choosie? Type 0 for rock, 1 for paper and 2 for scissors "))

computer_choice = random.randint(0,2)

print(f"computer choose {computer_choice}")

if player_choice < 0 or player_choice > 2:
    print("Invalid choice! You lose.")
elif player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == 0 and computer_choice == 2) or \
     (player_choice == 1 and computer_choice == 0) or \
     (player_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
