print("Welcome to Retail Row, You are to find your way to the treasure chest!")
first_choice = input("You came to a juntion, do you  want to go left or right?")
first_choice_lower = first_choice.lower()

if first_choice_lower == "left":
  print("congrats, you are one step closer to the chest")
  second_choice = input("Next up, you find a bus and a car. Go towards the bus or the car?")
  second_choice_lower = second_choice.lower()

  if second_choice_lower == "bus":
    print("Hehehe, another player boxes you up like a fish and clips you")

  elif second_choice_lower == "car":
    print("Welldone, Now you've seen 3 houses")
    third_choice = input("Choose the house you want to go, red, blue or yellow?")
    third_choice_lower = third_choice.lower()

    if third_choice_lower == "red":
      print("Drat! A trap eliminated you!")

    elif third_choice_lower == "blue":
      print("Damn!! you met 3 campers and they eliminated you")

    elif third_choice_lower == "yellow":
      print("Yay!!! You found the treasure chest and emote!")

elif first_choice_lower == "right":
  print("Oh no! you met a sweat and he one pumps you")