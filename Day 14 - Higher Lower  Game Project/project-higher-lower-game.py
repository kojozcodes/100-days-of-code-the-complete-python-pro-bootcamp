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

#If not, print you're wrong - End program