############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random

def deal_card():
    """It returns a random card from the list/deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
    return random.choice(cards)

def calculate_score(card_list):
    """It takes a list of cards, calculates and returns the score"""
    if len(card_list) == 2 and sum(card_list) == 21:
        return 0

    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)

def compare(player_score, computer_score):
    """It takes both the player and computer's list of card and compares them to find out the winner"""
    if player_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "You lose, Computer has Blackjack"
    elif player_score == 0:
        return "You win, You have a Blackjack"
    elif player_score > 21:
        return "You lose, Your score is over 21"
    elif computer_score > 21:
        return "You win, Computer score is over 21"
    elif player_score > computer_score:
        return "You win, Your score is closer to 21 than computer's score"
    else:
        return "You lose, Computer's score is closer to 21 than your score"

def play_game():
    player_cards = []
    computer_cards = []
    is_game_over = False

    for times in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over: 

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current_score: {player_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if player_score > 21 or player_score == 0 or computer_score == 0:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass")

            if another_card == "y":
                player_cards.append(deal_card())
                calculate_score(player_cards)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        calculate_score(computer_cards)


print(f"Your final hand: {player_cards}, final score: {player_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
compare(player_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
