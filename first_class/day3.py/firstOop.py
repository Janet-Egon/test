class User :
    def __init__(self, username, password) :
        self.username = username
        self.password = password

    def introduce(self):
        print(self.username)
        print(self.password)
            
user1 = User("michael",1234)
user2 = User("mike",64566)        
user1.introduce()
user2.introduce()