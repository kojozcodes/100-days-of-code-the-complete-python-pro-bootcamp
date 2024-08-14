class User:


    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "hamza")
user_2 = User("002", "ahmed")

print(user_1.followers)