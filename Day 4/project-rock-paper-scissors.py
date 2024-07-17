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

#Write your code below this line 👇
choice = [rock, paper, scissors]

random_integer = random.randint(0, 2)

computer_choice = choice[random_integer]

player_choice_number = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors\n"))

if player_choice_number < 0 or player_choice_number >= len(choice):
  print("Invalid Choice! you")

else:

  player_choice = choice[player_choice_number]

  print(choice[player_choice_number])

  print("Computer chose:")

  print(computer_choice)

  if player_choice == computer_choice:
    print("It's a draw!")
  elif player_choice == rock and computer_choice == scissors:
    print("You Win!")
  elif player_choice == paper and computer_choice == rock:
    print("You win!")
  elif player_choice == scissors and computer_choice == paper:
    print("You win!")
  else:
    print("You lose!")
