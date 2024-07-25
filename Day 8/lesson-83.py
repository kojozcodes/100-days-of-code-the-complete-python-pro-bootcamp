#Function with Inputs

#Simple Function
def greet():
    print("Hello")
    print("World")
    print("Hello World")

greet()

#Function that allows for input
def greet_with_name(name): #name is a parameter
    print(f"Hello {name}")
    print(f"{name}, would you like some chocolates?")

greet_with_name("Hamza") #"Hamza" is an argument

#Function with more than 1 parameter (Input)
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# greet_with("Hamza", "Nigeria") #Positional Arguments
greet_with(name="Hamza", location="Nigeria") #Keyword Arguments