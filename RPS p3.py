import random

# ASCII art structures stored in a list
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
         _______)
        _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

while True:
    try:
        user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

        if user_choice not in [0, 1, 2]:
            print("Invalid input! Please enter 0, 1, or 2.\n")
            continue

        computer_choice = random.randint(0, 2)

        print("\nYou chose:")
        print(choices[user_choice])

        print("Computer chose:")
        print(choices[computer_choice])

        # Game logic
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose!")

        # Ask to play again
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

    except ValueError:
        print("Invalid input! Please enter a number.\n")