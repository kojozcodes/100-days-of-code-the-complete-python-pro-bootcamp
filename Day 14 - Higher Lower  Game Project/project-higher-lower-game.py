import random
from game_data import data
from art import logo, vs
print(logo)

#Assign Celeb to variables function
data_a = random.choice(data)
data_b = random.choice(data)

while data_b == data_a:
    data_b = random.choice(data)

#Show first celeb details
print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}")

#Vs Logo
print(vs)

#Show second celeb details
print(f"Compare B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}")

#If correct, increment current score, assign the second celeb details as the first now then loop
print(data_a)
print(data_b)

choice = input("Who has more followers? Type 'A' or 'B': ").upper()
count = 0
if choice == 'A':
    if data_a['follower_count'] > data_b['follower_count']:
        count += 1
        print(f"You're  right! Current score: {count}.")
        data_a = data_b
        data_b = random.choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {count}")
else:
    if data_b['follower_count'] > data_a['follower_count']:
        count += 1
        print(f"You're  right! Current score: {count}.")
        data_a = data_b
        data_b = random.choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {count}")

print(data_a)
print(data_b)

#If not, print you're wrong - End program