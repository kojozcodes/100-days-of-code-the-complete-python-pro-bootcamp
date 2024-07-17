#Function with Inputs

#Simple Function
def greet():
    print("Hello")
    print("World")
    print("Hello World")

greet()

#Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"{name}, would you like some chocolates?")

greet_with_name("Hamza")