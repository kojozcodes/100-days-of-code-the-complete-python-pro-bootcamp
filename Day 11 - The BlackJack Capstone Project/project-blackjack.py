import random
from art import logo

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
    
    if player_score > 21 and computer_score > 21:
        return "You lose, Your score is over 21"

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

    print(logo)

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

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if another_card == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
