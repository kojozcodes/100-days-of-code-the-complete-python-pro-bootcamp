import random
from art import logo

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

number_to_guess = random.randint(1, 100)
print(number_to_guess)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()

if difficulty == 'easy':
    lives = 10
else:
    lives = 5