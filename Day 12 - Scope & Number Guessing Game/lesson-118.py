# Scope & Number Guessing Game

# Global scope
player_health = 10 #Available everywhere in the code

# Local Scope
def drink_potion():
    potion_strength = 2    # This variable is only available to this function
    print(potion_strength)
    print(player_health) # It will print

print(player_health) # It will print
print(potion_strength) #Error, It can't be accessed

# There is no Block Scope in Python

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]    # Block level variable

print(new_enemy)    # It will print