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

# Modifying Global Scope

enemies = 1

def increase_enemies():
    # global enemies (Using the global keyword allows you to modify the global varibale but IT IS NOT ADVISABLE)
    # enemies = 2 (this will create a local scope and won't modify the global variable) or enemies += 1 (will not work)
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies() # This method is better (by returning from the function and modifying outside the function)
print(f"enemies outside function: {enemies}")

# Global Constants
PI = 3.142    # The naming convention in Python is to use UPPERCASE for Constants
URL = "https://www.google.com"
X_HANDLE = "@kojozcodess"
