import random
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


images = [rock, paper, scissors]

try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
    if user_choice < 0 or user_choice >= 3:
        print("Invalid Input")
    else:
        print("Your Choice:")
        print(images[user_choice])

        com_choice = random.randint(0, 2)
        print("Computer Chose:")
        print(images[com_choice])

        if user_choice == 0 and com_choice == 2:
            print("You Win!")
        elif com_choice == 0 and user_choice == 2:
            print("You Lose!")
        elif user_choice > com_choice:
            print("You Win!")
        elif com_choice > user_choice:
            print("You Lose!")
        elif user_choice == com_choice:
            print("Draw!")

except ValueError:
    print("Invalid Input. Please enter a valid number.")
