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
game = [rock, paper, scissors]

print("Rock, Paper, Scissors.. Go!\n")

player_choice = int(input("type 0: Rock, 1: Paper, 2: Scissors\n"))
random_role = random.randint(0, 2)
computer_choice = game[random_role]

if player_choice >= 0 and player_choice <= 2:
    print("YOU:" + game[player_choice])
    print("COMPUTER:" + computer_choice)


if player_choice < 0 or player_choice > 2:
    print("This is an invalid choice. Please choose between 0 - 2.")
elif player_choice == 0 and random_role == 1:
    print("You LOSE!")
elif player_choice == 1 and random_role == 2:
    print("You LOSE!")
elif player_choice == 2 and random_role == 0:
    print("You LOSE!")
elif player_choice == random_role:
    print("DRAW!")
else:
    print("You WIN!")