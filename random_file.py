import random

random_number = random.randint(1, 10)  # Generate a random number between 1 and 10
total_chances = 5

for attempts in range(total_chances):
    user_input = int(input(f"Enter a number between 1 and 10 ({total_chances - attempts} chances left): "))

    if user_input == random_number:
        print("You guessed it right!")
        break  # Exit the loop if the user guesses correctly

    if attempts < total_chances - 1:
        print("Bad luck! Try again.")
    else:
        print(f"Out of chances! The correct number was {random_number}")
