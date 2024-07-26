import random
from art import logo

def check_wrong_guess(guess, number):
    if guess > number:
        return "Too High."
    else:
        return "Too Low."
        
print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

number_to_guess = random.randint(1, 100)
print(number_to_guess)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()

if difficulty == 'easy':
    lives = 10
else:
    lives = 5

is_game_over = False

while lives > 0 and not is_game_over:
    print(f"You have {lives} attempts to guess the number.")
    guess = input("Make a guess:    ")
    if guess == "":
        guess = 0
    else:
        guess = int(guess)

    if guess == number_to_guess:
        print(f"You got it! The answer was {number_to_guess}")
        is_game_over = True
    else:
        print(check_wrong_guess(guess, number_to_guess))
        lives -= 1

if lives == 0:
    print("You've run out of guesses, you lose.")