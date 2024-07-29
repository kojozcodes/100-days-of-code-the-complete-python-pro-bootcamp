import random
from game_data import data
from art import logo, vs

count = 0
#Assign Celeb to variables function
def assign():
    return random.choice(data)

data_a = assign()
data_b = assign()

game_over = False

while not game_over:
    while data_b == data_a:
        data_b = assign()

    print(logo)

    if count > 0:
        print(f"You're right! Current score: {count}.")
    #Show first celeb details
    print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}")

    #Vs Logo
    print(vs)

    #Show second celeb details
    print(f"Compare B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}")

    #If correct, increment current score, assign the second celeb details as the first now then loop
    # print(data_a)
    # print(data_b)

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if (choice == 'A' and data_a['follower_count'] > data_b['follower_count']) or (choice == 'B' and data_b['follower_count'] > data_a['follower_count']):
        count += 1
        # Update data_a to be the winner and get a new data_b
        data_a = data_b
        data_b = assign()
    else:
        print(f"Sorry, that's wrong. Final score: {count}")
        game_over = True

    # print(data_a)
    # print(data_b)