programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

#Retrieving items from dictionary
print(programming_dictionary["Function"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again." #"Lopp" is the key, "The action of doing something over and over again." is the value.

#create a new dictionary
empty_dictionary = {}

#wipe an existing dictionary
programming_dictionary = {}

#edit/override an item in a dictionary
programming_dictionary["Bug"] = "This is how to edit an item in a dictionary"

"---------------------------------------------------------------------------------"

#Nesting--------------------------------------------------------------------------

Capitals = {
    "France": "Paris",
    "Nigeria": "Abuja"
}

#Nesting a List in a dictionary
travel_log = {
    "Nigeria": ["Abuja", "Yola", "Kogi"],
    "Saudi Arabia": ["Madinah", "Makkah", "Jeddah"]
}

#Nesting dictionaries in a dictionary
travel_log2 = {
    "Nigeria": {"cities-visited": ["Abuja", "Yola", "Kogi"], "total_visits": 100},
    "Saudi Arabia": {"cities-visited": ["Madinah", "Makkah", "Jeddah"],"total_visits": 1} 
}

#Nesting dictionaries in Lists
travel_log3 = [
    {
        "country": "Nigeria", 
        "cities-visited": ["Abuja", "Yola", "Kogi"], 
        "total_visits": 100
    }, 
    {
        "country": "Saudi Arabia", 
        "cities-visited": ["Madinah", "Makkah", "Jeddah"],
        "total_visits": 1
    }
]