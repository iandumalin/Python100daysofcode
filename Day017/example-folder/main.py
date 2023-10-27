class User :
    def __init__(self, id = 0) :
        self.id = id
        
    
user_1 = User()
user_2 = User(3)

print(f"{user_1.id}, {user_2.id}")