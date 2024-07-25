#Scope & Number Guessing Game

#Global scope
player_health = 10 #Available everywhere in the code

#Local Scope
def drink_potion():
    potion_strength = 2    # This variable is only available to this function
    print(potion_strength)
    print(player_health) # It will print

print(player_health) # It will print
print(potion_strength) #Error, It can't be accessed