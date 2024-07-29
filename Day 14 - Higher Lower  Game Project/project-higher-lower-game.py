import random
from game_data import data
from art import logo, vs
print(logo)

#Assign Celeb to variables function
#Takes celeb at random
def assign_celeb():
    return random.choice(data)

#compare two celebs function
def compare(a, b):
    choice = input('A' or 'B')
    if choice == A:
        if A > B:
            print("A")
        else:
            print("B")
    elif choice == "B":
        if B > A:
            print("B")
        else:
            print("A")

#Show first celeb details

#Vs Logo
print(vs)

#Show second celeb details

#If correct, increment current score, assign the second celeb details as the first now then loop

#If not, print you're wrong - End program